import streamlit as st
from PIL import Image

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
    }
    .profile-pic {
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load your profile picture and convert it to a round shape
def make_profile_pic_round(photo_6230778330290962227_y.jpg):
    img = Image.open(photo_6230778330290962227_y.jpg)
    width, height = img.size
    radius = min(width, height) // 2
    mask = Image.new('L', (radius * 2, radius * 2), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    img = img.resize((radius * 2, radius * 2))
    img.putalpha(mask)
    return img

# Contact Information with profile picture
with st.sidebar:
    st.image(make_profile_pic_round("photo_6230778330290962227_y.jpg"), class_="profile-pic")
    st.sidebar.write("Name: Kunal Jagdish Patil")
    st.sidebar.write("Contact No.: 9881679381")
    st.sidebar.write("Email ID: pkunal842@gmail.com")
# Set page title and background image
st.set_page_config(
    page_title="Kunal Jagdish Patil's Portfolio",
    page_icon=":chart_with_upwards_trend:",
)


# Contact Information
st.sidebar.header("Contact")
st.sidebar.write("Name: Kunal Jagdish Patil")
st.sidebar.write("Contact No.: 9881679381")
st.sidebar.write("Email ID: pkunal842@gmail.com")

# Hero Section
st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.title("Welcome to My Portfolio")
st.write("Data Scientist | Machine Learning Enthusiast")
st.markdown("</div>", unsafe_allow_html=True)

# Career Summary
st.markdown("<hr/>", unsafe_allow_html=True)
st.header("Career Summary")
st.write(
    "Seeking a role in data science/analysis to leverage statistical and machine learning skills for impactful business decisions. Eager to contribute expertise in fostering organizational growth, paired with strong communication, teamwork, and leadership abilities."
)

# Skills Section with Icons
st.header("Skills")
skills = [
    {"icon": ":computer:", "name": "Programming Languages: Python, SQL"},
    {"icon": ":abacus:", "name": "Machine Learning: Supervised/Unsupervised"},
    {"icon": ":chart_with_upwards_trend:", "name": "Data Visualization: Seaborn, Matplotlib"},
    {"icon": ":speaking_head:", "name": "Communication & Teamwork"},
]
cols = st.columns(len(skills))
for i, col in enumerate(cols):
    col.markdown(f"{skills[i]['icon']} {skills[i]['name']}")

# Professional Experience
st.header("Professional Experience")
st.write("AI ML Intern")
st.write("Webmobi360.co | Pune | Dec.2023-Present")
st.markdown(
    "**LOGISTICS VIDEO ANALYTICS PRODUCT FOR FACILITY MANAGEMENT** \n"
    "- Innovated comprehensive video analytics: object tracking, anomaly detection, predictive models, vehicle/asset management, facial recognition, and occupancy monitoring. \n"
    "- Designed customizable dashboards and real-time alerts for proactive decision-making, optimizing facility operations through advanced tech solutions."
)

# Academic Projects
st.header("Academic Projects")
projects = [
    "Medicine Recommendation System using Machine Learning",
    "Online Shopping Process Analytics",
    "Credit Card Defaulter Prediction using Machine Learning (Classification)",
]
for project in projects:
    st.write(f"- {project}")

# Education
st.header("Education")
st.write("Course | Institution | Year")
st.write("---|---|---")
degrees = [
    ("Post Graduate Programme – Data Science and Engineering", "Great Lakes Institute of Management", "2023"),
    ("Bachelor Of Engineering (Mechanical Engg.)", "Sandip Institute of Engineering and Management, Nashik", "2019"),
    ("Diploma in Mechanical Engg.", "S.S.V.P.S’s college of engineering and Polytechnique, Dhule", "2016"),
    ("10th Std", "Sane Guruji Vidya Mandir, Amalner", "2013"),
]
for deg in degrees:
    st.write(f"- {deg[0]} | {deg[1]} | {deg[2]}")

# Other Achievements
st.header("Other Certificates/Achievements")
achievements = [
    "Introduction to R",
    "Fundamentals of Generative AI",
    "Basics of Power BI",
]
for ach in achievements:
    st.write(f"- {ach}")

# Call to Action
st.write("Let's connect!")
st.write("Connect with me on LinkedIn: https://www.linkedin.com/in/kunal-patil-35475a167/")
