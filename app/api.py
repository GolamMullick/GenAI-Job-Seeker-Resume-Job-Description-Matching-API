from fastapi import APIRouter, UploadFile, File, Form
from app.match import process_resume, process_jobs, get_matches
from app.cover_letter import generate_cover_letter

router = APIRouter()

@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):
    text = (await file.read()).decode(errors="ignore")
    process_resume(text)
    return {"status": "resume uploaded"}

@router.post("/upload_jobs")
async def upload_jobs(jobs: str = Form(...)):
    # Accept jobs as a single string (e.g., JSON list)
    import json
    job_list = json.loads(jobs)
    process_jobs(job_list)
    return {"status": "jobs uploaded"}

@router.get("/get_matches")
def match_jobs():
    matches = get_matches()
    return {"matches": matches}

@router.post("/generate_cover_letter")
async def gen_cover(job_idx: int = Form(...)):
    letter = generate_cover_letter(job_idx)
    return {"cover_letter": letter}
