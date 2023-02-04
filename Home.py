import streamlit as st
from requests import get

api_key = "sIwzWUH1dNgBnD9M8yYT8xDXc9OpQwgBCYuC6eUj"
request_url = "https://api.nasa.gov/planetary/apod?" + \
              f"api_key={api_key}"
request = get(request_url)
content = request.json()

img_url = content["hdurl"]
page_text = content["explanation"]

st.title(content["title"])
st.subheader("Astronomy Picture of the Day")
st.image(img_url)
st.write(page_text)
