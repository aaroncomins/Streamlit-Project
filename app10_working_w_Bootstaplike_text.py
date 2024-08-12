# Basics & Fundamentals

# Core Packages
import streamlit as st 

# Working with and Displaying Text
st.text("Hello World this is a text")
name = "Aaron"
st.text("This is so {}".format(name))

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Title
st.title("This is a title")

# Markdown
st.markdown("## This is markdown")

# Displaying Colored Text/Bootstraps Alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")
st.exception("This is an exception")