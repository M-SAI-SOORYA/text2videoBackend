import os
import uuid
from huggingface_hub import InferenceClient, InferenceTimeoutError
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
os.makedirs("videos", exist_ok=True)

def generate_video(prompt: str) -> str:
    """Generates a video from a prompt and saves it with a unique filename."""
    api_key = os.getenv("HF_TOKEN")
    
    if not api_key:
        raise ValueError("HF_TOKEN environment variable is not set.")

    client = InferenceClient(
        provider="fal-ai", 
        api_key=api_key,
        
    )

    try:
        print(f"Generating video for prompt: {prompt}")
        video = client.text_to_video(prompt, model="Wan-AI/Wan2.2-T2V-A14B")

        if not video:
            raise ValueError("No video data received from API.")

      
        filename = f"video_{uuid.uuid4().hex}.mp4"
        output_path = os.path.join("videos", filename)

  
        with open(output_path, "wb") as f:
            f.write(video)

        print(f"Video saved at {output_path}")
        return output_path

    except InferenceTimeoutError:
        raise HTTPException(status_code=504, detail="Inference Timeout Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
