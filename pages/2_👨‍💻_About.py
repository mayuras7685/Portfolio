import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import plotly.graph_objects as go
from streamlit_timeline import timeline

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_url_hello = "https://assets1.lottiefiles.com/packages/lf20_vfpu2rpp.json"

with st.container():
    col1, col2 = st.columns((2, 1))
    with col1:
      st.title('About')
      st.write('My name Mayur Asodara, and I am ***Electronics and Communication Engineering*** Undergraduate from VishwaKarma Government College - Ahmedabad.')

      st.write('As an ambitious and hardworking individual, I am constantly seeking opportunities to enhance my knowledge and skills. My passion for Artificial Intelligence and Machine Learning has led me to gain expertise in this field.')
        

    with col2:
        st_lottie(
            load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_Yf4ThO8if1.json"),
            height= 400,
            width= 300
        )


st.title('Eduaction 📖')

st.write('-----------')

with st.container():
    col3, col4 =st.columns((2,1))
    with col3:
        st.write('Vishwakarma Government Engineering College, Ahmedabad')
        st.text('Bachelors in Engineering: Electronics and Communication ')

    with col4:
        st.write('June-2024 ***(expected)***')

st.write('-----------')

with st.container():
    col3, col4 =st.columns((2,1))
    with col3:
        st.write('Axay HighSchool, Ahmedabad')
        st.text('GSHEB (Class XII)')

    with col4:
        st.write('March-2020')

st.write('-----------')

with st.container():
    col3, col4 =st.columns((2,1))
    with col3:
        st.write('Shriji Vidhyalay, Ahmedabad')
        st.text('GSHEB (Class X)')

    with col4:
        st.write('March-2018')
st.write('-----------')

    
# with st.spinner(text="Building line"):
#     with open('timeline.json', "r") as f:
#         data = f.read()
#         timeline(data, height=400)

st.title('Skills & Tools ⚒️')


with st.container():
    col5, col6, col7, col8= st.columns((1, 1, 1, 1))

    with col5:
        st.button('Python')
        st.button('Computer Vision')
        st.button('NLP')
    
    with col6:
        st.button('Flask')
        st.button('YOLO')
        st.button('TesorFlow')

    with col7:
        st.button('Mongodb')
        st.button('MySQL')
        st.button('Tableau')

    with col8:
        st.button('Colab')
        st.button('Streamlit')
        st.button('FastAPI')
st.write('-----')

st.title('Courses & Certification 📑')


