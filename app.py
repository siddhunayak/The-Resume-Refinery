import streamlit as st
import fitz  # PyMuPDF
import docx
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai

# --- Load API Key from .env ---
# Ensure you have a .env file with GOOGLE_API_KEY="YOUR_KEY"
load_dotenv()
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
except TypeError:
    st.error("Google API Key not found. Please make sure it's set in your .env file or environment variables.")
    st.stop()


# --- File Readers ---
def read_file(uploaded_file):
    """Reads text from an uploaded file based on its extension."""
    if uploaded_file.name.endswith('.pdf'):
        return read_pdf(uploaded_file)
    elif uploaded_file.name.endswith('.docx'):
        return read_docx(uploaded_file)
    else:
        # Assumes .txt or other plain text formats
        return uploaded_file.read().decode("utf-8")

def read_docx(file):
    """Reads text from a .docx file."""
    try:
        doc = docx.Document(file)
        return "\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        st.error(f"Error reading DOCX file: {e}")
        return ""

def read_pdf(file):
    """Reads text from a .pdf file."""
    try:
        # Use a stream to read the file in memory
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return "".join(page.get_text() for page in doc)
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return ""

# --- Gemini Prompts ---
@st.cache_data(show_spinner=False)
def extract_skills(jd):
    """Extracts and cleans key skills from a job description using Gemini."""
    prompt = f"""
From the job description provided below, please extract the top 15-20 most important technical skills, tools, and concepts.
- Return only the names of the skills.
- Each skill should be on a new line.
- Do not use any prefixes like bullet points, numbers, or asterisks.
- Do not add any commentary or explanations.

Job Description:
---
{jd}
---
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt)
        text = response.text.strip()
        
        # Raw skills list from Gemini
        raw_skills = [line.strip() for line in text.split("\n") if line.strip()]
        
        # Clean the skills list to remove unhelpful parenthetical notes
        cleaned_skills = []
        for skill in raw_skills:
            # This regex removes notes like (optional), (implied), (e.g., ...), etc.
            # but preserves valid abbreviations like (LSTM).
            # It looks for common non-abbreviation words inside the parentheses.
            cleaned_skill = re.sub(r'\s*\((optional|implied|e\.g\..*?|written and visual)\)\s*$', '', skill, flags=re.IGNORECASE).strip()
            cleaned_skills.append(cleaned_skill)

        # Further filter to ensure quality
        final_skills = [skill for skill in cleaned_skills if 2 < len(skill) < 50]
        return list(set(final_skills))  # remove duplicates
    except Exception as e:
        st.error(f"Error extracting skills with Gemini: {e}")
        return []

@st.cache_data(show_spinner=False)
def generate_summary(jd, resume):
    """Generates a professional summary using Gemini."""
    prompt = f"""You are an expert resume writer. Based on the provided resume and the target job description, write a compelling 2-3 sentence professional summary. The summary should immediately highlight the candidate's most relevant qualifications and experiences that align with the job's key requirements.

Job Description:
---
{jd}
---

Resume:
---
{resume}
---
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        return model.generate_content(prompt).text.strip()
    except Exception as e:
        return f"Could not generate summary: {e}"

@st.cache_data(show_spinner=False)
def generate_improvements(jd, resume):
    """Generates actionable resume improvements using Gemini."""
    prompt = f"""As an expert career coach, review the provided resume against the job description.
Provide a list of 3 to 5 specific, actionable improvements the candidate can make to their resume to better align with this specific job.
Focus on re-framing existing experience, quantifying achievements, and incorporating missing keywords naturally.

Job Description:
---
{jd}
---

Resume:
---
{resume}
---
"""
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        return model.generate_content(prompt).text.strip()
    except Exception as e:
        return f"Could not generate improvements: {e}"


