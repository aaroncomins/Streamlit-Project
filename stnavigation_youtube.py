import streamlit as st 
from streamlit_option_menu import option_menu
# Icon website: https://icons.getbootstrap.com/
# Youtube video: https://www.youtube.com/watch?v=hEPoto5xp3k 
# 1. As Sidebar Menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu", #required
#         options=["Home", "Projects", "Contact"], #required
#         icons=["house", "book", "envelope"], #optional
#         menu_icon="cast", #optional
#         default_index=0, #optional
#     )

# 2. As Horizontal Menu
# with st.sidebar:
#     selected = option_menu(
#         menu_title="Main Menu", #required
#         options=["Home", "Projects", "Contact"], #required
#         icons=["house", "book", "envelope"], #optional
#         menu_icon="cast", #optional
#         default_index=0, #optional
#         orientation="horizontal",
#         styles={
#             "container": {"padding": "0!important", "background-color": "#fafafa"},
#             "icon": {"color": "orange", "font-size": "25px"},
#             "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#             "nav-link-selected": {"background-color": "green"},
#         }
#     )
# 3. Different Style
# with st.sidebar:
#     selected = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
#         icons=['house', 'cloud-upload', "list-task", 'gear'], 
#         menu_icon="cast", default_index=0, orientation="horizontal",
#         styles={
#             "container": {"padding": "0!important", "background-color": "#fafafa"},
#             "icon": {"color": "orange", "font-size": "25px"}, 
#             "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#             "nav-link-selected": {"background-color": "green"},
#         }
#     )
# 4. Black lettering
with st.sidebar:
    selected = option_menu(None, ["Home", "Projects", "Contact", 'Settings'],
        icons=['house', 'p-square', "list-task", 'gear'],
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee", "color": "black"},
            "nav-link-selected": {"background-color": "green", "color": "black"}
        }
    )
    with st.expander("tst"):
        st.write(selected)
if selected == "Home":
    st.title(f"You have selected {selected}")
if selected == "Projects":
    st.title(f"You have selected {selected}")
if selected == "Contact":
    st.title(f"You have selected {selected}")
if selected == "Settings":
    st.title(f"You have selected {selected}")


#################### st.navigation #######################
    


home_page = st.Page(__file__, title="Home")
upload_page = st.Page("upload_page.py", title="Upload")
tasks_page = st.Page("tasks_page.py", title="Tasks")
settings_page = st.Page("settings_page.py", title="Settings")

# Navigation setup
selected_page = st.navigation({
    "Home": home_page,
    "Upload": upload_page,
    "Tasks": tasks_page,
    "Settings": settings_page,
})

# Display content based on selected page
if selected_page is home_page:
    st.title("Home")
    # Add content for Home page
elif selected_page is upload_page:
    st.title("Upload")
    # Add content for Upload page
    # ...
# ... (similarly for other pages)