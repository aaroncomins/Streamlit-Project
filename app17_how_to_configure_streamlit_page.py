# Core Packages
import streamlit as st
from PIL import Image
img = Image.open("PNG_ex1.png")
# Website for Emojis = emojipedia.org/people/
# Method 1
# Must be the first activity of streamlit
# st.set_page_config(page_title='STREAMLIT PROJECT',
#                    page_icon=img, layout='wide',
#                    initial_sidebar_state='expanded')
# other options for initial_sieebar_state are 'collapsed' or "auto"
                    # page_icon = ":knife:")

# Method 2: Dictionary
PAGE_CONFIG = {"page_title":"AaronsStreamlit","page_icon":"knife","layout":"centered"}
st.set_page_config(**PAGE_CONFIG)

 # Additional Packages

# Fxns

def main():
    """All your code goes here"""
    st.title("Hello Streamlit Lovers :knife: :smiley:")
    st.sidebar.success('Menu')

if __name__ == '__main__':
    main()
