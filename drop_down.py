import streamlit as st
import datetime as dt

st.set_page_config(layout = "wide", page_title="Drop Down Menu")

st.title("Drop Down Menu")

st.selectbox(label = "Choose your operating system", options = ["Windows", "Linux", "macOS"])

st.divider()

st.title("Time and Favorite Team Dropdown")

display_text = "Favorite Football Team"
now = dt.datetime.now().strftime("%y-%m-%d %H:%M")

st.write(f"It is now {now}. I am using a dropdown for: {display_text}")

name = "Aaron"
st.write(f"This is {name}'s python file.")

original_list = ["","Select Team", "Buffalo Bills", "New York Jets", "Miami Dolphins", "New England Patriots"]

result = st.selectbox("Select your favorite team", original_list)
st.write(f"My favorite team is: {result}")
