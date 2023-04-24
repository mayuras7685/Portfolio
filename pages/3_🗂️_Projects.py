import streamlit as st
from PIL import Image

st.title('Projects')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image(Image.open('./img/p1.png'))
  with col2:
    st.subheader("Olympic Data Analysis Web Application")
    st.write("""
    This analysis will provide detailed and accurate information regarding various factors which leads to the evolution of Olympic Games and improvement of Countries/Players over the time in visual format.
    """)

    st.markdown('`EDA`, `Streamlit`, `pandas`, `matplotlib`, `plotly`, `seaborn`')

    g1 = '[GitHub](https://github.com/mayuras7685/Olympics-data-analysis)'
    st.markdown(g1)

st.write('---')

with st.container():
  col3,col4 = st.columns((1, 2))
  with col3:
    st.image(Image.open('./img/p2.png'))
  with col4:
    st.subheader("Wild Animal Detection")
    st.write("""Custom object detection model that detects 6 classes (Tiger, Lion, Hyena, Cheetah, Wolf, Fox) and And came up with an Interface that detects Wild animals from webcam feed, images, and URLs of images""")

    st.markdown('`Computer Vision`, `openncv-python`, `RCNN`, `Yolo`, `Roboflow`, `colab` ')

    g2 = '[GitHub](https://github.com/mayuras7685/Deadly_animal_detection)'
    st.markdown(g2)

st.write('---')

with st.container():
  col5,col6 = st.columns((1, 2))
  with col5:
    st.image(Image.open('./img/p3.png'))
  with col6:
    st.subheader("Portfolio Website Using Streamlit")
    st.write("""Portfolio Website using Streamlit library, multi page stremlit webapp to showcase my work and skills """)

    st.markdown('`Python`, `Streamlit`')

    g3 = '[GitHub](https://github.com/mayuras7685/portfolio)'
    st.markdown(g3)


  

