# CareerCraft: ATS-Optimized Resume Analyzer Using Gemini Model

CareerCraft is a Streamlit application that compares a user's resume against a job description and generates ATS-focused feedback using Google's Gemini model.

## Features
- Upload resume in PDF format
- Paste a target job description
- Get ATS-style evaluation and keyword feedback
- Identify strengths and improvement suggestions

## Project Structure
- `app.py` - Main Streamlit app
- `evs.py` - Utility for adding vertical space
- `.env.example` - API key template
- `requirements.txt` - Python dependencies

## Setup
1. Clone the repository.
2. Create a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file from `.env.example` and add your Gemini API key.
5. Run the app:
   ```bash
   streamlit run app.py
   ```

## Notes
- The app uses `gemini-1.5-flash`.
- Resume parsing works for text-based PDFs.
- Image assets are loaded from public URLs.
