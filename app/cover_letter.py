import openai
import os
from app.match import resume_storage, jobs_storage

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_cover_letter(job_idx):
    if not jobs_storage or resume_storage["text"] == "":
        return "No resume or jobs found. Please upload first."
    job_desc = jobs_storage[job_idx]["job"]
    prompt = (
        f"Write a short, professional cover letter for the following job description:\n{job_desc}\n"
        f"Based on this resume:\n{resume_storage['text']}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
