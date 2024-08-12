# Core Packages
import streamlit as st  

# Working with Widgets
# Button/Radio/Checkbox/Select/

# Working with Buttons
name = "Aaron"
if st.button("Submit"):
    st.write("Name: {}".format(name.upper()))

if st.button("Submit", key='new02'): #need to write key if you have a button with the same name
    st.write("First Name: {}".format(name.lower()))

# Working with Radio Buttons
status = st.radio("What is your status",("Active", "Inactive"))
if status == "Active":
    st.success("You are Active!")
elif status == 'Inactive':
    st.warning("You are Inactive!")

# Working with Checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing something")

# Working with Beta Expander (you can also use if instead of with but i couldn't get it to work)
with st.expander("Expander"):
    st.success("Hello Expander")

with st.expander("Jessie"):
    st.text("Hello Jessie")