import streamlit as st



text = st.text_area("enter text")
submitbtn = st.button("Enter")

if submitbtn:
    st.balloons()
    st.success(text)