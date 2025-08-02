# GenAI Job Seeker Matcher API

A FastAPI backend for uploading your resume and matching it with job ads using semantic AI embeddings. Also generates custom cover letters!

## Features
- Upload resume (PDF or text)
- Upload job descriptions
- AI-powered semantic match ranking
- Custom cover letter generator
- Dockerized and cloud-ready

## Quickstart

```bash
git clone https://github.com/YOURUSERNAME/genai-jobseeker-matcher.git
cd genai-jobseeker-matcher
cp .env.example .env
# Add your OpenAI key
docker build -t genai-jobseeker-matcher .
docker run -p 8000:8000 --env-file .env genai-jobseeker-matcher
# Try http://localhost:8000/docs
```
