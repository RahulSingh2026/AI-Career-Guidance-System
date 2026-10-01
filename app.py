import streamlit as st
import pandas as pd
from model import train_model

model = train_model()

st.title("AI-Based Career Guidance and Recommendation System")

st.write("Find the career that best matches your skills and interests.")

st.header("Student Information")

name = st.text_input("Enter your name")

python = st.slider("Python Skill", 1, 10, 5)

communication = st.slider("Communication Skill", 1, 10, 5)

mathematics = st.slider("Mathematics Skill", 1, 10, 5)

problem_solving = st.slider("Problem Solving Skill", 1, 10, 5)

data_analysis = st.slider("Data Analysis Skill", 1, 10, 5)

web_development = st.slider("Web Development Skill", 1, 10, 5)

st.subheader("Your Interest")

interest = st.selectbox(
    "Select your main interest",
    [
        "Data Science",
        "Software Development",
        "Web Development",
        "Artificial Intelligence",
        "Cyber Security"
    ]
)

if st.button("Get Career Recommendation"):
    st.success("Your information has been submitted!")

    st.write("Name:", name)
    st.write("Interest:", interest)
    st.header("Career Recommendation")

if interest == "Data Science":
    career = "Data Scientist"

elif interest == "Software Development":
    career = "Software Developer"

elif interest == "Web Development":
    career = "Web Developer"

elif interest == "Artificial Intelligence":
    career = "AI/ML Engineer"

else:
    career = "Cyber Security Analyst"

st.subheader("🎯 Recommended Career")
st.write(career)
# Skill Based Match Score

st.header("Skill Based Career Analysis")

data_science_score = (
    python + mathematics + problem_solving + data_analysis
)

software_score = (
    python + problem_solving + communication
)

web_score = (
    web_development + python + communication
)

ai_score = (
    python + mathematics + problem_solving + data_analysis
)

cyber_score = (
    python + problem_solving + mathematics
)

# Calculate percentage
data_science_percentage = (data_science_score / 40) * 100
software_percentage = (software_score / 30) * 100
web_percentage = (web_score / 30) * 100
ai_percentage = (ai_score / 40) * 100
cyber_percentage = (cyber_score / 30) * 100

st.subheader("Career Match Scores")

st.write(
    f"📊 Data Scientist: {data_science_percentage:.1f}%"
)
st.progress(data_science_percentage / 100)

st.write(
    f"💻 Software Developer: {software_percentage:.1f}%"
)
st.progress(software_percentage / 100)

st.write(
    f"🌐 Web Developer: {web_percentage:.1f}%"
)
st.progress(web_percentage / 100)

st.write(
    f"🤖 AI/ML Engineer: {ai_percentage:.1f}%"
)
st.progress(ai_percentage / 100)

st.write(
    f"🔐 Cyber Security Analyst: {cyber_percentage:.1f}%"
)
st.progress(cyber_percentage / 100)
# Find the best career

career_scores = {
    "Data Scientist": data_science_percentage,
    "Software Developer": software_percentage,
    "Web Developer": web_percentage,
    "AI/ML Engineer": ai_percentage,
    "Cyber Security Analyst": cyber_percentage
}

best_career = max(career_scores, key=career_scores.get)
best_score = career_scores[best_career]

st.header("Final Recommendation")

st.success(
    f"🎯 Recommended Career: {best_career}"
)

st.info(
    f"Your Match Score: {best_score:.1f}%"
)
# AI/ML Career Prediction

st.header("🤖 AI/ML Career Prediction")

student_data = pd.DataFrame(
    [[
        python,
        mathematics,
        data_analysis,
        communication,
        web_development
    ]],
    columns=[
        "Python",
        "Mathematics",
        "Data_Analysis",
        "Communication",
        "Web_Development"
    ]
)

prediction = model.predict(student_data)

st.success(f"🤖 AI/ML Predicted Career: {prediction[0]}")

probabilities = model.predict_proba(student_data)

confidence = probabilities.max() * 100

st.info(f"AI Model Confidence: {confidence:.1f}%")

    # Skills to Learn

st.header("📚 Skills to Learn")

learning_skills = {
    "Data Scientist": [
        "Python",
        "Statistics",
        "SQL",
        "Pandas",
        "Machine Learning"
    ],

    "Software Developer": [
        "Programming",
        "Data Structures",
        "Algorithms",
        "Git",
        "Problem Solving"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Web Design"
    ],

    "AI/ML Engineer": [
        "Python",
        "Mathematics",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow / PyTorch"
    ],

    "Cyber Security Analyst": [
        "Computer Networking",
        "Linux",
        "Cyber Security Fundamentals",
        "Ethical Hacking",
        "Security Tools"
    ]
}
# Show skills for recommended career

predicted_career = prediction[0]

st.write("Based on your recommended career, you should focus on:")

for skill in learning_skills[predicted_career]:
    st.write("✅", skill)
    # Recommended Learning Path

st.header("🛣️ Recommended Learning Path")

learning_path = {
    "Data Scientist": [
        "Learn Python",
        "Learn Statistics",
        "Learn SQL",
        "Learn Pandas and NumPy",
        "Learn Machine Learning",
        "Build Data Science Projects"
    ],

    "Software Developer": [
        "Learn Programming",
        "Learn Data Structures",
        "Learn Algorithms",
        "Learn Git and GitHub",
        "Practice Problem Solving",
        "Build Software Projects"
    ],

    "Web Developer": [
        "Learn HTML",
        "Learn CSS",
        "Learn JavaScript",
        "Learn React",
        "Learn Web Development Tools",
        "Build Web Projects"
    ],

    "AI/ML Engineer": [
        "Learn Python",
        "Learn Mathematics",
        "Learn Machine Learning",
        "Learn Deep Learning",
        "Learn TensorFlow or PyTorch",
        "Build AI Projects"
    ],

    "Cyber Security Analyst": [
        "Learn Computer Networking",
        "Learn Linux",
        "Learn Cyber Security Fundamentals",
        "Learn Ethical Hacking",
        "Practice Security Tools",
        "Build Cyber Security Projects"
    ]
}

st.write("### Your Learning Roadmap")

for i, step in enumerate(learning_path[best_career], start=1):
    st.write(f"**Step {i}:** {step}")

if name:
    st.header(f"👋 Hello {name}!")
    st.write("Here is your personalized career guidance.")