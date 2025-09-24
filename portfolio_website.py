import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Portfolio Website',page_icon='crazy profile photo.png',layout='wide')
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpaperaccess.com/full/1124156.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0); /* Transparent header */
}

[data-testid="stToolbar"] {
    right: 2rem;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align: center; color: #ffffff; padding: 30px;'>Bringing together Code, Creativity and Intelligence</h1>", 
    unsafe_allow_html=True
)
st.markdown(
    "<h6 style='text-align: center; color: #ffffff; margin-left: 100px; margin-right: 100px;'>This website is a showcase of my skills, projects, and experiences. It brings together my work in data science, machine learning, engineering and digital content creation while also reflecting my journey as a learner and problem-solver. Feel free to explore my projects and get in touch!</h6>", 
    unsafe_allow_html=True
)
st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Projects','Links','Contact'],
        icons = ['person','code-slash','link-45deg','chat-left-text-fill'],
        orientation = 'horizontal'
        
    )
if selected=='About':
    with st.container():
        left_margin, col1, col2, right_margin = st.columns([0.2, 3, 1, 0.4])
        with col1:
            st.write("#####")
            st.title("Aditya Chakraborty")
            st.subheader("Undergraduate Student at Indian Institute of Technology, Kharagpur")
            st.markdown("#### Exploring various different technologies")
            st.markdown("[Linkedin](https://www.linkedin.com/in/adityachakrabortyiitkgp/)"+'     |     '+"[Instagram](https://www.instagram.com/adi_borty/?__pwa=1)"+'     |     '+"[Facebook](https://www.facebook.com/profile.php?id=61566906508902&ref=_ig_profile_ac)")
        with col2:
            st.image('1732554444067.png',use_container_width=True)
    
    st.write("---")

    with st.container():
        left_margin3,col3,col4,col5,right_margin3 = st.columns([0.2,1,1,1,0.2])
        with col3:
            st.subheader("""
        Education
        - Indian Institute of Technology, Kharagpur
            - Bachelor of Technology - Ocean Engineering and Naval Architecture
        - New Bombay City School, Ghansoli, Navi Mumbai
            - 11th & 12th - PCM
            - 12th Board - 92.8%
        - Bal Bharati Public School, Kharghar, Navi Mumbai
            - 2009-2022 
            - 10th Board - 94.8%
        """)
        with col4:
            st.subheader("""
        Experience
        - IDEAS-TIH @ ISI Kolkata - Foundational Autumn Internship Program
            - Position - Data Science Project Intern
                - Duration - (August 2025 - September 2025)
                - Type: Remote
        - SkilField Mentor - Internship (Trainee Program)
            - Position - Machine Learning Intern
                - Duration - (August 2025 - February 2026)
                - Type: Remote
        """)
        with col5:
            st.subheader("""
        Extracurriculars
        - Kshitij, IIT Kharagpur
            - Position - Design and Media Subhead (Portfolio - Videography)
                - Duration - (August 2025 - February 2026)
            - Position - Design and Media Associate Member 
                - Duration - (November 2024 - February 2025)
            - Position - Kshitij X Boeing National Aeromodelling Competition Volunteer
                - Duration - (January 2025 - January 2025)
        - Samudramanthan, IIT Kharagpur
            - Position - Associate Member
                - Duration - (September 2024 - April 2025)
        """)
        st.write("---")
