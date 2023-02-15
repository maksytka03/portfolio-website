import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg", width=600)

with col2:
    st.title("Pavlo Demianov")
    content = """
    Hi, I am Pavlo! I am a Python programmer. Currently, I am actively learning Python,
    and this is my first website written on it.
    """
    st.info(content)

content2 = """
Below, you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)
