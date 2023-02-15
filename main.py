import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])

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

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write("[Source Code](https://python.org)")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write("[Source Code](https://python.org)")