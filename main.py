import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
from geopy.geocoders import Nominatim
import geopy


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
top_categories = df.groupby('Category')['Purchase Amount (USD)'].sum().nlargest(5)  # Select top 5 categories

# Streamlit App
st.title("Top Categories - Pie Chart")

# Create a pie chart using Matplotlib
fig, ax = plt.subplots()
ax.pie(top_categories, labels=top_categories.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax.set_title("Top Categories Distribution")
st.pyplot(fig)

color_counts = df['Payment Method'].value_counts()

# Streamlit App
st.title("Donut Chart - Payment Method Distribution")

# Create a donut chart using Matplotlib
fig, ax = plt.subplots()
ax.pie(color_counts, labels=color_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.3))
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Add a white circle in the center to create the donut effect
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

ax.set_title("Donut Chart - Payment Method Distribution")
st.pyplot(fig)

# Streamlit App
st.title("Bubble Plot - Age vs Purchase Amount vs Review Rating")

# Assuming 'Age', 'Purchase Amount (USD)', and 'Review Rating' are columns in your dataset
fig, ax = plt.subplots()

# Scatter plot with bubbles
scatter = ax.scatter(
    df['Age'],
    df['Purchase Amount (USD)'],
    c=df['Review Rating'],
    cmap='viridis',  # You can choose a different colormap
    s=df['Review Rating'] * 20,  # Adjust the size of the bubbles based on 'Review Rating'
    alpha=0.7,
    edgecolors="w",
    linewidths=0.5,
)

# Add colorbar
cbar = plt.colorbar(scatter)
cbar.set_label('Review Rating')

# Set labels and title
ax.set_xlabel('Age')
ax.set_ylabel('Purchase Amount (USD)')
ax.set_title('Bubble Plot - Age vs Purchase Amount vs Review Rating')

# Show the plot in Streamlit
st.pyplot(fig)



st.title("Age Distribution Boxplot")
# Display the boxplot using matplotlib
fig, ax = plt.subplots()
ax.boxplot(df['Age'])
ax.set_xlabel("Age")
ax.set_ylabel("Distribution")
ax.set_title("Boxplot - Age Distribution")

# Show the plot in Streamlit
st.pyplot(fig)


df['Date'] = pd.to_datetime(df['Date']).dt.date  # Extract only the date component

# Streamlit App
st.title("Trends in Purchase Amount over Date")

# Create a line chart using Matplotlib
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Purchase Amount (USD)'], marker='o', linestyle='-')

# Set labels and title
ax.set_xlabel("Date")
ax.set_ylabel("Purchase Amount (USD)")
ax.set_title("Trends in Purchase Amount over Date")

# Show the plot in Streamlit
st.pyplot(fig)


df['Date'] = pd.to_datetime(df['Date']).dt.date  # Extract only the date component

# Streamlit App
st.title("Frequency of Purchases over Time")

# Create a line chart using Matplotlib
fig, ax = plt.subplots()
ax.plot(df['Date'], df['Frequency of Purchases'], marker='o', linestyle='-')

# Set labels and title
ax.set_xlabel("Date")
ax.set_ylabel("Frequency of Purchases")
ax.set_title("Frequency of Purchases over Time")

# Show the plot in Streamlit
st.pyplot(fig)



  
