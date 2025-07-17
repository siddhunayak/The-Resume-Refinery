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

Follow these steps to get the project running on your local machine.

---

### 🔐 Step 2: Set Up Your Environment

Create a `.env` file in the root directory and add your **Google Gemini API key** in the following format:

```env
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
### 📦 Step 3: Install Dependencies

Install all required Python packages using the following command:
```
```bash
pip install -r requirements.txt
``
Step 4: Run the Streamlit App
Start the application with:

bash
Copy
Edit
streamlit run app.py
Once started, open the provided URL in your browser (typically http://localhost:8501).

📂 Supported File Formats
.pdf — parsed using PyMuPDF

.docx — parsed using python-docx

.txt — read as plain text

✅ You're All Set!
Upload your resume and job description

Get AI-extracted skills and a match score

View matched and missing skills

Receive a personalized summary and improvement suggestions

📜 License
This project is licensed under the MIT License.
See the LICENSE file for more details.


Ask ChatGPT


