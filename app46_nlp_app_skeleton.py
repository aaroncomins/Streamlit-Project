# Core Packages
import streamlit as st

# Additional Packages


# Fxns


def main():
    st.title("NLP App with Streamlit")
    menu = ["Home", "NLP(files)", "About"]

    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Home":
        st.subheader("Home: Analyze Text")
        raw_text = st.text_area("Enter Text Here")
        num_of_most_common = st.sidebar.number_input("Most Common Tokens",5,15)
        if st.button("Analyze"):

            with st.expander("Original Text"):
                st.write(raw_text)

            with st.expander("Text Analysis"):
                st.write(raw_text) 
            
            with st.expander("Entities"):
                st.write(raw_text)

            
            # Layouts
                col1,col2 = st.columns(2)

            with col1:
                with st.expander("Word Stats"):
                    pass
                st.divider()
                with st.expander("Top Keywords"):
                    pass
                st.divider()        
                with st.expander("Sentiment"):
                    pass

            with col2:
                with st.expander("Plot Word Freq"):
                    pass
                st.divider()
                with st.expander("Plot Part of Speech"):
                    pass
                st.divider()
                with st.expander("Plot wordcloud"):
                    pass            

            with st.expanders("Download Text Analysis Results"):
                pass

        
    elif choice == "NLP(files)":
        st.subheader("NLP Task")

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()