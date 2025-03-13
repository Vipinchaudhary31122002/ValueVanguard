import streamlit as st
import pickle
import numpy as np
import json

# Load the trained model
model = pickle.load(open('./model/model.pickle', 'rb'))

# Load column info
with open("./model/columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# Extract locations from column data
locations = data_columns[3:]  # Assuming first 3 columns are sqft, bath, bhk

# Streamlit UI
st.title("🏠 Bangalore House Price Prediction App")
st.write("Enter the details below to get an estimated house price.")

# Input fields
sqft = st.number_input("📏 Square Footage", min_value=300, max_value=10000, step=50)
bhk = st.number_input("🛏️ Number of Bedrooms", min_value=1, max_value=10, step=1)
bath = st.number_input("🛁 Number of Bathrooms", min_value=1, max_value=10, step=1)
location = st.selectbox("📍 Select Location", locations)

# Prediction function
def predict_price(location, sqft, bath, bhk):
    try:
        loc_index = data_columns.index(location)
    except ValueError:
        st.error("Location not found in model features!")
        return None
    
    x = np.zeros(len(data_columns))  # Create input array with zeros
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1  # One-hot encode location
    
    return model.predict([x])[0]

# Predict button
if st.button("💰 Predict Price"):
    price = predict_price(location, sqft, bath, bhk)
    if price is not None:
        st.success(f"🏡 Estimated House Price: ₹{price:,.2f}")