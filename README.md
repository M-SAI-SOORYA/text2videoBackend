The Hugging face Open Source Model used here is Wan-AI/Wan2.2-T2V-A14B
I used HF Token so the rate limit is 3 videos, not more than that 
---

# 🎬 Text-to-Video API

A **FastAPI-based RESTful API** that converts text prompts into **videos** using the **Hugging Face Inference API**. Perfect for integrating text-to-video functionality into your apps or frontend projects.

Frontend example: [https://text2vid.netlify.app](https://text2vid.netlify.app) 🌐

---

## 📖 Table of Contents

* [✨ Features](#-features)
* [⚡ Prerequisites](#-prerequisites)
* [🚀 Installation](#-installation)
* [🛠 Configuration](#-configuration)
* [🎯 Usage](#-usage)
* [📝 API Endpoints](#-api-endpoints)
* [📂 File Structure](#-file-structure)
* [❌ Error Handling](#-error-handling)
* [🤝 Contributing](#-contributing)
* [📄 License](#-license)

---

## ✨ Features

* 🎥 Generate videos from text using **Wan-AI/Wan2.2-T2V-A14B** model
* ⚡ **FastAPI backend** with CORS support
* 🔒 Secure API key management via **environment variables**
* 🆔 Unique video filenames using **UUIDs**
* 🛡 Robust **error handling** for API failures and timeouts

---

## ⚡ Prerequisites

* Python **3.8+** 🐍
* Hugging Face account with an **API token** 🔑
* Frontend hosted at [https://text2vid.netlify.app](https://text2vid.netlify.app) 🌐 (or adjust CORS settings)

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/text-to-video-api.git
cd text-to-video-api
```

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠 Configuration

### Environment Variables

1. Create a `.env` file in the project root
2. Add your Hugging Face API token:

```env
HF_TOKEN=your_hugging_face_api_token
```

> ⚠️ Make sure `.env` is in `.gitignore` to avoid exposing secrets

### Directory Setup

* The app automatically creates a `videos/` directory to store generated videos 🗂

---

## 🎯 Usage

Run the FastAPI server:

```bash
uvicorn api:app --reload
```

Server runs at `http://localhost:8000` 🌟

### Test the API

**Root endpoint:**

```bash
curl http://localhost:8000/
```

**Response:**

```json
{"message":"Welcome Brother!"}
```

**Generate a video:**

```bash
curl -X POST http://localhost:8000/video_file \
-H "Content-Type: application/json" \
-d '{"prompt":"A serene beach at sunset"}'
```

* Returns a `.mp4` file: `video_<uuid>.mp4` 🎬

### Frontend Integration

* Ensure your frontend sends POST requests to `/video_file`
* Update `allow_origins` in `api.py` if hosting frontend elsewhere 🌍

---

## 📝 API Endpoints

| Endpoint      | Method | Description               | Request Body                    | Response                               |
| ------------- | ------ | ------------------------- | ------------------------------- | -------------------------------------- |
| `/`           | GET    | Welcome message           | None                            | JSON: `{"message":"Welcome Brother!"}` |
| `/video_file` | POST   | Generate and return video | JSON: `{"prompt": "your text"}` | Video file (`.mp4`) or JSON error      |

**Request Example:**

```json
{
  "prompt": "A serene beach at sunset"
}
```

**Response Example:**

* ✅ **Success:** `.mp4` video file named `video_<uuid>.mp4`
* ❌ **Error:**

```json
{
  "error": "Internal Server Error",
  "detail": "Error message"
}
```

---

## 📂 File Structure

```
text-to-video-api/
├── .gitignore          # Excludes .env and sensitive files
├── .env                # Environment variables (e.g., HF_TOKEN)
├── requirements.txt    # Python dependencies
├── api.py              # FastAPI app with endpoints
├── video.py            # Video generation logic
└── videos/             # Generated videos storage
```

---

## ❌ Error Handling

* 404 Not Found – Generated video not found 🕵️‍♂️
* 500 Internal Server Error – Unexpected video generation error ⚠️
* 504 Gateway Timeout – Hugging Face API timeout ⏳

---

## 🤝 Contributing

1. Fork the repository 🍴
2. Create a branch:

```bash
git checkout -b feature/your-feature
```

3. Commit your changes:

```bash
git commit -m "Add your feature"
```

4. Push to the branch:

```bash
git push origin feature/your-feature
```

5. Open a pull request ✨

---

## 📄 License

This project is licensed under **MIT License**. See the LICENSE file for details 📝

---

If you want, I can **also add GitHub badges** for Python version, license, and Hugging Face API integration to make it look even more professional.

Do you want me to add the badges?
