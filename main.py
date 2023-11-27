import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from geopy.geocoders import Nominatim

file_path = "shopping_trends.csv" 
df = pd.read_csv(file_path)


# Streamlit App
st.title("Customer Shopping Trends Dashboard")

# Gender Distribution
st.subheader("Gender Distribution")
gender_counts = df['Gender'].value_counts()
st.bar_chart(gender_counts)

# Category-wise Sales
st.subheader("Category-wise Sales")
category_counts = df['Category'].value_counts()
st.bar_chart(category_counts)

# Season-wise Sales
st.subheader("Season-wise Sales")
season_counts = df['Season'].value_counts()
st.bar_chart(season_counts)

# Subscription Status Distribution
st.subheader("Subscription Status Distribution")
subscription_counts = df['Subscription Status'].value_counts()
st.bar_chart(subscription_counts)

# Payment Method Distribution
st.subheader("Payment Method Distribution")
payment_counts = df['Payment Method'].value_counts()
st.bar_chart(payment_counts)

# Shipping Type Distribution
st.subheader("Shipping Type Distribution")
shipping_counts = df['Shipping Type'].value_counts()
st.bar_chart(shipping_counts)

st.title("Histogram - Age Distribution")
st.subheader("Histogram - Age Distribution")
fig, ax = plt.subplots()
ax.hist(df['Age'], bins=20,color='orange', edgecolor='black')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
st.pyplot(fig)

st.title("Histogram - Purchase Amount distribution")
st.subheader("Histogram - Purchase Amount distribution")
fig, ax = plt.subplots()
ax.hist(df['Purchase Amount (USD)'], bins=20,color='orange', edgecolor='black')
ax.set_xlabel('Purchase Amount (USD)')
ax.set_ylabel('Frequency')
st.pyplot(fig)

st.title("Histogram - Review Rating distribution")
st.subheader("Histogram - Review Rating distribution")
fig, ax = plt.subplots()
ax.hist(df['Review Rating'], bins=20,color='orange', edgecolor='black')
ax.set_xlabel('Review Rating')
ax.set_ylabel('Frequency')
st.pyplot(fig)



st.title("Scatter Plot - Age vs Purchase Amount")

# Scatter Plot for 'Age' vs 'Purchase Amount (USD)'
st.subheader("Scatter Plot - Age vs Purchase Amount")
st.scatter_chart(
    df,
    x='Age',
    y='Purchase Amount (USD)',
    color='Gender',  # Replace with an actual column for color differentiation if needed
    size=20,  # Adjust the size as needed
)

st.title("Scatter Plot - Age vs Review Rating")

# Scatter Plot for 'Age' vs 'Purchase Amount (USD)'
st.subheader("Scatter Plot - Age vs  Review Rating")
st.scatter_chart(
    df,
    x='Age',
    y='Review Rating',
    color='Category',  # Replace with an actual column for color differentiation if needed
    size=20,  # Adjust the size as needed
)

st.title("Scatter Plot - Purchase Amount (USD) vs Review Rating")

# Scatter Plot for 'Age' vs 'Purchase Amount (USD)'
st.subheader("Scatter Plot - Purchase Amount (USD) vs  Review Rating")
st.scatter_chart(
    df,
    x='Purchase Amount (USD)',
    y='Review Rating',
    color='Gender',  # Replace with an actual column for color differentiation if needed
    size=20,  # Adjust the size as needed
)

# chart = alt.Chart(df).mark_circle().encode(
#     x='Age:Q',
#     y='Purchase Amount (USD):Q',
#     color='Category:N'  # Replace 'Category' with the actual column for color differentiation
# ).properties(
#     title='Scatter Plot - Age vs Purchase Amount'
# )

# st.altair_chart(chart, use_container_width=True)
# # Box Plots

# df = df[['Location']]
   
#     columns=['lat', 'lon'])

# st.map(df)
