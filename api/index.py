from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional
import uvicorn
import os
import sys

# Add this if your app logic lives somewhere else (like app/main.py)
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")

from app.utils.openai_client import get_openai_response  # adjust as per your structure

app = FastAPI()

@app.post("/api/")
async def process_question(question: str = Form(...), file: Optional[UploadFile] = File(None)):
    try:
        temp_path = None
        if file:
            contents = await file.read()
            temp_path = f"/tmp/{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(contents)

        answer = await get_openai_response(question, temp_path)
        return {"answer": answer}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# For local testing (won't run on Vercel)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
