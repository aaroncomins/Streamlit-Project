import streamlit as st
from PIL import Image

@st.cache
def load_image(imagefile):
    img = Image.open(imagefile)
    return img

# Save our uploaded File
def save_uploaded_file(uploadedfile):
    with open(os.path.join("tempDir",uploadedfile.name))

def main():
    st.title("Multiple File Uploads App")

    menu = ["Home", "About"]
    choice = st.sidebar.selectbox