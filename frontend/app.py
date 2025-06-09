import streamlit as st
import requests
st.title(" AI Tutor & Quiz Generator")
lesson_text = st.text_area("Paste lesson content or textbook paragraph here:")
if st.button("Generate Learning Aids"):
    res = requests.post("http://localhost:8000/generate/", data={"text": lesson_text})
    output = res.json()
    st.subheader(" Simplified Explanation")
    st.write(output["explanation"])
    st.subheader(" Quiz Questions & Answers")
    st.write(output["quiz"])
    st.subheader(" Key Concepts")
    st.write(output["concepts"])