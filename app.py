import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🌾 Crop Recommendation System")
st.markdown("---")
st.write("Get personalized crop recommendations based on soil and environmental conditions.")

# Load the model
try:
    model = joblib.load('crop_recommendation.joblib')
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Soil Properties")
    nitrogen = st.slider(
        "Nitrogen (N) in soil",
        min_value=0,
        max_value=140,
        value=50,
        step=1,
        help="Nitrogen content in ppm"
    )
    
    phosphorus = st.slider(
        "Phosphorus (P) in soil",
        min_value=0,
        max_value=145,
        value=50,
        step=1,
        help="Phosphorus content in ppm"
    )
    
    potassium = st.slider(
        "Potassium (K) in soil",
        min_value=0,
        max_value=205,
        value=50,
        step=1,
        help="Potassium content in ppm"
    )
    
    ph_value = st.slider(
        "Soil pH",
        min_value=3.5,
        max_value=9.5,
        value=6.5,
        step=0.1,
        help="Soil acidity/alkalinity (pH scale)"
    )

with col2:
    st.subheader("🌡️ Environmental Conditions")
    temperature = st.slider(
        "Temperature (°C)",
        min_value=8.0,
        max_value=44.0,
        value=25.0,
        step=0.1,
        help="Average temperature in Celsius"
    )
    
    humidity = st.slider(
        "Humidity (%)",
        min_value=14.0,
        max_value=99.0,
        value=70.0,
        step=0.5,
        help="Relative humidity percentage"
    )
    
    rainfall = st.slider(
        "Rainfall (mm)",
        min_value=20.0,
        max_value=300.0,
        value=150.0,
        step=1.0,
        help="Annual rainfall in millimeters"
    )

# Prepare input features
features = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]])

# Create prediction button
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])

with col_btn2:
    if st.button("🔍 Get Crop Recommendation", use_container_width=True):
        # Make prediction
        try:
            prediction = model.predict(features)
            recommended_crop = prediction[0]
            
            # Display result
            st.success("✅ Prediction Complete")
            st.markdown("---")
            
            # Create a nice display for the result
            col_result1, col_result2 = st.columns([1, 1])
            
            with col_result1:
                st.metric("Recommended Crop", recommended_crop.upper(), delta="✓ Best Match")
            
            with col_result2:
                # Display input summary
                st.write("**Input Summary:**")
                st.write(f"- **N-P-K:** {nitrogen}-{phosphorus}-{potassium} ppm")
                st.write(f"- **Temperature:** {temperature}°C")
                st.write(f"- **Humidity:** {humidity}%")
                st.write(f"- **Soil pH:** {ph_value}")
                st.write(f"- **Rainfall:** {rainfall} mm")
            
            # Additional information box
            st.markdown("---")
            st.info(
                f"💡 **Your soil and environmental conditions are ideal for growing {recommended_crop.upper()}.** "
                f"This recommendation is based on historical crop data and optimal growing conditions."
            )
            
        except Exception as e:
            st.error(f"Error making prediction: {e}")

# Sidebar information
with st.sidebar:
    st.header("📖 Information")
    st.write("""
    ### How it Works
    This system uses machine learning to recommend the best crop based on:
    - **Soil Properties:** N, P, K nutrients and pH level
    - **Weather:** Temperature, humidity, and rainfall
    
    ### Features:
    - Real-time predictions
    - Interactive sliders for easy adjustment
    - Based on extensive crop data
    
    ### Model Details
    - **Input Features:** 7
    - **Output:** Recommended crop type
    """)
    
    st.markdown("---")
    st.write("**Default Parameter Ranges:**")
    st.write("""
    - Nitrogen: 0-140 ppm
    - Phosphorus: 0-145 ppm
    - Potassium: 0-205 ppm
    - Temperature: 8-44°C
    - Humidity: 14-99%
    - pH: 3.5-9.5
    - Rainfall: 20-300 mm
    """)
