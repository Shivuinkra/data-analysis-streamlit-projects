import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("Smart Data Analyzer")
st.write("Upload a dataset and perform statistics, probability, and similarity analysis")

# Upload file
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)

    # Show dataset preview
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Numeric columns
    numeric_columns = df.select_dtypes(include=['number']).columns

    if len(numeric_columns) > 0:
        # Select numeric column
        selected_column = st.selectbox("Select Numeric Column", numeric_columns)

        # Statistics
        st.subheader("Statistical Summary")

        mean_value = df[selected_column].mean()
        median_value = df[selected_column].median()
        std_value = df[selected_column].std()
        min_value = df[selected_column].min()
        max_value = df[selected_column].max()

        st.write(f"Mean: {mean_value}")
        st.write(f"Median: {median_value}")
        st.write(f"Standard Deviation: {std_value}")
        st.write(f"Minimum Value: {min_value}")
        st.write(f"Maximum Value: {max_value}")

        # Histogram
        st.subheader("Histogram")
        fig, ax = plt.subplots()
        ax.hist(df[selected_column], bins=10, color='lightblue', edgecolor='black')
        ax.set_title(f"Distribution of {selected_column}")
        ax.set_xlabel(selected_column)
        ax.set_ylabel("Frequency")
        st.pyplot(fig)

        # Probability Section
        st.subheader("Probability Analysis")

        lower_value = st.number_input("Enter Lower Range", value=float(min_value))
        upper_value = st.number_input("Enter Upper Range", value=float(max_value))

        filtered_data = df[(df[selected_column] >= lower_value) & (df[selected_column] <= upper_value)]

        probability = len(filtered_data) / len(df)

        st.write(f"Probability of values between {lower_value} and {upper_value}: {probability:.2f}")

        # Row Similarity
        st.subheader("Row Similarity Using Dot Product")

        row1 = st.number_input("Enter First Row Index", min_value=0, max_value=len(df)-1, value=0)
        row2 = st.number_input("Enter Second Row Index", min_value=0, max_value=len(df)-1, value=1)

        vector1 = df.loc[row1, numeric_columns].values
        vector2 = df.loc[row2, numeric_columns].values

        similarity = np.dot(vector1, vector2)

        st.write(f"Dot Product Similarity between Row {row1} and Row {row2}: {similarity}")

        # Comparison Chart
        st.subheader("Visual Comparison of Rows")

        comparison_df = pd.DataFrame({
            'Column': numeric_columns,
            'Row 1': vector1,
            'Row 2': vector2
        })

        fig2, ax2 = plt.subplots()
        x = np.arange(len(numeric_columns))
        width = 0.35

        ax2.bar(x - width/2, vector1, width, label='Row 1')
        ax2.bar(x + width/2, vector2, width, label='Row 2')

        ax2.set_xticks(x)
        ax2.set_xticklabels(numeric_columns, rotation=45)
        ax2.set_title("Row Comparison")
        ax2.legend()

        st.pyplot(fig2)

        # Insights
        st.subheader("Insights")

        if mean_value > median_value:
            st.write("The data is slightly right-skewed.")
        elif mean_value < median_value:
            st.write("The data is slightly left-skewed.")
        else:
            st.write("The data appears symmetric.")

        st.write(f"The probability for the selected range is {probability:.2f}.")
        st.write(f"The similarity score between the selected rows is {similarity}.")

    else:
        st.write("No numeric columns found in the dataset.")