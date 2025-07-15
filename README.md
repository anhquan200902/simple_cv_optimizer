# AI-Powered CV Optimizer

A Python-based command-line tool that analyzes a CV and a job description to generate an optimized version of the CV tailored for Applicant Tracking Systems (ATS). It leverages Large Language Models (LLMs) like Google Gemini or OpenAI's GPT to align the CV's content with the job requirements while preserving the original tone and language.

## Features

- **ATS Optimization:** Rewrites CV content to better match keywords and phrases from a job description, increasing its chances of passing through automated screening systems.
- **LLM Integration:** Seamlessly connects with Google Gemini (default) or OpenAI GPT APIs to process and generate text.
- **Automatic File Detection:** Scans the root directory to automatically find the user's CV in PDF format.
- **Text Extraction:** Parses and extracts text from PDF files for analysis.
- **Translation:** Includes a separate script to translate the optimized CV into English using the same LLM services.
- **Configurable:** Easily switch between different LLM providers and models by editing the configuration in the scripts.

## How It Works

The primary script, `main.py`, executes the following steps:
1.  **Loads Environment Variables:** Reads API keys (`GOOGLE_API_KEY`, `OPENAI_API_KEY`) from a `.env` file.
2.  **Finds and Reads Files:**
    - Locates the first `.pdf` file in the project directory to use as the CV.
    - Reads the job description from `job_description.txt`.
3.  **Constructs a Prompt:** Creates a detailed prompt for the LLM, providing the CV text and the job description as context. The prompt instructs the model to act as an ATS expert and optimize the CV.
4.  **Calls the LLM API:** Sends the prompt to the configured LLM (Gemini by default) and receives the optimized CV text.
5.  **Saves the Output:** Writes the generated text to `optimized_cv.txt`.

A secondary script, `translate.py`, can be run to translate the content of `optimized_cv.txt` into English.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- An API key from Google AI or OpenAI

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up your environment variables:**
    - Create a file named `.env` in the root directory.
    - Add your API key(s) to it. For Google Gemini, add:
      ```env
      GOOGLE_API_KEY="your_google_api_key_here"
      ```
    - For OpenAI, add:
      ```env
      OPENAI_API_KEY="your_openai_api_key_here"
      ```

4.  **Add your files:**
    - Place your CV (as a `.pdf` file) in the root directory.
    - Create a file named `job_description.txt` and paste the job description into it.

## Usage

1.  **Optimize the CV:**
    Run the `main.py` script to generate the optimized version of your CV.
    ```bash
    python main.py
    ```
    The output will be saved in `optimized_cv.txt`.

2.  **Translate the CV (Optional):**
    If your CV is not in English, you can translate it by running the `translate.py` script.
    ```bash
    python translate.py
    ```
    The translated text will be saved in `translated_cv.txt`.

## Configuration

The tool is configured to use Google Gemini by default. To switch to OpenAI or use a different model, you need to edit `main.py` and/or `translate.py`:

1.  **Locate the Configuration Block:** Find the model configuration section at the top of the script.
2.  **Switch Models:** Comment out the active model lines and uncomment the lines for the provider you wish to use.

**Example in `main.py`:**
```python
# --- Google Gemini Configuration ---
# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
# MODEL = "gemini-2.5-flash"

# --- OpenAI ChatGPT Configuration ---
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4o-mini" # Or whatever model you prefer
```
3.  **Switch API Calls:** Further down in the script, comment out the API call for the old provider and uncomment the one for the new provider.

## Future Improvements

- [ ] Develop a simple web interface (e.g., using Flask or Streamlit) for a more user-friendly experience.
- [ ] Add support for more input file formats, such as `.docx` and `.txt`.
- [ ] Implement a batch processing feature to optimize a CV for multiple job descriptions at once.
- [ ] Enhance error handling and provide more detailed feedback to the user.