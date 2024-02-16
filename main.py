import schedule
import streamlit as st

import api_helper


def job():
    api_helper.get_data_from_api()


schedule.every().day.at('07:00').do(job)

with open("./static/apod.txt") as file:
    image_description = file.read()

with open("./static/apod_title.txt") as file:
    title = file.read()

st.header(title, divider='rainbow')
st.image("./static/apod.jpg")
st.write(image_description)

schedule.run_pending()
