import streamlit as st 
import pandas as pd
import time

# Text Element
st.text("This is text")
st.title("This is a title:H")
st.header("This is a header")
st.subheader("This is a subheader")
st.write("This is a super function")
st.markdown(""" This is "markdown" """)
st.latex("\int")
st.json("""{"data":"This is streamlit"}""")
st.code("""
print("Hello Streamlit")
a=40
""", language="python", line_numbers=True)

# Error Element
st.success("This is success")
st.error("this is an error")
st.warning("Warning")
st.exception("TypeError")

# Input Widget
first_name = st.text_input("First Name")
password = st.text_input("Password",type="password")
message = st.text_area("Message")
date = st.date_input("Date")
appointment_time = st.time_input("Appointment Time")
age = st.number_input("Age",min_value=0,max_value=120)
gender = st.radio("Gender",["Male","Female"])
enable = st.toggle("Enable Picker")
level = st.checkbox("Level")

# Sliders
countries = st.selectbox("Countries",["Ghana","UK","India","Germany","USA"])
programming_languages = st.multiselect("Programming", ["Python","Golang","Julia","Javascript","Rust"])
rating = st.slider("Rating",0,10)
ranking = st.select_slider("Ranking",["Junior Dev","Mid Dev","Senior Dev","Architect"])

st.divider()
if enable:
    st.write(f"Details: {first_name},{password}")
    color = st.color_picker("Pick a Color")
    st.write(color)

# Data Elements

def load_data(data) -> pd.DataFrame:
    return pd.read_csv(data)

df = load_data("iris.csv")

st.write("Searchable and Downloadable")
st.dataframe(df)

st.write("Simple head/tail method")
st.table(df.head(2))

st.write("Dataframe that you can edit")
edited_df = st.data_editor(df)

# st.json(df.to_json())

# Connection to DB
# st.connection()

# Media Elements
img = st.image("image_icon.png")
audio_file = open("song.mp3", "rb")
st.audio(audio_file.read())

# Video
# st.video()

if st.button("Take a Picture"):
    pic = st.camera_input("Take a Photo")
    with open(f"{pic.name}","wb") as f:
        f.write(pic.getbuffer())

# Download and Uploads
file_upload = st.file_uploader("Upload CSV",type="csv")
if file_upload:
    st.write(pd.read_csv(file_upload))

st.download_button("Download","iris.csv")

# Status Element
if st.button("Compute"):

    with st.spinner("Thinking..."):
        time.sleep(4)
        st.write("Hello")

    # These lines do not work live due to str
    # with st.progress("Progressing"):
    #     time.sleep(2)
    #     st.write("Hello")

    st.toast("This is a toast")

# Chat Elements (LLM UI)
# Typewrite effect
def stream_data(data,delay:float=0.02):
    for word in data.split():
        yield word + " "
        time.sleep(delay)
prompt = st.chat_input("Ask Something")
if prompt:

    with st.chat_message("user"):
        st.write(f"You typed {prompt}")

    with st.spinner("Thinking..."):
        time.sleep(0.5)
        response = f"some random text from streamlit"
        st.write_stream(stream_data(response))

# Streaming Response
# Generator
# Some text or data
        
response = f"some random text from streamlit"
if st.button("Stream"):
    st.write_stream(stream_data(response))

st.divider()
### Layouts
# Tabs
home_tab, about_tab = st.tabs(["Home","About"])

with home_tab:
    st.subheader("This a home tab")

with about_tab:
    st.subheader("This is an about tab")
    st.dataframe(df)

# Columns
col1, col2, col3 = st.columns(3)
# Context manager approach
with col1:
    st.title("Columns")

col2.dataframe(df)

col3.image("image_icon.png",use_column_width=True)

st.divider()
# Container
container = st.container(border=True)
container.write("Some container")

row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":knife:")

# Expander and Popover
with st.expander("Expander"):
    st.dataframe(df)

with st.popover("Popover"):
    st.image("image_icon.png")

### Plots
st.area_chart(df,x="sepal_length",y="petal_length")

st.line_chart(df,x="sepal_length",y="petal_length")

st.bar_chart(df,x="sepal_length",y="petal_length")

st.scatter_chart(df,x="sepal_length",y="petal_length")
                 
# st.pyplot
# Need to add more to these, incomplete
# st.plotly_chart()
# st.altair_chart()
# st.map()
# st.bokeh_chart()

st.help(st.pyplot)
st.write(dir(st))

with st.form("Myform"):
    first_name = st.text_input("First Name")
    password = st.text_input("Password",type="password")
    message = st.text_area("Message")
    button = st.form_submit_button("Submit")

import streamlit.components.v1 as stc 
stc.html("<p> hello </p>")
stc.iframe()
# st.link_button("Visit",url="insert link")

# st.session_state
# st.cache_data

