import json
import streamlit as st
from streamlit_lottie import st_lottie 

def show_thank_you_emoji():
    st.text("  💖  ")

def Ask_To_PDF():
    st.markdown("1. Ask_To_PDF")
    with open('src/pdf.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)

    st.write("This service provides you the functionality to train the AI_Generative model.\n on your PDF and then apply your query on it.")


def ResumeAnalyzer():
    st.markdown("2. ResumeAnalyzer")
    with open('src/Resume.json', 'r', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    
    st.write("Check your resume's goodness \n Get recommendations for skills, fields, courses, etc.")


def main():
    a = "<h1><center>About</center></h1>"

    st.write(a, unsafe_allow_html=True)
    with open('src/About.json') as anim_source:
        animation = json.load(anim_source)
    st_lottie(animation, 1, True, True, "high", 200, -200)

    st.markdown("<p style='text-align: center;'>- ©️Team Unstoppable-</p>", unsafe_allow_html=True)

    
    st.write("\n")
    st.write("\n")

    col1, col2, col3 = st.columns([1,1,1])
    
    with col1:
        st.link_button('GitHub', "https://github.com/navin202/carrercraft.ai")
    with col2:
        st.link_button('LinkedIn', "https://www.linkedin.com/in/navin-kumar-872138245/")
    with col3:
        if st.button('Thankyou'):
            try:
                show_thank_you_emoji()
            except:
                print("💝")

    st.header('', divider='rainbow')
    #st.header('_Streamlit_ is :blue[cool] :sunglasses:')

    st.write("\n")
    st.write("\n")

    st.header("Page info:")
    
    
    Ask_To_PDF()
    ResumeAnalyzer()
    
    
if __name__=="__main__":
    main()


