from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

def tailor_resume(master_resume_text, job_description):
    prompt = f"""Tailor this resume to the job description. Keep it ATS-friendly.
Master Resume: {master_resume_text[:4000]}
Job: {job_description}
Output tailored resume in markdown."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Usage: extract text from your resume PDF/DOCX and call this.
