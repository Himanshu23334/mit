import streamlit as st

st.title("Hello! Beta")


name=st.text_input("Enter your name:")

#st.write(f" {name}")

if st.button("Submit"):
    st.write("Hello, Mr.", name)
    