# Load Packages
import streamlit as st 
import pandas as pd 

def main():
    st.title("Streamlit Forms & Salary Calculator")
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Forms Tutorial")

        # Salary Calculator
        # Combine forms + columns
        with st.form(key='salaryform'):
            col1,col2,col3 = st.columns([3,2,1])

            with col1:
                amount = st.number_input("Hourly Rate in $")
            
            with col2:
                hours_per_week = st.number_input("Hours Per Week",1,120)
                
            with col3:
                st.text("Salary")
                submit_salary = st.form_submit_button(label="Calculate")
        
        if submit_salary:
            with st.expander("Results"):
                daily = [amount * 8]
                weekly = [amount * hours_per_week]
                df = pd.DataFrame({'hourly':amount,'daily_8hrs':daily,'weekly':weekly})
                st.dataframe(df.T)



        # Method 1: Context Manager Approach (with)
        with st.form(key="form1"):
            firstname = st.text_input("Firstname")
            lastname = st.text_input("lastname")
            dob = st.date_input("Date of Birth")

            # Important
            submit_button = st.form_submit_button(label="Signup") #Submit is the default word

        if submit_button:
            st.success("Hello {}, you have created an account".format(firstname))

        # Method 2: 
        form2 = st.form(key='form2')
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Job",["DA","DS","DI"])
        submit_button2 = form2.form_submit_button("Login")

        if submit_button2:
            st.success("Hello {}, you are logged in".format(username))

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()