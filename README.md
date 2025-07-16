# VideoSummarizerAI

VideoSummarizerAI transcribes your videos and generates smart, human-like summaries so you never miss the main points.

## Features
- Upload videos
- Whisper ASR for transcription
- GPT-4 for summarization
- SQLite for storing your summaries

## Setup
1. Add `.env` with your OpenAI API key.
2. Install: `pip install -r requirements.txt`
3. Run: `uvicorn app.main:app --reload`
