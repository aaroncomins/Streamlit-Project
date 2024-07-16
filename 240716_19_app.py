# Core Packages
import streamlit as st

# Load EDA Packages
import pandas as pd
import numpy as np

# Load Data Vis Package
import plotly.express as px

def main():
    st.title("Plotting in Streamlit with Plotly")
    df = pd.read_csv("data/prog_languages_data.csv")
    st.dataframe(df)

    fig = px.pie(df,values='Sum',names='lang',title='Pie Chart of Languages')
    st.plotly_chart(fig)

    fig2 = px.bar(df,x='lang',y='Sum')
    st.plotly_chart(fig2)

if __name__ == '__main__':
    main()