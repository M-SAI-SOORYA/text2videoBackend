from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import os
from video import generate_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://text2vid.netlify.app/"],  # Adjust as necessary
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/video_file")
async def get_video_file(req: PromptRequest):
    try:
        print(f"Received prompt: {req.prompt}")
        video_path = generate_video(req.prompt)

        # Ensure the video path is absolute
        original_video_path = os.path.join(os.path.dirname(__file__), video_path)

        if not os.path.exists(original_video_path):
            raise HTTPException(status_code=404, detail="Video file not found")

        return FileResponse(
            path=original_video_path,
            media_type="video/mp4",
            filename=os.path.basename(original_video_path)
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": "Internal Server Error", "detail": str(e)},
        )
        
app.get("/")
def welcome():
    return {"message":"Welcome Brother!"}
