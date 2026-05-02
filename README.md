# 🎯 Quantum Resume Analyzer 

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Gemini AI](https://img.shields.io/badge/AI-Gemini_3_Flash-00FFF2?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-spaCy-09A3D5?style=for-the-badge)

An elite, high-performance Applicant Tracking System (ATS) simulator and AI resume enhancer. Built to bridge the gap between job descriptions and candidate profiles using advanced Natural Language Processing and Generative AI.

**🔥 [CLICK HERE FOR THE LIVE APP DEMO](https://huggingface.co/spaces/shwetaaank/RESUME-ANALYZER)**

---

## 📸 System Interface


**1. Command Interface**<img width="1878" height="801" alt="pv1" src="https://github.com/user-attachments/assets/42c47fe7-eaa6-40ec-b3bf-6876829b1886" />
![Uploading pv2.png…]()
<img width="1878" height="801" alt="pv1" src="https://github.com/user-attachments/assets/eadd5ce4-31c3-4ee0-9c38-34e591e4d1b0" />

`[Drop your scan-results.png screenshot here]`

**3. Gemini AI Enhancements and Matching Results**
<img width="1878" height="801" alt="pv1" src="https://github.com/user-attachments/assets/eadd5ce4-31c3-4ee0-9c38-34e591e4d1b0" />


---

## 🚀 Core Architecture & Features

This tool goes beyond basic keyword matching by utilizing fuzzy logic and state-of-the-art LLMs to provide actionable career intelligence.

* **PDF Data Extraction:** Robust text parsing using `pdfplumber` to bypass complex resume formatting.
* **NLP Skill Processing:** Utilizes `spaCy` (en_core_web_sm) and `thefuzz` for intelligent, context-aware skill identification and fuzzy matching (handling misspellings and variations).
* **Quantum Matching Engine:** Calculates a precise ATS compatibility score by cross-referencing extracted candidate skills against targeted job requirements.
* **Generative AI Enhancements:** Integrates Google's **Gemini 3 Flash** API to dynamically generate powerful, action-oriented resume bullet points that organically incorporate missing skills.
* **Cyberpunk / Sci-Fi UI:** Custom-built Streamlit interface featuring the Orbitron font family, dynamic gradients, and a highly responsive dark-mode layout.

---

## 🛠️ Technical Stack

* **Frontend:** Streamlit, Custom CSS
* **Backend:** Python 3.11
* **Machine Learning / NLP:** spaCy, TheFuzz, python-Levenshtein
* **Generative AI:** Google Generative AI SDK (Gemini API), Requests
* **Data Handling:** Pandas, JSON
* **Deployment:** Docker, Hugging Face Spaces

---

## 💻 Local Installation

To run the Quantum Resume Analyzer on your local machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shwetaaank/RESUME-ANALYZER.git](https://github.com/shwetaaank/RESUME-ANALYZER.git)
   cd RESUME-ANALYZER
