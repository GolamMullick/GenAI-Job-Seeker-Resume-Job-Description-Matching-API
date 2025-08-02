import openai
import chromadb
import numpy as np
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
chroma_client = chromadb.Client(path=os.getenv("CHROMA_DB_PATH", "./chroma_db"))

RESUME_COLLECTION = "resume"
JOBS_COLLECTION = "jobs"

resume_storage = {"text": "", "embedding": None}
jobs_storage = []

def embed(text):
    resp = openai.Embedding.create(input=[text], model="text-embedding-ada-002")
    return np.array(resp["data"][0]["embedding"])

def process_resume(resume_text):
    emb = embed(resume_text)
    resume_storage["text"] = resume_text
    resume_storage["embedding"] = emb

def process_jobs(job_list):
    jobs_storage.clear()
    for idx, job in enumerate(job_list):
        emb = embed(job)
        jobs_storage.append({"job": job, "embedding": emb, "idx": idx})

def get_matches():
    resume_emb = resume_storage["embedding"]
    matches = []
    for job in jobs_storage:
        score = float(np.dot(resume_emb, job["embedding"]) / (np.linalg.norm(resume_emb) * np.linalg.norm(job["embedding"])))
        matches.append({"job": job["job"], "score": score, "idx": job["idx"]})
    matches = sorted(matches, key=lambda x: -x["score"])
    for m in matches:
        m["why_match"] = f"Score: {m['score']:.2f}. Resume closely matches required skills."
    return matches
