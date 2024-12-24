import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Mental Health Support Platform",
    page_icon="🧠",
    layout="wide",
)

# Header Section
st.markdown(
    """
    <style>
    .header-title {
        font-size: 2.5em;
        color: #ffeddb;
        font-weight: bold;
        text-align: center;
    }
    .subheader-title {
        font-size: 1.5em;
        color: #dbffdb;
        text-align: center;
    }
    .info-text {
        font-size: 1.2em;
        color: #dbf6ff;
        text-align: center;
        margin-bottom: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h2 class="header-title">Welcome to the Mental Health Support Platform</h2>', unsafe_allow_html=True)
st.markdown('<h4 class="subheader-title">Empowering you to take control of your mental health 🌟</h4>', unsafe_allow_html=True)
st.markdown(
    '<p class="info-text">Mental health is essential to overall well-being. Our platform provides personalized tools to help you manage your emotions and thoughts effectively. Explore our features designed to offer support, guidance, and valuable resources in your mental health journey.</p>',
    unsafe_allow_html=True,
)

st.write("## 🌟 Platform Features")
st.markdown(
    """
    <style>
    .feature-box {
        background-color: #FFFFFF;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
        margin-bottom: 20px;
        height: auto;
        min-height: 350px; /* Ensure all boxes have consistent minimum height */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .feature-box:hover {
        transform: translateY(-10px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
    }
    .feature-title {
        font-size: 1.5em;
        color: ; #444444;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .feature-description {
        font-size: 1em;
        color: #444444; /* Use a darker shade for descriptions */
        margin-bottom: 20px;
    }
    .feature-icon {
        font-size: 2.5em;
        margin-bottom: 15px;
        color: #4CAF50;
    }
    .btn-learn {
        padding: 10px 20px;
        border-radius: 25px;
        border: none;
        color: white;
        background: linear-gradient(90deg, #4CAF50, #2E7D32);
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        text-align: center;
    }
    .btn-learn:hover {
        background: linear-gradient(90deg, #2E7D32, #1B5E20);
    }
    @media screen and (max-width: 768px) {
        .feature-box {
            min-height: auto; /* Adjust height for smaller screens */
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Responsive layout using Streamlit columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">💬</div>
            <h3 class="feature-title">Chatbot</h3>
            <p class="feature-description">
                - Offers emotional support.<br>
                - Helps you track your thoughts.<br>
                - Provides guidance in real time.
            </p>
            <button class="btn-learn">Learn More</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">🧠</div>
            <h3 class="feature-title">Cognitive Distortion Identifier</h3>
            <p class="feature-description">
                - Detects negative thought patterns.<br>
                - Offers techniques to challenge them.<br>
                - Encourages positive thinking.
            </p>
            <button class="btn-learn" style="background: linear-gradient(90deg, #2196F3, #1E88E5);">Learn More</button>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="feature-box">
            <div class="feature-icon">📚</div>
            <h3 class="feature-title">Contact and Resources</h3>
            <p class="feature-description">
                - Access professional helplines.<br>
                - Explore educational resources.<br>
                - Stay informed about mental health.
            </p>
            <button class="btn-learn" style="background: linear-gradient(90deg, #FF5722, #E64A19);">Explore Resources</button>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Why Mental Health Matters Section
st.write("## ❤️ Why Mental Health Matters")
st.markdown(
    """
    Mental health impacts every aspect of our lives. It influences how we think, feel, and act. By prioritizing 
    mental health, you can:
    - Build resilience to life’s challenges.
    - Strengthen your relationships.
    - Improve overall quality of life.
    """,
    unsafe_allow_html=True,
)

# Call to Action Section
st.write("## 🚀 Take the First Step Today")
st.markdown(
    """
    Start your journey towards better mental health with our tools and resources:
    - Identify and address cognitive distortions.
    - Access a wide range of resources and professional support.
    """,
    unsafe_allow_html=True,
)

# Navigate to Cognitive Distortion Detector page
st.button("Get Started", help="Begin your mental health journey now!")
    

# Footer Section
st.write("___")
st.markdown(
    """
    <style>
    .footer {
        text-align: center;
        color: #888;
        margin-top: 30px;
        font-size: 0.9em;
    }
    </style>
    <div class="footer">
        Made with ❤️ by Shanthi <br>
        <strong>Disclaimer:</strong> This platform is not a substitute for professional medical advice or therapy. Always seek help from qualified professionals for serious mental health concerns.
    </div>
    """,
    unsafe_allow_html=True,
)
