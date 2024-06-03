import streamlit as st
from PIL import Image
from pathlib import Path

st.header("Takes your picture and turns it to grayscale")




# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)
    # Convert the image to grayscale
    gray_uploaded_img = img.convert('L')
    # Display the grayscale image on the webpage
    st.write("This is your grayscale converted image:")
    st.image(gray_uploaded_img)

st.divider()
st.write("or click on 'Start camera' and allow browser to use camera")

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
    st.write("grayscale image:")
    st.image(gray_img)
    st.write("rgb image:")
    st.image(rgb_img)
    st.write("binary image:")
    st.image(binary_img)
    st.write("pallete image:")
    st.image(palette_img)

# --------------------------------------------------------------

    # Construct the path to the desktop
    desktop_path = Path.home() / "Desktop" / "saved_image.jpg"
    # Save the result
    rgb_img.save(desktop_path)
    st.write("Image saved to desktop")
