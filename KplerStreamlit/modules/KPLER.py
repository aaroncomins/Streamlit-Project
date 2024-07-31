import pandas as pd 
# from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import streamlit as st



def eda(data):
    st.title("Snapshot of the first five rows of KPLER Data and row count")
    df = pd.read_csv(data)
    st.write(df.head())
    st.write(len(df))
    st.title("Describe")
    st.subheader("Provides a quick overview of the central tendency, dispersion, and shape of a dataset’s distribution, excluding NaN values.")
    st.subheader("It generates descriptive statistics that summarize the sample, providing insights into the distribution of the data.")
    st.write(df.describe())

    st.title('Nunique')
    st.subheader("Returns the number of unique values for each column in the DataFrame.")
    st.subheader("This can be useful for understanding the diversity of data within each column, which can inform decisions about data cleaning, feature engineering, and model training.")
    st.write(df.nunique())

    st.title("Columns")
    st.subheader("All the available columns in the dataset")
    # Convert DataFrame columns to a list and display
    st.write(df.columns.to_list())

    st.title("Info")
    st.subheader("Provides a concise summary of a DataFrame's structure and information.")
    # Display additional information about the DataFrame
    info_text = """
    DataFrame Info:
    - Total Columns: {}
    - Total Rows: {}
    - Memory Usage: {:.2f} MB
    """.format(len(df.columns), len(df.index), df.memory_usage(deep=True).sum() / (1024 * 1024))
    st.text(info_text)

    st.title("Value count and location of Last Ports")
    st.write(df['LAST_PORT'].value_counts())

    st.title("Value count and location of Current Ports")
    st.write(df['CURRENT_PORT'].value_counts())

    st.title("Value count and location of Next Ports")
    st.write(df['NEXT_PORT_NAME'].value_counts())

    st.title("Type name of each vessel")
    st.write(df['TYPE_NAME'].value_counts())

    st.title("AIS Type Summary of each vessel")
    st.write(df['AIS_TYPE_SUMMARY'].value_counts())

    st.title("Destination of each vessel")
    st.write(df['DESTINATION'].value_counts())

    st.title("Rows of Ro-Ro/Container Carriers")
    filtered_df = df[df['TYPE_NAME'] == 'Ro-Ro/Container Carrier']
    st.write(filtered_df)

    st.title("Rows of Chinese flagged ships going to the US")
    flag_next_port_df = df.loc[(df['FLAG'] == 'CH') & (df['NEXT_PORT_COUNTRY'] == 'US')]
    st.write(flag_next_port_df)

    st.title("List of locations that Chinese flagged ships are going")
    icemask = df[df['FLAG'] == 'CH']
    st.write(icemask['NEXT_PORT_COUNTRY'].value_counts())

    # Create a histogram of the FLAG column with white bars
    plt.hist(df['FLAG'], color='white')

    # Add a title to the histogram
    plt.title('Histogram of Vessel Flags', color='white')

    # Set the color of the x-axis tick labels to white
    plt.xticks(color='white')

    # Set the color of the y-axis tick labels to white
    plt.yticks(color='white')

    # Save the plot to a file
    plt.savefig("histogram.png")

    # Clear the Matplotlib inline backend to prevent plots from stacking
    plt.clf()

    st.title("Histogram of Vessel Flags")
    # Display the image in Streamlit
    st.image("histogram.png")