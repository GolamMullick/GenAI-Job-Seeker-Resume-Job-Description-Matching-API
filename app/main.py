from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="GenAI Job Seeker Matcher API",
    description="Upload your resume and jobs, get semantic matches and custom cover letters!",
    version="1.0"
)
app.include_router(router)
