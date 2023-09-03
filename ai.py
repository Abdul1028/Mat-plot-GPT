import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Streamlit UI
st.title("Mat-Plot GPT")

# Upload CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    st.subheader("Data Preview")
    st.write(df)

    # Allow user to select a color
    color = st.color_picker("Select a color for the plot", "#FF5733")

    # Select plot type
    plot_type = st.selectbox("Select a plot type", ["Bar Plot", "Line Plot", "Box Plot", "Scatter Plot", "Pie Plot", "Violin Plot", "Histogram Plot"])

    if plot_type == "Bar Plot":
        st.subheader("Bar Plot")
        plt.figure()
        plt.bar(df.index, df.iloc[:, 1], color=color)
        plt.xticks(df.index, df.iloc[:, 0], rotation=45)
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        st.pyplot(plt)

    elif plot_type == "Line Plot":
        st.subheader("Line Plot")
        plt.figure()
        plt.plot(df.iloc[:, 0], df.iloc[:, 1], marker='o', color=color)
        plt.xlabel(df.columns[0])
        plt.ylabel(df.columns[1])
        st.pyplot(plt)

    elif plot_type == "Box Plot":
        st.subheader("Box Plot")
        plt.figure()
        plt.boxplot(df.iloc[:, 1], labels=[df.columns[1]], patch_artist=True, boxprops=dict(facecolor=color))
        plt.ylabel(df.columns[1])
        st.pyplot(plt)

    elif plot_type == "Scatter Plot":
        st.subheader("Scatter Plot")
        x_axis = st.selectbox("Select X-axis column", df.columns)
        y_axis = st.selectbox("Select Y-axis column", df.columns)
        plt.figure()
        plt.scatter(df[x_axis], df[y_axis], color=color)
        plt.xlabel(x_axis)
        plt.ylabel(y_axis)
        st.pyplot(plt)

    elif plot_type == "Pie Plot":
        st.subheader("Pie Plot")
        pie_column = st.selectbox("Select column for the pie chart", df.columns)
        pie_data = df[pie_column].value_counts()
        plt.figure()
        plt.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%', colors=[color])
        plt.axis('equal')
        st.pyplot(plt)

    elif plot_type == "Violin Plot":
        st.subheader("Violin Plot")
        x_axis = st.selectbox("Select X-axis column", df.columns)
        y_axis = st.selectbox("Select Y-axis column", df.columns)
        plt.figure()
        plt.violinplot(df[y_axis], vert=False, showmedians=True, showextrema=True, widths=0.7, patch_artist=True, bw_method=0.2)
        plt.xlabel(y_axis)
        st.pyplot(plt)

    elif plot_type == "Histogram Plot":
        st.subheader("Histogram Plot")
        column = st.selectbox("Select a column for the histogram", df.columns)
        plt.figure()
        plt.hist(df[column], bins='auto', color=color, alpha=0.7, rwidth=0.85)
        plt.xlabel(column)
        plt.ylabel("Frequency")
        st.pyplot(plt)
