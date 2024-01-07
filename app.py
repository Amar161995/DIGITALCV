from pathlib import Path

import streamlit as st

from PIL import Image

#-----paths----

current_dir = Path(__file__).parent if __file__ in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"Ahmed_Amar_Resume.pdf"
profile_pic = current_dir/"assets"/"profile-pic_.png"

#------General----
PAGE_TITLE = "DIGITAL CV | Ahmed AMAR"
PAGE_ICON = ":wave:"
NAME = "Ahmed AMAR"
DESCRIPTION = " I am an AI Engineer, I have an expertise of five years in computer vision and NLP"
EMAIL = "amarahmed1607@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn" :"https://www.linkedin.com/in/ahmed-amar-ba6b7815a/",
    "Github" : "https://github.com/Amar161995",
    "Twiter" : "https://x.com/amarahm58287990?s=21"
}

PROJECTS = {
    "🏆 Image classification": "Data wrangling, CNN model to classify(43 class) images of German traffic signs and performing this model by using techniques such as data augmentation",
    "🏆 Sentiment analysis": "Natural language processing, deep learning model to predict the sentiment(positive or negative) of food consumers",
    "🏆 Data Analysis": "Data preparation, Data exploration, Feature engineering and Machine Learning models to predict the price of diamonds based on some significant features"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


#----load css,pdf and profile pic ----

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

#---Hero section-----

col1, col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫",EMAIL)

#---- Social links ----
st.write("#")
cols=st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

    
# ---- experiences and qualifications -----
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔️ 5 years of experience in computer vision algorithms
    - ✔️ Strong hands on experience and knowledge in Python
    - ✔️ Good understanding of different AI models in computer vision
    - ✔️ Excellent team-player and displaying sense of initiative on tasks
    """
)

#----- SKILLS -----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 👩‍💻 Programming: Python, tensorflow, PyTorch
    - 📚 Modeling: Machine Learning
    - 🗄️ Databases: MySQL
    """
)

# ---- WORK HISTORY -----
st.write("#")
st.subheader("Work History")
st.write("----")
# --- JOB1
st.write("🚧", "**Data Scientist | Société Générale**")
st.write("01/2022 - Present")
st.write(
    """
I am in charge of data analysis, market data quality monitoring and applying machine learning algorithms to build predictive models and optimize processes based on data patterns.
"""
)
# --- JOB 2
st.write('\n')
st.write("🚧", "**Data Scientist Intern | Société Générale**")
st.write("04/2021 - 09/2021")
st.write(
    """
- ► I have worked as data scientist to build a robust model to predict the market volatilities.
- ► SVM and XGBoost
- ► Deep learning
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Data Analyst | National Agricultural Bank of Tunisia**")
st.write("02/2020 - 07/2020")
st.write(
    """
Data modeling, risk exchange rate prediction and  development of a Dashboard for risk assessment(VaR, CVaR...).
"""
)
# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")



