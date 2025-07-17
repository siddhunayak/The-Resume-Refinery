
🎯 **AI Resume Tailor**


# 🧠 AI Resume Tailor ✨

An intelligent Streamlit application powered by **Google Gemini API** that helps you analyze, score, and tailor your resume for any job description. Whether you're optimizing for an ATS or impressing recruiters, this tool delivers powerful insights to elevate your resume.

---

## 🚀 Features

- ✅ **AI Skill Extraction** – Identifies essential skills from any job description using Gemini API.
- ✅ **Resume Scoring** – Instantly provides a match score based on skill alignment.
- ✅ **Keyword Analysis** – Displays Matched vs Missing skills side-by-side.
- ✅ **AI Summary Generator** – Crafts a tailored professional summary for the role.
- ✅ **Improvement Suggestions** – Offers action-based edits to boost resume impact.
- ✅ **File Support** – Upload `.pdf`, `.docx`, or `.txt` resumes and JDs.
- ✅ **Live App Interface** – Built with Streamlit for smooth, interactive use.

---

## 🧠 Tech Stack

| Layer        | Tools Used                                     |
|--------------|------------------------------------------------|
| Backend      | Python                                         |
| Frontend     | Streamlit                                      |
| AI / NLP     | Gemini API (`gemini-1.5-flash-latest`)         |
| File Parsing | `PyMuPDF` (PDF), `python-docx` (DOCX)          |
| Matching     | Regex via Python `re` module                   |
| Env Mgmt     | `python-dotenv` for secure API key loading     |

---

🖼️ Application Preview
---
🌐 Click here to view the live app

https://the-resume-refinery.onrender.com/
---

---

## 📂 Directory Structure

```

AI-Resume-Tailor/
│
├── app.py                   # Main Streamlit application
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (API keys)
├── utils.py                 # Helper functions (optional)
├── README.md                # Project documentation

````

---

## 🛠️ Getting Started

Follow these steps to run the app locally:

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Siddhunayak/AI-Resume-Tailor.git
cd AI-Resume-Tailor
````

---

### 2️⃣ Set Up Environment Variables

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY="your_gemini_api_key_here"
```

> 🔑 Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)

---

## 📦 Step 3: Install Dependencies

Run the following command to install all required packages:

```bash
pip install -r requirements.txt
```

---

🚀 Step 4: Run the Streamlit App
---
To run the app locally:
streamlit run app.py
---




## 📂 Supported File Formats

* `.pdf` — parsed using **PyMuPDF**
* `.docx` — parsed using **python-docx**
* `.txt` — read as plain text

---

## ✅ You're All Set!

Once the app is running, you can:

* Upload your resume and job description
* Get AI-extracted skills and a match score
* View matched and missing keywords
* Receive a tailored summary and suggestions

> ⚠️ **Note**: Always review AI-generated suggestions before final use.

---

## 🧪 Sample Prompt (Gemini API)

```python
# Extract skills from Job Description
"Act as a recruiter. Extract the key hard and soft skills from the following job description. Return as a comma-separated list:\n\n{job_description_text}"
```

```python
# Improve Resume
"Act as a resume coach. Based on the following resume and job description, provide suggestions to improve:\n\nResume:\n{resume_text}\n\nJD:\n{job_description_text}"
```


## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 👨‍💻 Author

Developed by [Siddhu Nayak](https://github.com/siddhunayak)
Inspired by the need for **AI-first job readiness tools**.

---

## 📈 Future Enhancements

* 🔍 Add OCR for image-based resumes
* 🌐 Support for multiple languages
* 🧠 More detailed skill categorization
* ☁️ Deploy to Hugging Face or Streamlit Cloud


