# Basics & Fundamentals

# Core Pkgs
import streamlit as st

# Working with and Displaing Text
st.text("Hello World this is a test")

name = "Aaron"
st.text(f"This is {name}")

# Header 
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Title
st.title("This is the title")

# Markdown
st.markdown("## This is markdown")

#Displaying Colored Text/Bootstraps Alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("Thiss is an error")
st.exception("This is an exception")

# Superfunction
st.write("Normal Text")
st.write("## This is a mardown text")
st.write(1+2)

st.write(dir(st))

st.help(range)

