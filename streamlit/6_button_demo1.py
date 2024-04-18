import streamlit as st

animal_shelter=['cat','dog','rabbit','tiger']

animal=st.text_input('type an animal')

if st.button('Check avilability'):
    have_it=animal.lower() in animal_shelter
    if(have_it):
        st.write("we have this animal")
    else:
        st.write("we dont have this animal")
