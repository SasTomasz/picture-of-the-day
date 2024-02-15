import streamlit as st

with open("./assets/data/apod.txt") as file:
    image_description = file.read()

with open("./assets/data/apod_title.txt") as file:
    title = file.read()

st.header(title, divider='rainbow')
st.image("./assets/images/apod.jpg")
st.write(image_description)
