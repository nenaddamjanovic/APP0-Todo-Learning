import streamlit as st
from PIL import Image

st.header("Takes your picture and turns it to grayscale")
st.write("Click on 'Start camera' and allow browser to use camera")
with st.expander("Start camera"):
    # We start a camera here
    camera_image = st.camera_input("Camera")

# Waits for user to allow camera use in browser
if camera_image:
    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image to grayscale
    gray_img = img.convert("L")

    # Render a grayscale on browser
    st.image(gray_img)