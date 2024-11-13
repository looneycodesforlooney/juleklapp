import streamlit as st
import os
from PIL import Image

# Path to your images folder
IMAGE_FOLDER = 'images'

# Check if the folder exists and list the files
if not os.path.exists(IMAGE_FOLDER):
    print(f"Error: The folder '{IMAGE_FOLDER}' does not exist!")
else:
    print(f"Reading images from folder: {os.path.abspath(IMAGE_FOLDER)}")

# Get the list of image files in the "images" folder
images = [f for f in os.listdir(IMAGE_FOLDER) if f.endswith('.jpeg')]

# Function to display image based on file name
def show_image(image_file):
    image_path = os.path.join(IMAGE_FOLDER, image_file)
    if os.path.exists(image_path):
        img = Image.open(image_path)
        st.image(img, caption=image_file)
    else:
        st.write("Image not found.")

# Check if the user is on a specific image page
image_name = st.experimental_get_query_params().get('image', [None])[0]

if image_name:
    # If there's an image name in the URL, show the corresponding image
    if image_name in images:
        show_image(image_name)
    else:
        st.write("Image not found.")
else:
    # Display the list of available images with links to their pages
    st.title("Secret Santa!")
    #st.write("Click on an image to view it:")
    st.write("Nothing to see here. This is strictly confidential Secret Santa Stuff")

    #for image in images:
    #    image_url = f"?image={image}"  # This is how the image will be accessed via URL
    #    st.markdown(f"[{image}]({image_url})")
