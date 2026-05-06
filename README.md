# 🌾 Crop Recommendation System

A machine learning-powered web application that recommends the most suitable crop based on soil properties and environmental conditions.

## 📋 Features

- **Real-time Predictions**: Get instant crop recommendations based on input parameters
- **Interactive Interface**: User-friendly Streamlit web app with intuitive sliders
- **Data-Driven**: Recommendations based on comprehensive crop and soil data
- **7-Parameter Analysis**: Considers nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall
- **Responsive Design**: Clean and organized layout with information sidebar

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language
- **Streamlit**: Web app framework for interactive UI
- **joblib**: Model serialization and loading
- **scikit-learn**: Machine learning library (for model training)
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing

## 📦 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone or download the repository**:
   ```bash
   git clone <repository-url>
   cd Crop_Detection_System
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install streamlit joblib scikit-learn pandas numpy
   ```

## 🚀 Usage

1. **Navigate to the project directory**:
   ```bash
   cd Crop_Detection_System
   ```

2. **Run the Streamlit app**:
   ```bash
   streamlit run app.py
   ```

3. **Open in browser**: The app will automatically open at `http://localhost:8501`

4. **Make predictions**:
   - Adjust soil property sliders (Nitrogen, Phosphorus, Potassium, pH)
   - Adjust environmental condition sliders (Temperature, Humidity, Rainfall)
   - Click "Get Crop Recommendation" button
   - View the recommended crop and analysis

## 📊 Input Parameters

| Parameter | Range | Unit | Description |
|-----------|-------|------|-------------|
| Nitrogen (N) | 0-140 | ppm | Nitrogen content in soil |
| Phosphorus (P) | 0-145 | ppm | Phosphorus content in soil |
| Potassium (K) | 0-205 | ppm | Potassium content in soil |
| Temperature | 8-44 | °C | Average temperature |
| Humidity | 14-99 | % | Relative humidity |
| Soil pH | 3.5-9.5 | - | Soil acidity/alkalinity |
| Rainfall | 20-300 | mm | Annual rainfall |

## 📁 Project Structure

```
Crop_Detection_System/
├── app.py                          # Main Streamlit application
├── crop_recommendation.joblib      # Pre-trained ML model
├── crop_recommendation.csv         # Training/reference dataset
├── crop_recomendation_system_model.ipynb  # Jupyter notebook (model development)
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
└── README.md                       # This file
```

## 🤖 Model Information

- **Type**: Supervised Learning Classification Model
- **Algorithm**: Machine Learning Classifier (trained on crop data)
- **Input Features**: 7 (N, P, K, Temperature, Humidity, pH, Rainfall)
- **Output**: Crop type recommendation
- **Training Data**: Historical crop yield data from `crop_recommendation.csv`

### Supported Crops
The model recommends from a variety of crops including rice, wheat, maize, chickpea, kidneybeans, pigeonpeas, mothbeans, mungbean, blackgram, lentil, pomegranate, banana, mango, grapes, watermelon, muskmelon, apple, orange, papaya, coconut, cotton, sugarcane, and others.

## 💡 How It Works

1. **Input Collection**: The app collects soil and environmental parameters via interactive sliders
2. **Feature Preparation**: Input values are formatted as a numerical array
3. **Model Prediction**: The pre-trained model predicts the best crop
4. **Result Display**: The recommended crop and input summary are displayed with helpful insights

## 🔧 Troubleshooting

### Model not found
- Ensure `crop_recommendation.joblib` is in the project directory
- Verify the file path in the error message

### Dependencies not installed
- Run: `pip install -r requirements.txt`
- Or: `pip install streamlit joblib scikit-learn pandas numpy`

### Port already in use
- Run Streamlit on a different port:
  ```bash
  streamlit run app.py --server.port 8502
  ```

## 📝 Data Source

The model is trained on agricultural crop data including:
- Soil nutrient levels (NPK values)
- Climate conditions (temperature, humidity, rainfall)
- Historical crop yield data
- Optimal growing conditions for various crops

## 🤝 Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes and commit them (`git commit -am 'Add improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 📄 License

This project is open source and available under the MIT License.

## 📧 Contact & Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Happy Farming! 🌱** 

Get the best crop recommendations for your land with data-driven insights.