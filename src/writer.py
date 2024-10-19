import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the generative AI model
api_key = os.getenv('google_ai_studio_key')
genai.configure(api_key=api_key)

generator_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a personal assistant helping in my job search in a very competitive field. You are "
                       "experienced at writing CVs and you will be helping finetune my CV to the Job Descriptions I "
                       "want to apply for by emphasizing what is necessary, downplaying some and removing others "
                       "completely. Also add a note for skills I could add if I had them. I will also want a cover "
                       "letter as well"
)


def write_cv(cv, jd):
    prompt = (f"You are my personal assistant helping me apply for jobs in a very competitive field. Focus on "
              f"personal summary, skills, experience and certification/licences.This is my CV containing everything "
              f"about me that may be relevant for this purpose as well as a Job Description for a job I am interested "
              f"in. Your task is to use all that information to craft a concise, Applicant Tracking System (ATS) "
              f"compliant CV for the given job description. My personal information is here {cv}"
              f"and the job description is {jd}.")

    response = generator_model.generate_content(prompt)
    return response.text


def write_cover(cv, jd):
    prompt = (f"You are my personal assistant helping me apply for jobs in a very competitive field. This is my CV "
              f"containing everything about me that may be relevant for this purpose as well as a Job Description for "
              f"a job I am interested in. Your task is to write a cover letter for this job description based on my "
              f"CV. My personal information is here {cv} and the job description is {jd}.")

    response = generator_model.generate_content(prompt)
    return response.text
