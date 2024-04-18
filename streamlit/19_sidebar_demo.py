import streamlit as st

#Using object notation
add_selectbox=st.sidebar.selectbox(
    "How would you like to be contacted",
    ("Email","Home phone","mobile phone")
)

#Using "with" notation
with st.sidebar:
    add_radio=st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)","Express(2-5 days)")
    )
    name=st.text_input("Enter Customer Name")