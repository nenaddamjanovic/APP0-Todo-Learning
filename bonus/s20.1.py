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

    # Convert image to RGB
    rgb_img = img.convert('RGB')

    # Convert image to black and white (binary)
    binary_img = img.convert('1')

    # Convert image to a palette-based image
    palette_img = img.convert('P')

# ------------------------------------------------------------

    # Render on browser
    st.image(gray_img)
    st.image(rgb_img)
    st.image(binary_img)
    st.image(palette_img)