import streamlit as st 

def main():
    st.title("Streamlit App")
    st.subheader("Hello Streamlit")

    # Docs
    # st.help(st.form)

    with st.form(key="myform",clear_on_submit=True):
        firstname = st.text_input("FirstName")
        lastname = st.text_input("LastName")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.info("Results")
        result = firstname + lastname + '@gmail.com'
        st.write(result)

if __name__ == '__main__':
    main()








