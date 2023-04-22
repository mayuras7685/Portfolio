import streamlit as st

st.title('Projects')

with st.container():
  col1,col2 = st.columns((1, 2))
  with col1:
    st.image('https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/2cf7715148724d268e9e4b31d46c30ea/assets/favicon/512.jpeg')
  with col2:
    st.write("Project Title")
    st.text("""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""")

with st.container():
  col3,col4 = st.columns((1, 2))
  with col3:
    st.image('https://devfolio-prod.s3.ap-south-1.amazonaws.com/hackathons/2cf7715148724d268e9e4b31d46c30ea/assets/favicon/512.jpeg')
  with col4:
    st.write("Project Title")
    st.text("""
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx""")

