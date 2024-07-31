import streamlit as st
import pandas as pd
import json
from PIL import Image
import streamlit_option_menu
from streamlit_option_menu import option_menu
import numpy as np
from modules.pages import pages

#To Run
#streamlit run main.py --server.port=8080

def add_logo(logo_path):
    """Read and return a resized logo"""
    logo = Image.open(logo_path)
    return logo

class main(pages):
    def __init__(self):
        self.main()
    
    def main(self):
        super().__init__()
        st.set_page_config(layout="wide")
        with st.sidebar:
            st.sidebar.image(add_logo(logo_path="media/IDST_tpt (1).png"))
            selected = option_menu(
                menu_title = "Kpler API Showcase",
                options = ["Home", "Data Dictionary", "Map Example", "Analysis Example"],
                menu_icon = "house",
                default_index = 0,
            )
        page_methods = {
            "Home": self.home,
            "Data Dictionary": self.data_dict,
            "Map Example": self.map_example,
            "Analysis Example": self.example_analysis
        }
        
        page_methods[selected]()



if __name__ == '__main__':
    main()