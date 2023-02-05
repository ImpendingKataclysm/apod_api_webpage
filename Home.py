import streamlit as st
from requests import get

api_key = "sIwzWUH1dNgBnD9M8yYT8xDXc9OpQwgBCYuC6eUj"
request_url = "https://api.nasa.gov/planetary/apod?" + \
              f"api_key={api_key}"

response = get(request_url)
content = response.json()

title = content["title"]
img_url = content["url"]
page_text = content["explanation"]

img_path = "img.png"
img_response = get(img_url)

with open(img_path, "wb") as file:
    file.write(img_response.content)

st.title(title)
st.subheader("Astronomy Picture of the Day")
st.image(img_path)
st.write(page_text)
