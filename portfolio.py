import streamlit as st

# Set page title and background image
st.set_page_config(
    page_title="Kunal Jagdish Patil's Portfolio",
    page_icon=":chart_with_upwards_trend:",
)
st.markdown(
    """
    <style>
    body {
        background-image: url("background.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #ffffff;  /* Set text color to white */
    }
    .hero {
        padding: 2rem 0;
        text-align: center;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .hero-subtitle {
        font-size: 1.2rem;
    }
    .section {
        padding: 2rem 0;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
    }
    .contact-info {
        margin-bottom: 1rem;
    }
    .skill-icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
    }
    .project-item {
        margin-left: 2rem;
    }
    .education-item {
        margin-left: 1rem;
    }
    .achievement-item {
        margin-left: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Contact Information
st.sidebar.header("Contact")
st.sidebar.write("Name: Kunal Jagdish Patil")
st.sidebar.write("Contact No.: 9881679381")
st.sidebar.write("Email ID: pkunal842@gmail.com")

# Hero Section
st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.markdown("<div class='hero-title'>Welcome to My Portfolio</div>", unsafe_allow_html=True)
st.markdown("<div class='hero-subtitle'>Data Scientist | Machine Learning Enthusiast</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Career Summary
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Career Summary</div>", unsafe_allow_html=True)
st.write(
    "Seeking a role in data science/analysis to leverage statistical and machine learning skills for impactful business decisions. Eager to contribute expertise in fostering organizational growth, paired with strong communication, teamwork, and leadership abilities."
)

# Skills Section with Icons
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Skills</div>", unsafe_allow_html=True)
skills = [
    {"icon": "💻", "name": "Programming Languages: Python, SQL"},
    {"icon": "🧮", "name": "Machine Learning: Supervised/Unsupervised"},
    {"icon": "📈", "name": "Data Visualization: Seaborn, Matplotlib"},
    {"icon": "🗣️", "name": "Communication & Teamwork"},
]
for skill in skills:
    st.write(f"<span class='skill-icon'>{skill['icon']}</span> {skill['name']}", unsafe_allow_html=True)

# Professional Experience
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Professional Experience</div>", unsafe_allow_html=True)
st.write("AI ML Intern")
st.write("Webmobi360.co | Pune | Dec.2023-Present")
st.markdown(
    "**LOGISTICS VIDEO ANALYTICS PRODUCT FOR FACILITY MANAGEMENT** \n"
    "- Innovated comprehensive video analytics: object tracking, anomaly detection, predictive models, vehicle/asset management, facial recognition, and occupancy monitoring. \n"
    "- Designed customizable dashboards and real-time alerts for proactive decision-making, optimizing facility operations through advanced tech solutions."
)

# Academic Projects
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Academic Projects</div>", unsafe_allow_html=True)
projects = [
    {"title": "Medicine Recommendation System using Machine Learning", "description": "Developed a machine learning model to recommend medicines based on patient symptoms and medical history."},
    {"title": "Online Shopping Process Analytics", "description": "Analyzed user behavior data to optimize the online shopping process and improve user experience."},
    {"title": "Credit Card Defaulter Prediction using Machine Learning (Classification)", "description": "Built a classification model to predict credit card defaulters based on historical transaction data."},
]
for project in projects:
    st.write(f"<div class='project-item'><strong>{project['title']}</strong>: {project['description']}</div>", unsafe_allow_html=True)

# Education
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Education</div>", unsafe_allow_html=True)
degrees = [
    ("Post Graduate Programme – Data Science and Engineering", "Great Lakes Institute of Management", "2023"),
    ("Bachelor Of Engineering (Mechanical Engg.)", "Sandip Institute of Engineering and Management, Nashik", "2019"),
    ("Diploma in Mechanical Engg.", "S.S.V.P.S’s college of engineering and Polytechnique, Dhule", "2016"),
    ("10th Std", "Sane Guruji Vidya Mandir, Amalner", "2013"),
]
for deg in degrees:
    st.write(f"<div class='education-item'>- {deg[0]} | {deg[1]} | {deg[2]}</div>", unsafe_allow_html=True)

# Other Achievements
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.markdown("<div class='section-header'>Other Certificates/Achievements</div>", unsafe_allow_html=True)
achievements = [
    "Introduction to R",
    "Fundamentals of Generative AI",
    "Basics of Power BI",
]
for ach in achievements:
    st.write(f"<div class='achievement-item'>- {ach}</div>", unsafe_allow_html=True)

# Call to Action
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("Let's connect!")
st.write("Connect with me on LinkedIn: [Kunal Patil](https://https://www.linkedin.com/in/kunal-patil-35475a167/)")
