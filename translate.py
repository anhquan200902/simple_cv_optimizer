
from dotenv import load_dotenv
import os
import google.generativeai as genai
import openai

# --- CONFIGURATION ---
# Load environment variables from .env file, overriding any existing variables
load_dotenv(override=True)

# --- Google Gemini Configuration ---
#IMPORTANT: Make sure you have a .env file with your Google API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
MODEL = "gemini-1.5-flash" 

# --- OpenAI ChatGPT Configuration ---
# IMPORTANT: Make sure you have a .env file with your OpenAI API key
# openai.api_key = os.getenv("OPENAI_API_KEY")
# MODEL = "gpt-4o-mini" # You can change this to "gpt-4" if you have access

INPUT_FILE = "optimized_cv.txt"
OUTPUT_FILE = "translated_cv.txt"

# --- FUNCTIONS ---

def read_txt(file_path):
    """Reads the content from a text file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: The file '{file_path}' was not found."
    except Exception as e:
        return f"An error occurred while reading the text file: {e}"

def translate_text(text):
    """Uses Google's Gemini model to translate the text to English."""
    if not text or text.startswith("Error:"):
        return "Could not translate text because the input text could not be read."

    prompt = f"""
    Please translate the following text to English.

    Text to translate:
    {text}

    Translated text (English):
    """

    # --- Call to Google Gemini API ---
    try:
        model = genai.GenerativeModel(MODEL)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"An error occurred with the Google API: {e}"

    # --- Call to OpenAI ChatGPT API ---
    # try:
    #     response = openai.chat.completions.create(
    #         model=MODEL,
    #         messages=[
    #             {"role": "system", "content": "You are a helpful assistant that translates text to English."},
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
        return f"Successfully saved the translated CV to '{file_path}'"
    except Exception as e:
        return f"An error occurred while saving the file: {e}"

# --- MAIN EXECUTION ---

if __name__ == "__main__":
    print("Starting translation process...")

    # 1. Read the optimized CV
    print(f"Reading optimized CV from '{INPUT_FILE}'...")
    cv_text = read_txt(INPUT_FILE)
    if cv_text.startswith("Error:"):
        print(cv_text)
    else:
        print("Optimized CV read successfully.")

    # 2. Translate the CV
    if not cv_text.startswith("Error:"):
        print(f"Translating CV using '{MODEL}'...")
        translated_content = translate_text(cv_text)
        print("Translation complete.")

        # 3. Save the translated CV
        print(f"Saving translated CV to '{OUTPUT_FILE}'...")
        result_message = save_to_txt(translated_content, OUTPUT_FILE)
        print(result_message)

    print("Translation process finished.")
