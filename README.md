Text-to-Video API
This project provides a FastAPI-based RESTful API that generates videos from text prompts using the Hugging Face Inference API. The API accepts a text prompt, processes it to create a video, and returns the generated video file. The frontend is hosted separately (e.g., at https://text2vid.netlify.app), and CORS is configured to allow communication with it.
Table of Contents

Features
Prerequisites
Installation
Configuration
Usage
API Endpoints
File Structure
Error Handling
Contributing
License

Features

Generate videos from text prompts using Hugging Face's text-to-video model (Wan-AI/Wan2.2-T2V-A14B).
FastAPI backend with CORS support for cross-origin requests.
Environment variable management for secure API key storage.
Unique video file generation with UUID-based naming.
Robust error handling for API failures and timeouts.

Prerequisites

Python 3.8 or higher
A Hugging Face account with an API token for the Inference API
A frontend application hosted at https://text2vid.netlify.app (or adjust CORS settings for your frontend)

Installation

Clone the repository:
git clone https://github.com/your-username/text-to-video-api.git
cd text-to-video-api


Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt



Configuration

Set up environment variables:

Create a .env file in the project root (or update the existing one).
Add your Hugging Face API token:HF_TOKEN=your_hugging_face_api_token


Ensure the .env file is included in .gitignore to prevent exposing sensitive information.


Directory setup:

The application automatically creates a videos directory to store generated video files.



Usage

Run the FastAPI server:
uvicorn api:app --reload

This starts the server on http://localhost:8000. The --reload flag enables auto-reload during development.

Access the API:

Use the root endpoint (/) to verify the server is running:
curl http://localhost:8000/

Response: {"message":"Welcome Brother!"}

Send a POST request to /video_file with a JSON payload containing the prompt:
curl -X POST http://localhost:8000/video_file -H "Content-Type: application/json" -d '{"prompt":"A serene beach at sunset"}'

This returns a video file (video_<uuid>.mp4) generated from the prompt.



Frontend integration:

Ensure your frontend (e.g., hosted at https://text2vid.netlify.app) is configured to send POST requests to the /video_file endpoint.
Update the allow_origins list in api.py if your frontend is hosted elsewhere.



API Endpoints



Endpoint
Method
Description
Request Body
Response



/
GET
Welcome message
None
JSON: {"message":"Welcome Brother!"}


/video_file
POST
Generate and return a video file
JSON: {"prompt": "your text"}
Video file (video/mp4) or JSON error


Request Example
{
  "prompt": "A serene beach at sunset"
}

Response Example

Success: Returns a .mp4 video file with a filename like video_<uuid>.mp4.
Error:{
  "error": "Internal Server Error",
  "detail": "Error message"
}



File Structure
text-to-video-api/
├── .gitignore          # Excludes .env and other sensitive files
├── .env                # Environment variables (e.g., HF_TOKEN)
├── requirements.txt    # Python dependencies
├── api.py             # FastAPI application with endpoints
├── video.py           # Video generation logic using Hugging Face
└── videos/            # Directory for storing generated videos

Error Handling

404 Not Found: Returned if the generated video file is not found on the server.
500 Internal Server Error: Returned for unexpected errors during video generation.
504 Gateway Timeout: Returned if the Hugging Face Inference API times out.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.
