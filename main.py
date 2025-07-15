
from dotenv import load_dotenv
import os
from pypdf import PdfReader
from google import genai
from google.genai import types
import openai

# --- CONFIGURATION ---
# Load environment variables from .env file, overriding any existing variables
load_dotenv(override=True)

# --- Google Gemini Configuration ---
#IMPORTANT: Make sure you have a .env file with your Google API key
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-2.5-flash" 

# --- OpenAI ChatGPT Configuration ---
# IMPORTANT: Make sure you have a .env file with your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
# MODEL = "gpt-4o-mini-2024-07-18" # You can change this to "gpt-4" if you have access

def find_cv_file():
    """Finds the first PDF file in the current directory."""
    for file in os.listdir('.'):
        if file.lower().endswith('.pdf'):
            return file
    return None

CV_FILE = find_cv_file()
JOB_DESCRIPTION_FILE = "job_description.txt"
OUTPUT_FILE = "optimized_cv.txt"

# --- FUNCTIONS ---

def read_pdf(file_path):
    """Reads the text content from a PDF file."""
    try:
        with open(file_path, "rb") as f:
            pdf_reader = PdfReader(f)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An error occurred while reading the PDF: {e}"

def read_txt(file_path):
    """Reads the content from a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An error occurred while reading the text file: {e}"

def optimize_cv(cv_content, job_description):
    """Uses Google's Gemini model to optimize the CV for the job description."""
    if not cv_content or cv_content.startswith("Error:"):
        return "Could not optimize CV because the CV content could not be read."
    if not job_description or job_description.startswith("Error:"):
        return "Could not optimize CV because the job description could not be read."

    prompt = f"""
    Here is a CV and a job description.
    Please optimize the CV to be more compliant with Applicant Tracking Systems (ATS) and tailor its content to the provided job description. The writing style should be as close to the original CV as possible. Use the same language as the original CV.
    The output should be a text file that I can use to make manual adjustments.

    CV:
    {cv_content}

    Job Description:
    {job_description}

    Optimized CV (TXT format):
    """

    # --- Call to Google Gemini API ---
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred with the Google API: {e}"

    # --- Call to OpenAI ChatGPT API ---
    # try:
    #     response = openai.chat.completions.create(
    #         model=MODEL,
    #         messages=[
    #             {"role": "system", "content": "You are a helpful assistant that optimizes CVs."},
    #             {"role": "user", "content": prompt}
    #         ]
    #     )
    #     return response.choices[0].message.content
    # except Exception as e:
    #     return f"An error occurred with the OpenAI API: {e}"

def save_to_txt(content, file_path):
    """Saves the given content to a text file."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Successfully saved the optimized CV to '{file_path}'"
    except Exception as e:
        return f"An error occurred while saving the file: {e}"

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    print("Starting CV optimization process...")

    # 1. Read the CV
    if not CV_FILE:
        print("Error: No CV file in PDF format found in the directory.")
        cv_text = "Error: CV file not found."
    else:
        print(f"Reading CV from '{CV_FILE}'...")
        cv_text = read_pdf(CV_FILE)
        if cv_text.startswith("Error:"):
            print(cv_text)
        else:
            print("CV read successfully.")

    # 2. Read the job description
    print(f"Reading job description from '{JOB_DESCRIPTION_FILE}'...")
    job_desc_text = read_txt(JOB_DESCRIPTION_FILE)
    if job_desc_text.startswith("Error:"):
        print(job_desc_text)
    else:
        print("Job description read successfully.")

    # 3. Optimize the CV
    if not cv_text.startswith("Error:") and not job_desc_text.startswith("Error:"):
        print(f"Optimizing CV using '{MODEL}'...")
        optimized_content = optimize_cv(cv_text, job_desc_text)
        print("Optimization complete.")

        # 4. Save the optimized CV
        print(f"Saving optimized CV to '{OUTPUT_FILE}'...")
        result_message = save_to_txt(optimized_content, OUTPUT_FILE)
        print(result_message)

    print("CV optimization process finished.")
