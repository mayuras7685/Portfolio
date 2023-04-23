import streamlit as st

st.title('Projects')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image('https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/2cf7715148724d268e9e4b31d46c30ea/assets/favicon/512.jpeg')
  with col2:
    st.subheader("Olympic Data Analysis Web Application")
    st.write("""
    This analysis will provide detailed and accurate information regarding various factors which leads to the evolution of Olympic Games and improvement of Countries/Players over the time in visual format.
    """)
    st.markdown('`EDA`, `Streamlit`, `pandas`, `matplotlib`, `plotly`, `seaborn`')

st.write('---')

with st.container():
  col3,col4 = st.columns((1, 2))
  with col3:
    st.image('https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/2cf7715148724d268e9e4b31d46c30ea/assets/favicon/512.jpeg')
  with col4:
    st.header("Deadly Animal Detection")
    st.write("""Custom object detection model that detects 6 classes (Tiger, Lion, Hyena, Cheetah, Wolf, Fox) and And came up with an Interface that detects Wild animals from webcam feed, images, and URLs of images""")
    st.markdown('`Computer Vision`, `openncv-python`, `RCNN`, `Yolo`, `Roboflow`, `colab` ')

