import streamlit as st
import os
import base64
import subprocess
import sys
import json
import google.generativeai as genai

# --- FORCED SPACY INSTALLATION ---
try:
    import en_core_web_sm
except ImportError:
    subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
# ---------------------------------

# --- NEW DIRECT IMPORTS (No 'engine.' prefix) ---
from extractor import extract_text_from_pdf
from processor import ResumeProcessor
from matcher import ResumeMatcher
from improver import ResumeImprover 

# --- GEMINI API CONFIGURATION ---
# This pulls the key from the 'Secrets' you add in Space Settings
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Resume Analyzer", page_icon="🎯", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Inter:wght@400;600&display=swap');
/* BACKGROUND */
html, body, [data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #020c11 0%, #051923 50%, #003554 100%) !important;
}
/* REMOVE HEADER */
[data-testid="stHeader"] { display: none; }
/* HEADER */
.brand-section {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
}
.main-logo-img {
    height: 65px;
    filter: drop-shadow(0px 0px 10px #00fff2);
}
.main-title {
    font-family: 'Orbitron';
    font-size: 36px;
    color: #00fff2;
}
/* CENTER WRAPPER */
.center-wrapper {
    display: flex;
    justify-content: center;
}
/* MATRIX */
.matrix {
    width: 100%;
    max-width: 1100px;
}
/* LABEL */
.label {
    font-family: 'Orbitron';
    font-size: 13px;
    color: #00fff2;
    margin-bottom: 6px;
}
/* INPUT HEIGHTS */
[data-testid="stFileUploader"] section,
.stTextArea textarea {
    height: 250px !important;
    min-height: 250px !important;
}
/* UPLOADER STYLING */
[data-testid="stFileUploader"] label { display:none; }
[data-testid="stFileUploader"] section {
    border: 2px dashed #00fff2;
    border-radius: 12px;
    background: rgba(0,255,242,0.05);
}
/* TEXT AREA STYLING */
.stTextArea textarea {
    border-radius: 12px !important;
    border: 2px solid rgba(0,255,242,0.3) !important;
    background: rgba(255,255,255,0.03) !important;
    color: white !important;
    padding: 15px !important;
    font-family: 'Inter';
}
/* BUTTON */
div.stButton > button {
    height: 55px;
    width: 100%;
    font-size: 16px;
    font-family: 'Orbitron';
    background: linear-gradient(90deg, #00fff2, #0077b6) !important;
    color: #020c11 !important;
    border-radius: 10px !important;
    border:none !important;
    font-weight: bold;
    cursor: pointer;
}
/* RESULT CARDS */
.result-box {
    margin-top: 10px;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid rgba(0,255,242,0.3);
    background: rgba(0,255,242,0.05);
    color: white;
    font-family: 'Inter';
}
</style>
""", unsafe_allow_html=True)

# ---------------- ENGINE LOAD ----------------
@st.cache_resource
def load_all_engines():
    # These classes are now imported from the root files
    return ResumeProcessor(), ResumeMatcher(), ResumeImprover()

processor, matcher, improver = load_all_engines()

# ---------------- BRANDING / LOGO ----------------
def get_b64(file):
    try:
        with open(file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo_b64 = get_b64("logo.png")
if logo_b64:
    st.markdown(f"""
    <div class="brand-section">
        <img src="data:image/png;base64,{logo_b64}" class="main-logo-img">
        <div class="main-title">RESUME ANALYZER</div>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<h1 style='color:#00fff2; font-family:Orbitron;'>🎯 RESUME ANALYZER</h1>", unsafe_allow_html=True)

# ---------------- UI WORKSPACE ----------------
st.markdown('<div class="center-wrapper"><div class="matrix">', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="label">SOURCE: RESUME</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload PDF", type=["pdf"], key="pdf_uploader", label_visibility="collapsed")

with col2:
    st.markdown('<div class="label">TARGET: SPECS</div>', unsafe_allow_html=True)
    jd_text = st.text_area("Job Description", placeholder="Paste job requirements here...", key="jd_area", label_visibility="collapsed")

st.markdown('<div class="btn-container">', unsafe_allow_html=True)
scan_trigger = st.button("🚀 INITIATE QUANTUM SCAN", use_container_width=True)
st.markdown('</div></div></div>', unsafe_allow_html=True)

# ---------------- SCAN LOGIC ----------------
if scan_trigger:
    if uploaded_file and jd_text.strip():
        if not api_key:
            st.warning("⚠️ API Key not found. Please add GEMINI_API_KEY to Space Secrets.")
            st.stop()

        with st.spinner("Extracting PDF Data..."):
            tmp_path = "temp_scan.pdf"
            with open(tmp_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            final_resume_text = extract_text_from_pdf(tmp_path)
            os.remove(tmp_path)
            
        with st.spinner("Quantum Matching in Progress..."):
            resume_skills = processor.extract_skills(final_resume_text)
            job_skills = processor.extract_skills(jd_text)

            score, missing_skills, matched_skills = matcher.calculate_match(
                resume_skills, job_skills
            )

            # 1. DISPLAY SCORE
            st.markdown(f"""
            <div style='margin-top:30px; padding:20px; text-align:center; border:2px solid #00fff2; 
                 border-radius:12px; color:#00fff2; font-family:Orbitron; font-size:26px; background:rgba(0,255,242,0.1);'>
            MATCH SCORE: {score}%
            </div>
            """, unsafe_allow_html=True)

            # 2. SKILL COLUMNS
            res_col1, res_col2 = st.columns(2)

            with res_col1:
                st.markdown("<h3 style='color:#00fff2; font-family:Orbitron; font-size:18px; margin-top:20px;'>✅ Matched Skills</h3>", unsafe_allow_html=True)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                if matched_skills:
                    for s in matched_skills: st.write(f"• {s}")
                else:
                    st.write("No overlaps detected.")
                st.markdown('</div>', unsafe_allow_html=True)

            with res_col2:
                st.markdown("<h3 style='color:#ff4b4b; font-family:Orbitron; font-size:18px; margin-top:20px;'>❌ Missing Skills</h3>", unsafe_allow_html=True)
                st.markdown('<div class="result-box">', unsafe_allow_html=True)
                if missing_skills:
                    for s in missing_skills: st.write(f"• {s}")
                else:
                    st.write("Resume covers all specs! 🎯")
                st.markdown('</div>', unsafe_allow_html=True)

            # 3. AI IMPROVEMENTS
            st.markdown("<h3 style='color:#00fff2; font-family:Orbitron; font-size:18px; margin-top:30px;'>💡 AI Resume Enhancements</h3>", unsafe_allow_html=True)
            st.markdown('<div class="result-box">', unsafe_allow_html=True)

            if missing_skills:
                with st.spinner("🤖 Gemini is architecting your improvements..."):
                    suggestions = improver.generate_bullets(missing_skills, jd_text)
                    st.markdown(suggestions)
                    
                    st.markdown("<br>", unsafe_allow_html=True)
                    
                    st.download_button(
                        label="📥 Download AI Enhancements",
                        data=suggestions,
                        file_name="Quantum_Resume_Enhancements.txt",
                        mime="text/plain",
                        use_container_width=True
                    )
            else:
                st.success("Your profile is already optimized for this position. 🚀")
            st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.error("SYSTEM ERROR: Missing Source Resume or Target Specs.")
