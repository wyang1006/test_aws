import streamlit as st




# Database connection function
conn = st.connection("postgresql", type="sql",autocommit =True)




# Streamlit UI
st.title("PostgreSQL Data with Dask")

selected_month = st.selectbox("select",['April 2023','October 2023','April 2024','October 2024'])
Selected_route =st.selectbox("select",['100','22','103','3'])
query = f"SELECT * FROM otp WHERE \"routeShortName\" = '{Selected_route}' AND \"month\" = '{selected_month}' LIMIT 100;"
df = conn.query(query, ttl="10m")


st.write("First 10 rows:")
st.dataframe(df.head(10))
