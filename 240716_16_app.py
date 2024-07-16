# Core Packages
import streamlit as st

# Text Input
fname = st.text_input("Enter Firstname",max_chars=10)
password = st.text_input("Enter Password",type="password")
st.title(fname)

# Text Area
message = st.text_area("Enter Message",height=100)
st.write(message)

# Numbers
number = st.number_input("Enter Number",1,25)

# Date Input
myappointment = st.date_input("Appointment")

# Time Inputs
mytime = st.time_input("My Time")

# Color Picker
# beta does not work => (color = st.beat_color_picker("Select Color"))
color = st.color_picker("Select Color")