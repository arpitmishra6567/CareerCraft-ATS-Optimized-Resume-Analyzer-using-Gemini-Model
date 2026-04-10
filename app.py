from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import PyPDF2
from PIL import Image
import os
import evs

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_text):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(input_text)
    return response.text


def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text


input_prompt = """
You are an experienced ATS (Applicant Tracking System) and technical hiring assistant.
Evaluate the provided resume against the supplied job description.
Give a clear, practical response with these sections:
1. Match Percentage
2. Missing Keywords
3. Profile Summary
4. Strengths
5. Improvement Suggestions
Keep the tone professional and concise.
"""

st.set_page_config(page_title="Resume ATS Tracker", layout="wide")

col1, col2 = st.columns([3, 1])
with col1:
    st.title("CareerCraft")
    st.header("ATS-Optimized Resume Analyzer Using Gemini Model")
    st.markdown(
        "CareerCraft helps you compare your resume with a target job description, identify missing keywords, and improve your ATS match."
    )
with col2:
    st.image("https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80", use_container_width=True)

evs.add_vertical_space(2)

col3, col4 = st.columns([1, 2])
with col3:
    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?auto=format&fit=crop&w=900&q=80", use_container_width=True)
with col4:
    st.header("Wide Range of Offerings")
    st.markdown(
        """
- ATS-Optimized Resume Analysis
- Resume Optimization Recommendations
- Missing Keyword Detection
- Skill Enhancement Insights
- Job Description Alignment
- Better Interview Preparation Support
        """
    )

evs.add_vertical_space(2)

left, right = st.columns([2, 1])
with left:
    st.header("Embark on Your Career Adventure")
    job_description = st.text_area("Paste the Job Description", height=220)
    uploaded_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
    submit = st.button("Submit")

    if submit:
        if not job_description:
            st.warning("Please paste a job description.")
        elif not uploaded_file:
            st.warning("Please upload a resume PDF.")
        else:
            resume_text = input_pdf_text(uploaded_file)
            final_prompt = f"{input_prompt}\n\nJob Description:\n{job_description}\n\nResume:\n{resume_text}"
            response = get_gemini_response(final_prompt)
            st.subheader("ATS Evaluation")
            st.write(response)
with right:
    st.image("https://images.unsplash.com/photo-1521791136064-7986c2920216?auto=format&fit=crop&w=900&q=80", use_container_width=True)

evs.add_vertical_space(2)
faq1, faq2 = st.columns([1, 2])
with faq1:
    st.image("https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=900&q=80", use_container_width=True)
with faq2:
    st.header("FAQ")
    st.write("**What does CareerCraft do?**")
    st.write("It compares your resume with a job description and highlights areas to improve for ATS screening.")
    evs.add_vertical_space(1)
    st.write("**Which file format is supported?**")
    st.write("Currently, the application supports PDF resumes.")
    evs.add_vertical_space(1)
    st.write("**Do I need an API key?**")
    st.write("Yes. Add your Gemini API key in the .env file before running the app.")
    evs.add_vertical_space(1)
    st.write("**Can this guarantee interview calls?**")
    st.write("No. It helps improve resume alignment, but final hiring decisions depend on multiple factors.")