if selected=='Projects': 
    with st.container():
        st.header("My Projects")
        st.write("###")
        left_margin1,col6,middle_col,col7,right_margin1 = st.columns([0.2,1,0.2,2,0.2])
        with col6:
            st.markdown(
            """
            <style>
            .responsive-img {
            width: 58%;           
            max-width: 400px;      
            height: auto;         
            display: block;
            margin: 0 auto 30px;
            }
            </style>
            """,
            unsafe_allow_html=True
            )
            st.markdown('<img src="https://static.wixstatic.com/media/5e79ca_dce5c923992f41fa81d8465041fe5163~mv2.png/v1/fill/w_109,h_107,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/IDEAS-TIH%2C%20ISI%2C%20Kolkata.png" class="responsive-img">',unsafe_allow_html=True)
        with col7:
            st.markdown("<h3 style='margin-bottom: -35px;'>Fake News Detection and Evaluation with Confusion Matrix</h3>",unsafe_allow_html=True)
            st.write("Associated with Foundational Autumn Internship - IDEAS-TIH @ ISI Kolkata")
            st.write("Fake News Detection using Machine Learning (Logistic Regression & Random Forest). Includes preprocessing, EDA, vectorization with Word2Vec, model training, evaluation, and serialization. Repository contains Jupyter notebooks, datasets, pickle models, project report, and a demo video.")
            st.markdown("[Visit GitHub Repository](https://github.com/Adiborty-Code/IDEAS-TIH-ISI-Kolkata-Project-Repo)")
        st.write("---")
if selected=='Contact':
    st.header("Contact me via Email!")
    st.write("##")

    contact_form = """
    <style>
    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
        color: white;
    }
    input, textarea {
        padding: 15px;
        border-radius: 5px;
        border: 1px solid gray;
    }
    button {
        padding: 10px;
        border: none;
        border-radius: 5px;
        background-color: #0078ff;
        color: white;
        cursor: pointer;
    }
    button:hover {
        background-color: #005bb5;
    }
    </style>

    <form action="https://formsubmit.co/adityachakraborty153@gmail.com" method="POST">
        <input type = "hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_margin2,left_col,middle_margin,right_col,right_margin2 = st.columns([0.2,2,0.4,1,0.3])
    with left_col:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_col:
        st.image("1732554444045.png",use_container_width=True)
    st.write("---")
if selected=='Links': 
    with st.container():
        st.header("Important links to checkout!")
        st.write("###")
        l1,c1,c2,r1 = st.columns([0.4,1,2,0.2])
        with c1:
            st.image('Github.png',width=220)
        with c2:
            st.markdown("<h3>GitHub</h3>",unsafe_allow_html=True)
            st.write("All my GitHub repository projects and also upcoming ones on Artificial Intelligence and Machine Learning will be pushed here.")
            st.markdown("[GitHub Profile](https://github.com/Adiborty-Code/)")
        st.write("---")
        st.write("######")
        l2,c3,c4,r2 = st.columns([0.4,1,2,0.2])
        with c3:
            st.image('Kaggle.png',width=220)
        with c4:
            st.markdown("<h3>Kaggle</h3>",unsafe_allow_html=True)
            st.write("My Kaggle Account for data science and machine learning notebooks.")
            st.markdown("[Kaggle Profile](https://www.kaggle.com/adibortykaggle/competitions)")
        st.write("---")
        st.write("######")
        l3,c5,c6,r3 = st.columns([0.4,1,2,0.2])
        with c5:
            st.image('Leetcode.png',width=220)
        with c6:
            st.markdown("<h3>Leetcode</h3>",unsafe_allow_html=True)
            st.write("This is my personal LeetCode account, all the solved DSA questions here.")
            st.markdown("[Leetcode Profile](https://leetcode.com/u/axXXo0mxnI/)")
        st.write("---")
        st.write("######")
        l4,c7,c8,r4 = st.columns([0.4,1,2,0.2])
        with c7:
            st.image('codeforces.png',width=220)
        with c8:
            st.markdown("<h3>CodeForces</h3>",unsafe_allow_html=True)
            st.write("This is my personal CodeForces account, all the solved DSA questions here.")
            st.markdown("[Codeforces Profile](https://codeforces.com/profile/Adi_borty)")
        st.write("---")
        st.write("######")
        l5,c9,c10,r5 = st.columns([0.4,1,2,0.2])
        with c9:
            st.image('Design and media portfolio.png',width=220)
        with c10:
            st.markdown("<h3>Design and Media Portfolio</h3>",unsafe_allow_html=True)
            st.write("This Google Drive folder has all the design and media projects in which I have worked on.")
            st.markdown("[Drive Folder Link](https://drive.google.com/drive/u/3/folders/1Wwd7f9SY7Gj8pz8Jzv7Ifqk_bTld9YNf)")
        st.write("---")