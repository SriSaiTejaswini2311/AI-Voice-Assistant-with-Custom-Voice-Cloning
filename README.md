# Voice Assistant Project (XTTS)

## Overview
This project is a voice assistant application that allows users to interact using voice commands. It supports voice cloning, audio processing, and provides a web interface for user interaction.

## Features
- Record and upload voice samples
- Clone voices and generate responses
- Web interface for interaction
- Audio file management
- User authentication (login page)

## Folder Structure
```
XTTS/
  recordings/           # Original and processed audio recordings
  voice_assistant/
    app.py              # Main application logic
    cloned_voices.json  # Stores cloned voice data
    input.wav           # Input audio file
    output.wav          # Output audio file
    requirements.txt    # Python dependencies
    package.json        # Node.js dependencies (if any)
    test.py             # Test scripts
    static/             # Static files (HTML, CSS, MP3)
    templates/          # HTML templates
    uploads/            # Uploaded audio files
    voice_samples/      # Sample voices for cloning
    voices/             # Generated/processed voices
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repo-url>
   ```
2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```
3. (Optional) Install Node.js dependencies:
   ```
   npm install
   ```
4. Run the application:
   ```
   python app.py
   ```

## Usage
- Access the web interface via your browser.
- Record or upload your voice.
- Interact with the assistant and receive responses.

## Dependencies
- Python 3.11+
- Flask (or relevant web framework)
- Other dependencies listed in `requirements.txt` and `package.json`

## Project Pipeline

### Voice Assistant Flow
1. **User Interaction**: The user accesses the web interface and records or uploads a `.wav` audio file.
2. **Audio Storage**: The uploaded/recorded audio is saved in the `recordings/` folder.
3. **Text Processing**: The user submits a text query via the interface. The query is sent to the backend (`app.py`).
4. **LLM Response**: The backend uses LangChain and Anthropic's Claude model to generate a conversational response.
5. **Voice Generation**: If a custom voice is selected, the TTS (Coqui) model uses the chosen `.wav` file as a speaker reference to synthesize the response in that voice. The output is saved as `output.wav`.
6. **Playback/Download**: The user can play or download the generated response from the web interface.
7. **Session Management**: User history and session data are managed using Flask sessions.

**Tools & Technologies:**
- Flask (web server, session management)
- LangChain + Anthropic Claude (LLM for conversation)
- Coqui TTS (voice cloning and synthesis)
- HTML/CSS/JS (frontend)

### Voice Cloning Studio Flow
1. **Voice Sample Upload**: User uploads a `.wav` file to serve as a reference voice.
2. **Sample Storage**: The sample is stored in `recordings/` or `voice_samples/`.
3. **Text-to-Speech**: User provides text and selects a language and speaker sample.
4. **Voice Synthesis**: The TTS model generates speech in the selected voice and language, saving the result as `output.wav`.
5. **Playback/Download**: User can play or download the generated audio.

**Tools & Technologies:**
- Flask (web server)
- Coqui TTS (voice cloning)
- HTML/CSS/JS (frontend)

---

## Contributing
Feel free to submit issues or pull requests for improvements.

## License
Specify your license here (e.g., MIT, Apache 2.0).


## Deployment Setup
For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md).

### Quick Steps
1. Prepare your environment (Python 3.11+, Node.js if needed).
2. Clone the repository and install dependencies:
   ```sh
   git clone <repo-url>
   cd XTTS/voice_assistant
   pip install -r requirements.txt
   # (Optional) npm install
   ```
3. Create a `.env` file for secrets (see DEPLOYMENT.md for example).
4. Run the app:
   ```sh
   python app.py
   ```
5. For production, use Gunicorn or Docker (see DEPLOYMENT.md).
