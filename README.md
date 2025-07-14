# CV Optimizer

This project optimizes a CV based on a job description using Large Language Models (LLMs). By default, it uses Google's Gemini API, but it can be configured to use OpenAI's API as well.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Google API key to the `.env` file:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```
   - If you want to use the OpenAI API, you also need to add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

3. **Add your CV and job description:**
   - Place your CV (in PDF format) in the root directory. The script will automatically find the first PDF file.
   - Add the job description to `job_description.txt`.

## Usage

Run the `main.py` script to generate an optimized version of your CV:

```bash
python main.py
```

The optimized CV will be saved in `optimized_cv.txt`.

## Configuration

To switch between the Google Gemini and OpenAI models, you can edit the `main.py` file.

- **For Google Gemini (default):**
  ```python
  MODEL = "gemini-1.5-flash"
  ```

- **For OpenAI:**
  - Comment out the Google Gemini configuration.
  - Uncomment the OpenAI configuration and choose your model:
  ```python
  # openai.api_key = os.getenv("OPENAI_API_KEY")
  # MODEL = "gpt-4o-mini" # You can change this to "gpt-4" if you have access
  ```
