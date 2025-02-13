import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Fungsi untuk memuat data
def load_data():
    uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df
    return None

# Fungsi untuk menampilkan statistik deskriptif
def show_descriptive_stats(df):
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

# Fungsi untuk membuat visualisasi

def plot_correlation_matrix(df):
    st.subheader("Correlation Matrix")
    numeric_df = df.select_dtypes(include=['number'])  # Hanya kolom numerik
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

def plot_histogram(df):
    st.subheader("Histogram")
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        column = st.selectbox("Select Column for Histogram", numeric_columns)
        fig, ax = plt.subplots()
        sns.histplot(df[column], bins=20, kde=True, ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for histogram.")

def plot_boxplot(df):
    st.subheader("Boxplot")
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 0:
        column = st.selectbox("Select Column for Boxplot", numeric_columns, key='boxplot')
        fig, ax = plt.subplots()
        sns.boxplot(y=df[column], ax=ax)
        st.pyplot(fig)
    else:
        st.write("No numeric columns available for boxplot.")

def plot_scatter(df):
    st.subheader("Scatter Plot")
    numeric_columns = df.select_dtypes(include=['number']).columns
    if len(numeric_columns) > 1:
        x_col = st.selectbox("Select X Column", numeric_columns, key='scatter_x')
        y_col = st.selectbox("Select Y Column", numeric_columns, key='scatter_y')
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)
    else:
        st.write("Not enough numeric columns available for scatter plot.")

def plot_pairplot(df):
    st.subheader("Pairplot")
    numeric_df = df.select_dtypes(include=['number'])
    if len(numeric_df.columns) > 1:
        st.write("Displaying pairplot for first 5 numerical columns")
        selected_columns = numeric_df.iloc[:, :5]
        fig = sns.pairplot(selected_columns)
        st.pyplot(fig)
    else:
        st.write("Not enough numeric columns available for pairplot.")

# Streamlit UI
st.title("Data Visualization and Descriptive Statistics")

df = load_data()
if df is not None:
    st.write("Data Loaded Successfully!")
    show_descriptive_stats(df)
    
    # Menampilkan visualisasi
    plot_correlation_matrix(df)
    plot_histogram(df)
    plot_boxplot(df)
    plot_scatter(df)
    plot_pairplot(df)
else:
    st.write("Please upload a CSV file to proceed.")