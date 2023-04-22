import streamlit as st
from PIL import Image

 

def txt(a, b, c, d, hed, img):
   st.header(hed) #Header
   st.image(img) #Imgage 
   st.write(f'{a}') #Description
   st.markdown(f'##### {b}: {c}') #Skills explored during hackthon
   st.markdown(f'##### Project: {d}') #github link

h1 = Image.open('./img/hacksvit.jpg')
h2 = Image.open('./img/hackout.png')
h3 = Image.open('./img/hackthisfall.png')
h4 = Image.open('./img/dotslash.png')
h5 = Image.open('./img/hackvengers.png')
h6 = Image.open('./img/wittyhacks.png')


st.title('Hackathons')

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["HackSVIT", "Hackout'22", "Hackthisfall 3.0", "DotSlash 6.0", "HackVengers", "WittyHacks 3.0"])

with tab1:   
   txt('My first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`React` , `Node.js`, `Mysql`, `Tailwind CSS`',
      'https://github.com/mayuras7685/SVIT-project-api',
      'HackSVIT',
      h1)

  

with tab2:
   txt('My first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`HTML`, `CSS`, `Flask`, `Mongodb`, `Figma`',
      'https://github.com/mayuras7685/Geek-Unkils_Submission_H22',
      "Hackot'22",
      h2)

with tab3:
   txt('My first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`React`, `Tailwind CSS`, `Flask`, `OCR`, `TensorFlow`, `Vercel`',
      'https://github.com/mayuras7685/KU-hackathon',
      'HackThisFall 3.0',
      h3)

with tab4:
   txt('My first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`React`, `Tailwind CSS`, `Flask`, `OCR`, `TensorFlow`, `Vercel`',
      'https://github.com/mayuras7685/Unkils-DotSlash6.0-Submission',
      'DotSlash 6.0',
      h4)

with tab5:
   txt('My first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`Computer Vision`, `Yolov5`, `Roboflow`, `Colab`',
      'https://github.com/mayuras7685/Unkils_HackVengers',
      'Hackvengers',
      h5)

with tab6:
   txt('My first hackthon and started journey that never ends, to attending   such hackathon we can up to date with latest technology advancemnets, thier in hackthon we creted sort of feedback form that calculates the Happiness index of school students.',
      'Skills', 
      '`TensorFlow`, `React` , `Node.js`, `Mongodb`',
      'https://github.com/WittyhacksCR003/WH012_Unkils',
      'Wittyhacks 3.0',
      h6)
