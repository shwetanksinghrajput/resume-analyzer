# 🎯 Quantum Resume Analyzer 

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
![Gemini AI](https://img.shields.io/badge/AI-Gemini_3_Flash-00FFF2?style=for-the-badge)
![NLP](https://img.shields.io/badge/NLP-spaCy-09A3D5?style=for-the-badge)
![Hugging Face](https://img.shields.io/badge/Deployed_on-Hugging_Face-F9AB00?style=for-the-badge&logo=huggingface)

An elite, high-performance Applicant Tracking System (ATS) simulator and AI resume enhancer. Built to bridge the gap between job descriptions and candidate profiles using advanced Natural Language Processing and Generative AI. 

**🔥 [CLICK HERE FOR THE LIVE APP DEMO ON HUGGING FACE](https://huggingface.co/spaces/shwetaaank/RESUME-ANALYZER)**

---

## 📸 System Interface

*(Note: Drag and drop your screenshots here to replace these placeholder lines!)*

**1. The Command Center**
<img width="1878" height="801" alt="pv1" src="https://github.com/user-attachments/assets/e5f8c980-8250-4cc7-ad0f-64509fa3b8fc" />




**2. Gemini AI Enhancements and Match Results**
<img width="1822" height="870" alt="pv2" src="https://github.com/user-attachments/assets/70fc2fa5-f22a-4d7d-8709-3068f0dee26e" />

`[Drop your ai-enhancements.png screenshot here]`

---

## 🚀 Core Architecture & Features

This tool goes beyond basic keyword matching. It mimics the strict filters of enterprise ATS software, but pairs it with an AI mentor to help candidates instantly improve their odds.

* **Smart PDF Data Extraction:** Utilizes `pdfplumber` for robust text parsing, designed to bypass complex resume formatting, hidden tables, and multi-column layouts.
* **NLP Skill Processing:** Powered by `spaCy` (en_core_web_sm) for intelligent, context-aware skill identification.
* **Fuzzy Logic Matching:** Implements `thefuzz` and `python-Levenshtein` to account for human error, misspellings, and variations in skill naming conventions (e.g., matching "React.js" with "ReactJS").
* **Quantum Matching Engine:** Calculates a mathematically precise ATS compatibility score by cross-referencing extracted candidate skills against targeted job requirements.
* **Generative AI Enhancements:** Integrates Google's state-of-the-art **Gemini 3 Flash** API. When the system detects missing skills, the LLM dynamically generates powerful, action-oriented resume bullet points that organically incorporate those missing keywords.
* **Cyberpunk / Sci-Fi UI:** Custom-built Streamlit interface featuring the Orbitron font family, dynamic background gradients, and a highly responsive dark-mode matrix layout.

---

## 🛡️ Enterprise Security & Stability

Built with production-grade safeguards to ensure cloud stability and protect API quotas.

* **Session-Based Rate Limiting:** Engineered a custom `st.session_state` cooldown protocol to prevent API spam and quota exhaustion. This allows multiple recruiters to test the application simultaneously without triggering global rate limits.
* **Direct Binary Injection (Cloud Bypass):** Successfully engineered a bypass for standard Hugging Face Docker caching bugs by hardcoding the direct `.tar.gz` binary release of the spaCy English model into the dependency tree. This ensures a 100% crash-free build rate during automated cloud deployments.

## ☁️ Cloud Deployment via Hugging Face

This application is fully containerized and hosted in the cloud to ensure high availability and fast processing.

* **Platform:** Deployed live on **Hugging Face Spaces**.
* **Containerization:** Runs in an isolated **Docker** environment, ensuring perfect dependency management and avoiding local environment clashes.
* **Reverse Proxy Bypass:** Configured with custom Streamlit server flags (`--server.enableCORS=false`) to seamlessly handle file uploads through Hugging Face's strict security protocols.
* **Secret Management:** API keys and environment variables are securely managed via Hugging Face Secrets (`os.getenv`).

---

## 🛠️ Technical Stack

* **Frontend:** Streamlit, Custom CSS/HTML injections
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

Developed By: Shwetank Singh Rajput
