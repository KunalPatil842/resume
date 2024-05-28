import streamlit as st

# Set page title
st.title("Kunal Jagdish Patil's Portfolio")

# Display contact information
st.write("Name: Kunal Jagdish Patil")
st.write("Contact No.: 9881679381")
st.write("Email ID: pkunal842@gmail.com")

# Display career summary
st.write("CAREER SUMMARY")
st.write("Seeking a role in data science/analysis to leverage statistical and machine learning skills for impactful business decisions. Eager to contribute expertise in fostering organizational growth, paired with strong communication, teamwork, and leadership abilities")

# Display skills
st.write("KEY SKILLS")
st.write("• Skills: Exploratory Data Analysis, MS-EXCEL, MS-PowerPoint, Machine Learning, Data Query, Data Manipulation and Data Visualization.")
st.write("• Coding Languages: Python, SQL")
st.write("• Machine Learning: Supervised and Unsupervised Machine Learning, Regression, Classification, Clustering.")
st.write("• Machine Learning Algorithms: Linear Regression, Logistic Regression, K-Nearest Neighbours, Gaussian Naïve Bayes, Decision Tree, Random Forest, K-Means Clustering, Agglomerative Hierarchical Clustering.")
st.write("• Statistical Methods: Hypothesis Testing, Z-test, T-test, Chi-square test, and ANOVA test.")
st.write("• Data Visualization: Seaborn, Matplotlib, Google Data Studio(Looker), Power BI.")
st.write("• Python: Seaborn, Matplotlib, NumPy, Pandas, Plotly, Scipy, Scikit-Learn, Statsmodels.")
st.write("• Microsoft Office: MS Word, MS Excel, MS PowerPoint")
st.write("• Generative AI: LLM, OpenAI, Gemini-pro, etc.")
st.write("• Soft Skills: Communication Skills, Time management, Team Player, Problem Solving Skills, Decision making, Writing")

# Display professional experience
st.write("PROFESSIONAL EXPERIENCE")
st.write("AI ML Intern :")
st.write("Webmobi360.co | Pune | Dec.2023-Present")
st.write("LOGISTICS VIDEO ANALYTICS PRODUCT FOR FACILITY MANAGEMENT - Innovated comprehensive video analytics: object tracking, anomaly detection, predictive models, vehicle/asset management, facial recognition, and occupancy monitoring. Designed customizable dashboards, and real-time alerts for proactive decision-making, optimizing facility operations through advanced tech solutions.")

# Display academic projects
st.write("ACADEMIC – DATA SCIENCE PROJECTS")
st.write("• Medicine Recommendation System using Machine Learning")
st.write("• Online Shopping Process Analytics")
st.write("• Credit Card Defaulter Prediction using Machine Learning – Classification")

# Display education
st.write("EDUCATION")
st.write("Course Institution Year")
st.write("Post Graduate Programme – Data Science and Engineering Great Lakes Institute of Management 2023")
st.write("Bachelor Of Engineering (Mechanical Engg.) Sandip Institute of Engineering and Management, Nashik 2019")
st.write("Diploma in Mechanical Engg. S.S.V.P.S’s college of engineering and Polytechnique, Dhule 2016")
st.write("10th Std Sane Guruji Vidya Mandir, Amalner 2013")

# Display other certificates/achievements
st.write("OTHER CERTIFICATES/ACHIEVEMENTS")
st.write("• Introduction to R")
st.write("• Fundamentals of Generative AI")
st.write("• Basics of Power BI")

# Add CSS for styling
st.markdown(
    """
    <style>
    .projects {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0px 2px 10px rgba(0, 0, 0, 0.1);
    }
    .projects h3 {
        color: #333333;
        margin-bottom: 1rem;
    }
    .project {
        margin-bottom: 1.5rem;
    }
    .project img {
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease-out;
    }
    .project img:hover {
        transform: scale(1.05);
    }
    .project-desc {
        color: #666666;
        margin-top: 0.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='projects'>", unsafe_allow_html=True)
st.markdown("<h3>Recent Projects</h3>", unsafe_allow_html=True)

# Add images and descriptions for projects
st.markdown("<div class='project'>", unsafe_allow_html=True)
st.image("project1.jpg", width=200)
st.markdown("<p class='project-desc'>Project One - Data Analysis</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# Add more projects
st.markdown("</div>", unsafe_allow_html=True)
