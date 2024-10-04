import streamlit as st
from streamlit_extras.dataframe_explorer import dataframe_explorer
import streamlit_extras as stx
import random
import pandas as pd

def main():
    st.title("Two Column Sesson State Practice")
    menu = ["Home", "About"]
    random_number = random.randint(1, 50)
    choice = st.sidebar.selectbox("Menu", menu)

    filtered_df = None

    def apply_filters(df, filters):
        # Apply filters based on the user's selections
        filtered_df = df.copy()

        for column, value in filters.items():
            filtered_df = filtered_df[filtered_df[column] == value]

        return filtered_df

    if choice == "Home":
        st.subheader("Two Column Sesson State Practice")

        col1, col2 = st.columns(2)

        with col1:
            adult_train = pd.read_csv("uw data/adult_train.csv")
            display = adult_train.dtypes
            # st.write(display)
            if st.button("Random Number Button"):

                st.session_state.test1_results = adult_train  # Store results in session state

            if st.button("Hot Random Button"):
                st.write(random_number)

            with st.container():  # Create a fixed container for the results
                if "test1_results" in st.session_state:
                    st.dataframe(st.session_state.test1_results, use_container_width=True)

                    if st.button("Apply Filters"):
                        filters = {}
                        # Collect user's filter selections
                        for column in adult_train.columns:
                            value = st.text_input(f"Filter {column}:")
                            if value:
                                filters[column] = value

                        filtered_df = apply_filters(st.session_state.test1_results, filters)

        with col2:
            if st.button("Press"):
                st.session_state.test2_results = f"{random_number} + 'is a random number'"   # Store results in session state

            with st.container():  # Create a fixed container for the results
                if "test2_results" in st.session_state:
                    st.write(st.session_state.test2_results)

        # Display the filtered DataFrame after applying filters
        if filtered_df is not None:
            st.dataframe(filtered_df, use_container_width=True)

    else:
        st.subheader("About")


if __name__ == '__main__':
    main()