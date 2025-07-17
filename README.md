🧠 AI Resume Tailor ✨
An intelligent Streamlit application powered by Google Gemini to analyze, score, and tailor your resume for any job description. This tool helps you optimize your resume to pass applicant tracking systems (ATS) and catch the eye of recruiters.

🚀 Core Features
AI Skill Extraction: Automatically identifies the most important skills and keywords from a job description using the Gemini API.

Resume Scoring: Provides an instant match score based on how well your resume's content aligns with the job's key requirements.

Keyword Analysis: Delivers a clear, side-by-side comparison of "Matched Skills" and "Missing Skills" to guide your edits.

AI-Generated Summary: Creates a tailored, professional summary that highlights your most relevant strengths for the specific role.

Actionable Improvements: Offers specific, AI-powered suggestions on how to re-frame your experience, quantify your achievements, and improve your resume's overall impact.

🛠️ Tech Stack
This project is built with a modern Python stack, leveraging powerful tools for AI, web development, and file processing.

Backend: Python

Frontend: Streamlit

AI & NLP: Google Gemini API (gemini-1.5-flash-latest)

File Parsing: PyMuPDF (for PDFs), python-docx (for Word documents)

Text Matching: Python's re module (Regular Expressions)

Environment: python-dotenv

⚙️ How It Works
The application follows a sophisticated workflow to provide a comprehensive analysis:

Text Extraction: The app first parses the uploaded resume and job description files (.pdf, .docx, .txt) into plain text.

AI Skill Analysis: It sends the job description text to the Gemini API, prompting it to act like an expert recruiter and extract a clean list of the most critical skills.

Local Matching & Scoring: Using regular expressions, the script performs a robust local comparison between the extracted skills and the resume text to calculate a match score and identify gaps.

AI Content Generation: Finally, it sends both the resume and job description text to the Gemini API with two distinct prompts: one to generate a tailored summary and another to provide actionable improvement tips.

Display: All results are then rendered in a clean, interactive dashboard using Streamlit.

🏁 Quick Start
To get this project running on your local machine, follow these steps:

1. Clone the repository
Bash

git clone https://github.com/your-username/AI-Resume-Tailor.git
cd AI-Resume-Tailor
2. Set up your environment
Create a file named .env in the root directory. Add your Google Gemini API key to this file:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
3. Install dependencies
Bash

pip install -r requirements.txt
4. Run the Streamlit app
Bash

streamlit run app.py
Open your browser and navigate to the local URL provided by Streamlit.

📜 License
Distributed under the MIT License. See LICENSE for more information.
