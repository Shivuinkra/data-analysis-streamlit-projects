
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Title
st.title("Data Explorer App")
st.write("Upload a CSV file and explore your dataset")

# Upload CSV file
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read dataset
    df = pd.read_csv(uploaded_file)

    # Show dataset
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Select numeric columns only
    numeric_columns = df.select_dtypes(include=['number']).columns

    if len(numeric_columns) > 0:
        selected_column = st.selectbox("Select Numeric Column", numeric_columns)

        # Calculate statistics
        mean_value = df[selected_column].mean()
        median_value = df[selected_column].median()
        mode_value = df[selected_column].mode()[0]
        std_value = df[selected_column].std()
        min_value = df[selected_column].min()
        max_value = df[selected_column].max()

        # Display statistics
        st.subheader("Statistical Summary")
        st.write(f"Mean: {mean_value}")
        st.write(f"Median: {median_value}")
        st.write(f"Mode: {mode_value}")
        st.write(f"Standard Deviation: {std_value}")
        st.write(f"Minimum Value: {min_value}")
        st.write(f"Maximum Value: {max_value}")

        # Histogram
        st.subheader("Histogram")
        fig, ax = plt.subplots()
        ax.hist(df[selected_column], bins=10, color='skyblue', edgecolor='black')
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        ax.set_title(f"Distribution of {selected_column}")
        st.pyplot(fig)

        # Insights
        st.subheader("Insights")

        if mean_value > median_value:
            st.write("The data is slightly right-skewed because mean is greater than median.")
        elif mean_value < median_value:
            st.write("The data is slightly left-skewed because mean is smaller than median.")
        else:
            st.write("The data appears to be symmetric because mean and median are almost equal.")

        st.write(f"The values range from {min_value} to {max_value}.")
        st.write(f"The standard deviation is {std_value}, which shows the spread of the data.")

    else:
        st.write("No numeric columns found in the dataset.")
