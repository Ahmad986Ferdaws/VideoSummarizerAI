# app/transcriber.py

import os
import openai

openai.api_key = os.getenv(\"OPENAI_API_KEY\")aaaa
                           

                           def transcribe_video(file_path: str) -> str:
    with open(file_path, \"rb\") as video_file:
        transcript = openai.Audio.transcribe(\"whisper-1\", video_file)
    return transcript[\"text\"]
    
if __name__ == \"__main__\":
    result = transcribe_video(\"videos/sample.mp4\")
    print(\"Transcript:\\n\", result)
