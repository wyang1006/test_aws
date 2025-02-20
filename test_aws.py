import streamlit as st
import dask.dataframe as dd
import psycopg2

import pandas as pd

# Database connection function
@st.cache_data
def load_data(query):
    conn = psycopg2.connect(
        dbname="miamicoa",
        user="postgres",
        password="19871228@Zy",
        host="localhost",
        port="5432"
    )
    df = pd.read_sql(query, conn)  # Load using Pandas
    conn.close()
    ddf = dd.from_pandas(df, npartitions=4)  # Convert to Dask DataFrame
    return ddf

# Streamlit UI
st.title("PostgreSQL Data with Dask")

selected_month = st.selectbox("select",['April 2023','October 2023','April 2024','October 2024'])
Selected_route =st.selectbox("select",['100','22','103','3'])
query = f"SELECT * FROM otp WHERE \"routeShortName\" = '{Selected_route}' AND \"month\" = '{selected_month}';"

data = load_data(query)
st.write("First 10 rows:")
st.dataframe(data.compute().head(10))

