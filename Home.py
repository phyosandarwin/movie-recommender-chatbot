import streamlit as st
from components.ui_components import display_lottie_animation, load_lottie
from streamlit_extras.switch_page_button import switch_page
from PIL import Image
st.set_page_config(page_title="Cinematic Seeker", page_icon="🍿", layout="wide")


# load lottie
lottie_coding = load_lottie("https://assets1.lottiefiles.com/packages/lf20_CTaizi.json")

# Divide the layout into two columns
col1, col2 = st.columns([4,1])  
with col1:
        st.title("Welcome to Cinematic Seeker")
        st.markdown('''
                    Choose to interact with the movie recommendation guide or the chatbot 
                    feature. 
                    ''')
        st.error("You need to have a Hugging Face account to to use the chatbot!")
with col2:
        display_lottie_animation(lottie_coding)

st.divider()

column1, column2, column3 = st.columns([1,1,2])

with column1:
    use_chatbot = st.button("I want to use the chatbot!")
    if (use_chatbot):
        switch_page("Chatbot")

    use_guide = st.button("I want to use the guide!")
    if (use_guide):
            switch_page("Guide")

with column2:
    st.write("")

with column3:
    picture = Image.open("images/movie_meme.jpg")
    st.image(picture, width=400)


