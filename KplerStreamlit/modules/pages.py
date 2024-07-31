import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import json
from PIL import Image
import streamlit_option_menu
from streamlit_option_menu import option_menu
import numpy as np
from modules.map import filter_dataframe, create_marker
import streamlit.components.v1 as components
from modules.KPLER import eda

data_dict = pd.read_csv('media/KplerDataDict.csv')
sample_data = pd.read_csv('media/Live_AIS_data.csv')
sample_data['MMSI'].astype(str)
df = sample_data.iloc[:1000]

def _sample_setter():
    if st.session_state.get('clear'):
        st.session_state['name'] = ''
    if st.session_state.get('streamlit'):
        st.session_state['name'] = 'Streamlit'
    
    st.text_input('Name', key='name')
    
    st.button('Clear name', key='clear')
    st.button('Streamlit!', key='streamlit')

class pages:
    def home(self):
        pass
    def data_dict(self):
        st.title('Data Dictionary')
        st.caption('Copy of raw data dictionary can be provided upon request')
        tab1, tab2= st.tabs(["Sample Data", "Vessel AIS Position Dictionary"])
        with tab1:
            st.subheader('Sample Data')
            st.write('This table shows the response for the AIS Vessel Position call')
            st.dataframe(filter_dataframe(df))
        with tab2:
            st.subheader('AIS Vessel Position data dictionary')
            st.write('')
            st.table(data_dict)
    def map_example(self):
        st.header('Kpler Example Map')
        st.subheader('This shows global vessels but filtered down due to CSV size')
        with st.form(key='my_form', clear_on_submit=False, border=False):
            num_input = st.text_input(label='Enter Number of Vessels')
            submit_button = st.form_submit_button(label='Submit')
            if submit_button:
                try:
                    df = sample_data.sample(n=int(num_input))
                    st.dataframe(df)
                    create_marker(df)
                except:
                    st.write('Please enter valid number')

    def example_analysis(self):
       eda('media/Live_AIS_data.csv')

    def test_page(self):
        pass