# --- Skill Matching Logic (Corrected and Improved) ---
def match_skills(resume_text, skills):
    """
    Matches skills from a list against resume text using robust regex.
    Handles skills with abbreviations in parentheses, e.g., "Long Short-Term Memory (LSTM)".
    """
    resume_lower = resume_text.lower()
    matched = []
    missing = []
    
    # Pattern to find abbreviations in parentheses
    abbr_pattern_extract = re.compile(r'\((.*?)\)')

    for skill in skills:
        skill_lower = skill.lower()
        found = False

        # Check for abbreviations in the skill string
        match = abbr_pattern_extract.search(skill_lower)
        if match:
            # Main skill part, e.g., "long short-term memory"
            main_skill = abbr_pattern_extract.sub('', skill_lower).strip()
            # Abbreviation part, e.g., "lstm"
            abbr = match.group(1).strip()

            # Create regex for both parts to find them as whole words
            main_pattern = r'\b' + re.escape(main_skill) + r'\b'
            abbr_pattern_search = r'\b' + re.escape(abbr) + r'\b'

            # If either the full name OR the abbreviation is found, it's a match
            if re.search(main_pattern, resume_lower) or re.search(abbr_pattern_search, resume_lower):
                found = True
        else:
            # Original logic for skills without abbreviations
            pattern = r'\b' + re.escape(skill_lower) + r'\b'
            if re.search(pattern, resume_lower):
                found = True
        
        if found:
            matched.append(skill)
        else:
            missing.append(skill)
            
    return matched, missing

def score_resume(matched_count, total_skills):
    """Calculates the resume score based on matched skills."""
    return round((matched_count / total_skills) * 100) if total_skills > 0 else 0

# --- Streamlit UI ---
st.set_page_config(page_title="AI Resume Tailor", layout="wide")
st.title("🧠 AI Resume Tailor with Google Gemini")

# --- File Uploaders ---
col1, col2 = st.columns(2)
with col1:
    st.subheader("📄 Upload Resume (.pdf, .docx, .txt)")
    resume_file = st.file_uploader("Drag and drop file here", type=["pdf", "docx", "txt"], label_visibility="collapsed", key="resume_uploader")
with col2:
    st.subheader("📝 Upload Job Description (.pdf, .docx, .txt)")
    jd_file = st.file_uploader("Drag and drop file here", type=["pdf", "docx", "txt"], label_visibility="collapsed", key="jd_uploader")

# --- Main Logic ---
if resume_file and jd_file:
    resume_text = read_file(resume_file)
    jd_text = read_file(jd_file)

    if resume_text and jd_text:
        with st.spinner("🔍 Extracting key skills from job description..."):
            skills_from_jd = extract_skills(jd_text)

        st.info("🔍 Extracted Skills:")
        st.write(skills_from_jd)

        matched, missing = match_skills(resume_text, skills_from_jd)
        score = score_resume(len(matched), len(skills_from_jd))

        st.subheader("📊 Resume Score")
        st.progress(score)
        st.markdown(f"<h3 style='text-align: center;'>{score}%</h3>", unsafe_allow_html=True)


        col1, col2 = st.columns(2)
        with col1:
            st.success(f"✅ Matched Skills ({len(matched)})")
            st.write(", ".join(sorted(matched)) if matched else "None")
        with col2:
            st.warning(f"⚠️ Missing Skills ({len(missing)})")
            st.write(", ".join(sorted(missing)) if missing else "None")

        st.divider()

        st.subheader("💬 Gemini-Generated Summary")
        with st.spinner("✍️ Generating tailored summary..."):
            summary = generate_summary(jd_text, resume_text)
            st.markdown(f"> {summary}")

        st.subheader("🔧 Gemini's Suggested Improvements")
        with st.spinner("💡 Generating improvement suggestions..."):
            suggestions = generate_improvements(jd_text, resume_text)
            st.markdown(suggestions)

elif resume_file or jd_file:
    st.info("Please upload both your resume and the job description to proceed.")
