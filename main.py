import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world!*
""")
 
df = pd.read_csv("shopping_trends.csv")
selected_columns=['Age']
bar_chart_data = df[selected_columns]
st.bar_chart(bar_chart_data)
