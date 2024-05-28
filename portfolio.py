import streamlit as st

# Set page title
st.title("Kunal Jagdish Patil's Portfolio")

# Set page width
st.markdown(
    """
    <style>
    .reportview-container {
        padding-top: 2rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a background color and padding to the contact information section
st.markdown(
    """
    <style>
    .contact-info {
        background-color: #f0f0f0;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display contact information
st.markdown("<div class='contact-info'>", unsafe_allow_html=True)
st.write("**Name:** Kunal Jagdish Patil")
st.write("**Contact No.:** 9881679381")
st.write("**Email ID:** pkunal842@gmail.com")
st.markdown("</div>", unsafe_allow_html=True)

# Add a background color and padding to the other sections
st.markdown(
    """
    <style>
    .section {
        background-color: #f9f9f9;
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display career summary
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("**CAREER SUMMARY**")
st.write("Seeking a role in data science/analysis to leverage statistical and machine learning skills for impactful business decisions. Eager to contribute expertise in fostering organizational growth, paired with strong communication, teamwork, and leadership abilities")
st.markdown("</div>", unsafe_allow_html=True)

# Display skills
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("**KEY SKILLS**")
st.write("• Skills: Exploratory Data Analysis, MS-EXCEL, MS-PowerPoint, Machine Learning, Data Query, Data Manipulation and Data Visualization.")
st.write("• Coding Languages: Python, SQL")
st.write("• Machine Learning: Supervised and Unsupervised Machine Learning, Regression, Classification, Clustering.")
# Add more skills as needed
st.markdown("</div>", unsafe_allow_html=True)

# Display professional experience
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("**PROFESSIONAL EXPERIENCE**")
st.write("AI ML Intern :")
st.write("Webmobi360.co | Pune | Dec.2023-Present")
st.write("LOGISTICS VIDEO ANALYTICS PRODUCT FOR FACILITY MANAGEMENT - Innovated comprehensive video analytics: object tracking, anomaly detection, predictive models, vehicle/asset management, facial recognition, and occupancy monitoring. Designed customizable dashboards, and real-time alerts for proactive decision-making, optimizing facility operations through advanced tech solutions.")
st.markdown("</div>", unsafe_allow_html=True)

# Display academic projects
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("**ACADEMIC – DATA SCIENCE PROJECTS**")
st.write("• Medicine Recommendation System using Machine Learning")
st.write("• Online Shopping Process Analytics")
st.write("• Credit Card Defaulter Prediction using Machine Learning – Classification")
st.markdown("</div>", unsafe_allow_html=True)

# Display education
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("**EDUCATION**")
st.write("Course Institution Year")
st.write("Post Graduate Programme – Data Science and Engineering Great Lakes Institute of Management 2023")
st.write("Bachelor Of Engineering (Mechanical Engg.) Sandip Institute of Engineering and Management, Nashik 2019")
st.write("Diploma in Mechanical Engg. S.S.V.P.S’s college of engineering and Polytechnique, Dhule 2016")
st.write("10th Std Sane Guruji Vidya Mandir, Amalner 2013")
st.markdown("</div>", unsafe_allow_html=True)

# Display other certificates/achievements
st.markdown("<div class='section'>", unsafe_allow_html=True)
st.write("**OTHER CERTIFICATES/ACHIEVEMENTS**")
st.write("• Introduction to R")
st.write("• Fundamentals of Generative AI")
st.write("• Basics of Power BI")
st.markdown("</div>", unsafe_allow_html=True)
