import streamlit as st
import os
from PIL import Image
from first_init import run_init

run_init()
logo = Image.open("image/logo.png")
logo_green = Image.open("image/logo_green.png")

st.set_page_config(
    page_title="Welcome to TechWas!",
    page_icon=logo,
)

st.sidebar.success("Select a demo above.")

st.image(logo_green, use_column_width=True)

st.write(
    "<h1 style='text-align: center;'>Welcome!</h6>",
    unsafe_allow_html=True,
)

st.markdown(
    """
    TechWas is a student-led organization dedicated to enhancing the management of e-waste disposals and increasing awareness of electronic waste. Our team of six members, divided into machine learning, cloud computing, and mobile development divisions, has developed an app to achieve our goal. 
    
    On this page, we showcase the **image classification** and **summarization** capabilities of our project. Our goal is to provide anyone who is interested about our project with a clear understanding of how we’re using machine learning to tackle electronic waste. We value your feedback and welcome any suggestions you may have. Thank you for visiting!
    """
)

st.markdown(
    """    
    ##### **Visit our repository [here](https://github.com/TechWas)!**
    """
)
