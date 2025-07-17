# 🧠 AI Resume Tailor ✨

An intelligent Streamlit application powered by Google Gemini that helps you **analyze, score, and tailor your resume** for any job description. Whether you're optimizing for ATS or trying to impress recruiters, this tool gives you actionable insights to improve your chances of landing the job.

---

## 🚀 Core Features

- **AI Skill Extraction:** Automatically identifies key skills and keywords from any job description using Gemini API.
- **Resume Scoring:** Instantly generates a match score to evaluate how well your resume aligns with job requirements.
- **Keyword Analysis:** Side-by-side display of _Matched Skills_ vs _Missing Skills_.
- **AI-Generated Summary:** Creates a personalized, professional summary for the specific role.
- **Actionable Improvements:** AI-powered suggestions to re-frame experiences, quantify achievements, and improve overall resume impact.

---

## 🛠️ Tech Stack

| Layer        | Tools Used                          |
|--------------|-------------------------------------|
| Backend      | Python                              |
| Frontend     | Streamlit                           |
| AI & NLP     | Google Gemini API (gemini-1.5-flash-latest) |
| File Parsing | `PyMuPDF` (PDFs), `python-docx` (DOCX) |
| Matching     | `re` module (Regex)                 |
| Env Mgmt     | `python-dotenv`                     |

---

## ⚙️ How It Works

1. **Text Extraction:** Parses `.pdf`, `.docx`, and `.txt` resume and JD files into plain text.
2. **AI Skill Analysis:** Uses Gemini to extract critical skills from the JD.
3. **Scoring & Matching:** Uses regex to match skills from JD with your resume and calculates a match score.
4. **Content Generation:** Prompts Gemini to:
   - Generate a **tailored summary**
   - Suggest **resume improvements**
5. **Display:** Renders all outputs in an intuitive, interactive Streamlit dashboard.

---

## 🏁 Quick Start

Follow these steps to get started locally:

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Tailor.git
cd AI-Resume-Tailor
2. Set Up Your Environment
Create a .env file in the root directory and add your Google Gemini API key:
```

```bash
env
Copy
Edit
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
