import streamlit as st
from PIL import Image

st.header("image Gallery")

st.header("shinchan")
img=Image.open("shinchan.webp")
st.image(img,width=400)

st.info("shinchan family")
img2=Image.open("shinchan family.jpg")
st.image(img2,width=500)

