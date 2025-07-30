from flask import Flask, render_template, request, send_file, jsonify, redirect, url_for, session
from TTS.api import TTS
from pathlib import Path
import uuid, os
from langchain_anthropic import ChatAnthropic
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

app = Flask(__name__)
app.secret_key = "your-secret-key"  # Required for sessions

UPLOAD_FOLDER = Path("recordings")
UPLOAD_FOLDER.mkdir(exist_ok=True)
output_path = Path("output.wav")

TTS_MODEL = TTS("tts_models/multilingual/multi-dataset/your_tts", gpu=False)

llm = ChatAnthropic(
    model="claude-3-haiku-20240307",
    temperature=0.5,
    model_kwargs={"system": "You're Gen Z voice assistants. Be witty, casual, and super friendly. Use fun slang. Always give crisp, helpful responses unless asked for more. Do not give emoji in output"}
)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        if email:
            session["email"] = email
            session["history"] = []  # initialize history
            return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/", methods=["GET", "POST"])
def index():
    if "email" not in session:
        return redirect(url_for("login"))

    message = ""
    recordings = [f.name for f in UPLOAD_FOLDER.glob("*.wav")]
    
    if request.method == "POST":
        try:
            if "recording" in request.files and request.form.get("rec_name"):
                file = request.files["recording"]
                name = request.form["rec_name"].strip()
                if file and file.filename.endswith(".wav"):
                    save_path = UPLOAD_FOLDER / f"{name}.wav"
                    file.save(save_path)
                    message = f"Recording '{name}' uploaded."
                    recordings = [f.name for f in UPLOAD_FOLDER.glob("*.wav")]
        except Exception as e:
            message = f"Error uploading file: {str(e)}"

    return render_template("index.html", recordings=recordings, message=message, history=session.get("history", []))

@app.route("/process", methods=["POST"])
def process_text():
    if "email" not in session:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.json
    user_input = data.get("user_input")
    voice_choice = data.get("voice_choice", "default")

    try:
        memory = ConversationBufferMemory()  # fresh memory each session
        conversation = ConversationChain(llm=llm, memory=memory)
        response = conversation.run(user_input)

        # Store history in session
        session["history"].append({"user": user_input, "bot": response})
        session.modified = True

        if voice_choice != "default":
            speaker_file = UPLOAD_FOLDER / voice_choice
            if speaker_file.exists():
                TTS_MODEL.tts_to_file(
                    text=response,
                    speaker_wav=str(speaker_file),
                    language="en",
                    file_path=str(output_path)
                )

        return jsonify({
            "response": response,
            "voice_generated": voice_choice != "default"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/download")
def download():
    try:
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route("/play")
def play():
    try:
        return send_file(output_path, mimetype="audio/wav")
    except Exception as e:
        return jsonify({"error": str(e)}), 404

if __name__ == "__main__":
    app.run(debug=True)
