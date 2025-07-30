# Deployment Setup for Voice Assistant Project (XTTS)

## Deployment Instructions

### 1. Environment Preparation
- Ensure you have Python 3.11+ installed.
- (Optional) For frontend assets, Node.js may be required if you use Tailwind or other npm packages.

### 2. Clone the Repository
```sh
git clone <repo-url>
cd XTTS/voice_assistant
```

### 3. Install Dependencies
- Python:
  ```sh
  pip install -r requirements.txt
  ```
- (Optional) Node.js:
  ```sh
  npm install
  ```

### 4. Environment Variables
- Create a `.env` file in the `voice_assistant` folder for any required secrets (e.g., API keys, secret keys).
- Example:
  ```env
  SECRET_KEY=your-secret-key
  ANTHROPIC_API_KEY=your-anthropic-key
  ```

### 5. Run the Application
```sh
python app.py
```
- The Flask server will start. Access the web interface at `http://localhost:5000`.

### 6. Production Deployment
- For production, use a WSGI server like Gunicorn or uWSGI:
  ```sh
  gunicorn app:app
  ```
- Set up reverse proxy (e.g., Nginx) for HTTPS and static file serving.
- Configure environment variables securely.

### 7. File & Folder Permissions
- Ensure the following folders are writable by the application:
  - `recordings/`
  - `uploads/`
  - `voice_samples/`
  - `voices/`
  - `temp/`

### 8. Optional: Docker Deployment
- Create a `Dockerfile` for containerized deployment.
- Example:
  ```Dockerfile
  FROM python:3.11
  WORKDIR /app
  COPY . .
  RUN pip install -r requirements.txt
  CMD ["python", "app.py"]
  ```
- Build and run:
  ```sh
  docker build -t xtts-assistant .
  docker run -p 5000:5000 xtts-assistant
  ```

---

## Notes
- For GPU support, ensure your environment supports CUDA and install compatible versions of TTS and dependencies.
- Secure your `.env` file and never commit secrets to version control.
- Monitor logs and set up error handling for production.
