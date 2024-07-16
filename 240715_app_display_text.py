# Basics & Fundamentals

# Core Pkgs
import streamlit as st

# Load EDA Pkgs
import pandas as pd

# Display Data
# df = pd.read_csv("iris.csv")

# Method 1 (height (first number) and width (second number))
# Schema is filterable, if you leave blank, it will default height and width
# st.dataframe(df,200,100)

# Adding a color style from pandas
# st.dataframe(df.style.highlight_max(axis=0))

# Method 2: Static Table
# Can not be filter or sorted
# st.table(df)

# Method 3: Using superfunction st.write
# st.write(df.head())

# Display JSON
st.json({'data':'name'})

# Display code
mycode = """
def sayhello():
    print("Hello Streamlit Lovers)
# end - for ruby
"""
st.code(mycode,language='python') #or 'ruby' but add the word 'end' above
