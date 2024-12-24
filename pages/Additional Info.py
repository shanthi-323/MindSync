import streamlit as st

# Set up the page configuration
st.set_page_config(page_title="Additional Resources", page_icon="📚", layout="wide")

# Add custom CSS for enhanced UI and responsiveness
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        color: #34495E;
        background-color: #1E1E2F;
    }
    .section-title {
        font-size: 2.5em;
        font-weight: bold;
        background: rgb(238,174,202);
        background: radial-gradient(circle, rgba(238,174,202,1) 0%, rgba(148,187,233,1) 100%);
        margin-top: 30px;
        margin-bottom: 20px;
        text-align: center;
        border-bottom: 2px solid #1ABC9C;
        padding-bottom: 10px;
    }
    .resource-box {
        background-color: #2C2C38;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 30px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s, box-shadow 0.3s;
        width: 100%;
    }
    .resource-box:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0, 0, 0, 0.4);
    }
    .resource-box h3 {
        color: #1ABC9C;
        margin-bottom: 15px;
        text-align: center;
        font-size: 1.8em;
    }
    .resource-box p {
        color: #ECECEC;
        margin-bottom: 15px;
        line-height: 1.6;
        text-align: justify;
    }
    .resource-box a {
        display: inline-block;
        background-image: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        padding: 10px 15px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 10px;
        text-align: center;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .resource-box a:hover {
        background-color: #2980B9;
        transform: scale(1.05);
        text-decoration: none;
    }
    .column-section {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: space-between;
        

    }
    .column {
        flex: 1;
        min-width: 300px;
        max-width: 400px;
        margin: 10px;
    }
    @media screen and (max-width: 768px) {
        .resource-box {
            margin: 15px auto;
        }
        .section-title {
            font-size: 2em;
        }
        .column-section {
            flex-direction: column;
            align-items: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.title("📚 Additional Resources")
st.markdown(
    """
    Welcome to the Additional Resources page! Here you will find valuable tools, support services, and
    information to guide your mental health journey in Malaysia.
    """
)

# General Information Section
st.markdown("<div class='section-title'>Understanding Mental Health</div>", unsafe_allow_html=True)
with st.container():
    st.markdown(
        """
        - **Importance of Mental Health:** Mental health affects how we think, feel, and act.
        - **Common Challenges:** Depression, anxiety, and stress are prevalent in Malaysia.
        - **Reducing Stigma:** Normalize conversations and seek professional help.
        """
    )

# Cognitive Behavioural Therapy (CBT) Section
st.markdown("<div class='section-title'>Cognitive Behavioural Therapy (CBT)</div>", unsafe_allow_html=True)
with st.container():
    st.markdown(
        """
        - **What is CBT?**
          - A structured therapy focusing on changing negative thought patterns.
        - **Techniques:**
          - Thought logs.
          - Behavioral activation.
          - Cognitive restructuring.
        - **Resources:**
          - <a href='https://www.getselfhelp.co.uk' class='resource-link'>CBT Workbooks</a>
          - <a href='https://www.coursera.org' class='resource-link'>CBT Online Courses</a>
        """,
        unsafe_allow_html=True,
    )

# Cognitive Distortions Section
st.markdown("<div class='section-title'>Cognitive Distortions</div>", unsafe_allow_html=True)
st.markdown(
    """
    - **Examples:**
      - All-or-Nothing Thinking: "If I fail, I'm a failure."
      - Catastrophizing: "Everything will go wrong."
    - **How to Challenge Distortions:**
      - Recognize distorted thoughts.
      - Question their validity.
      - Replace with balanced alternatives.
    """
)

# Coping Strategies Section
st.markdown("<div class='section-title'>Coping Strategies</div>", unsafe_allow_html=True)
with st.container():
    st.markdown(
        """
        - **Healthy Coping Mechanisms:**
          - Journaling.
          - Mindfulness and breathing exercises.
          - Positive activities like yoga or walking.
        - **Emergency Tips:**
          - Focus on breathing during panic attacks.
          - Grounding exercises like the 5-4-3-2-1 technique.
        """
    )

# Mental Health Support in Malaysia Section
st.markdown("<div class='section-title'>Mental Health Support in Malaysia</div>", unsafe_allow_html=True)
with st.container():
    st.markdown("<div class='column-section'>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class='resource-box'>
        <h3>Government Resources</h3>
        <p>- **Malaysia Mental Health Association (MMHA):** <a href='https://mmha.org.my' class='resource-link'>Visit Website</a></p>
        <p>- **Talian Kasih 15999:** 24/7 helpline.</p>
        <p>- **Public Hospitals:** Affordable care.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class='resource-box'>
        <h3>Private Resources</h3>
        <p>- **MentCouch:** Private counseling services.</p>
        <p>- **ThoughtFull:** Online therapy platform.</p>
        <p>- **Mind Matters:** Private therapy clinic.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class='resource-box'>
        <h3>Crisis Helplines</h3>
        <p>- **Befrienders KL:** <a href='https://www.befrienders.org.my' class='resource-link'>Visit Website</a></p>
        <p>- **MIASA:** Support for mental health challenges.</p>
        <p>- **MCMC Support Line:** Emotional crisis support.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)

# Educational Resources Section
st.markdown("<div class='section-title'>Educational Resources</div>", unsafe_allow_html=True)
with st.container():
    st.markdown(
        """
        - **Awareness Campaigns:** Participate in mental health events like World Mental Health Day.
        - **Workshops:** Learn CBT techniques through local workshops.
        - **Apps:**
          - <a href='https://www.thoughtfull.world' class='resource-link'>ThoughtFull</a>
          - <a href='https://www.calm.com' class='resource-link'>Calm</a>
          - <a href='https://www.headspace.com' class='resource-link'>Headspace</a>
        """,
        unsafe_allow_html=True,
    )

# Personal Stories Section
st.markdown("<div class='section-title'>Personal Stories</div>", unsafe_allow_html=True)
st.markdown(
    """
    Real-life experiences from individuals who have benefited from therapy or mental health support in Malaysia. 
    These stories aim to inspire and normalize seeking help for mental health issues.
    """
)

# Footer Section
st.markdown("---")
st.markdown(
    """
    Made with ❤️ to support mental health awareness in Malaysia.  
    **Disclaimer:** This platform is not a substitute for professional medical advice. For serious mental health concerns, always consult a qualified professional.
    """
)
