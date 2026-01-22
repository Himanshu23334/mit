import streamlit as st

st.title("Add city and age")
age=st.slider("Select your age" ,1,100)

city = st.selectbox("select your city:", ["delhi", "mumbai", "Chicago", "Houston", "Phoenix"])

if st.button("Submit"):
    st.write("age:", age)
    st.write("city:", city)