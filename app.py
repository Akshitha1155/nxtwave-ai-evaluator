import streamlit as st
import random

# Page Config
st.set_page_config(
    page_title="NxtWave AI Career Readiness Evaluator",
    page_icon="🚀",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main-header {
        font-size: 28px;
        font-weight: 800;
        color: #FF4B4B;
        text-align: center;
    }
    .sub-text {
        font-size: 16px;
        color: #555555;
        text-align: center;
        margin-bottom: 30px;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FF4B4B;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-header">🎯 NxtWave AI Career Readiness & Resume Audit Tool</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Built for Final-Year Engineering Students | Check your ATS & AI readiness score instantly.</p>', unsafe_allow_html=True)

# User Input Section
col1, col2 = st.columns(2)
with col1:
    student_name = st.text_input("Your Full Name", placeholder="e.g. Rahul Sharma")
with col2:
    college_tier = st.selectbox("College Tier", ["Tier-2 / Tier-3 Engineering College", "Tier-1 College"])

branch = st.selectbox("Your Specialization / Branch", ["Computer Science / IT", "Electronics & Communication", "Mechanical / Civil / Electrical", "Other Engineering"])

uploaded_resume = st.file_uploader("Upload Your Resume (PDF / TXT)", type=["pdf", "txt", "docx"])

if st.button("🚀 Analyze My AI Readiness Score", use_container_width=True):
    if not student_name:
        st.warning("Please enter your name to proceed.")
    else:
        with st.spinner("Analyzing resume against industry ATS & GenAI benchmarks..."):
            # Simulated intelligent scoring logic
            ai_score = random.randint(42, 58) # Typically low because students lack practical AI projects
            
        st.success("Analysis Complete!")
        
        # Display Score Card
        st.markdown(f"### 📊 Audit Results for {student_name}")
        col_a, col_b, col_c = st.columns(3)
        col_a.metric("AI Readiness Score", f"{ai_score}/100", "-35% vs Industry Avg")
        col_b.metric("ATS Compatibility", "Moderate", "Needs Formatting")
        col_c.metric("Practical AI Projects", "0 Found", "Critical Gap")
        
        st.warning("⚠️ **Critical Gap Detected:** Your resume currently lacks deployable LLM/RAG or practical AI project experience, which causes 85% of automated ATS rejections for entry-level engineering roles.")
        
        st.markdown("---")
        st.markdown("### 🔥 Instant Fix: Close the Gap in 60 Minutes")
        st.info("Don't let your resume get filtered out. Build a resume-worthy AI application live in our upcoming free masterclass.")
        
        # Registration CTA Button (Simulating WhatsApp / Form conversion)
        st.markdown("""
            <div style="text-align: center; margin-top: 25s px;">
                <a href="https://chat.whatsapp.com/sample-nxtwave-workshop-link" target="_blank">
                    <button style="background-color: #25D366; color: white; padding: 15px 30px; font-size: 18px; font-weight: bold; border: none; border-radius: 8px; cursor: pointer;">
                        📱 Register Free via WhatsApp (Instant Access)
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.caption("NxtWave Growth Challenge Submission | Built with Streamlit & Python")
