# Customer Churn Prediction Application

A modern, interactive web application for predicting customer churn using Deep Learning (Artificial Neural Networks). Built with Streamlit and TensorFlow.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.13+-orange.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 🎯 Features

- **Interactive UI**: Modern, user-friendly interface with intuitive controls
- **Real-time Predictions**: Instant churn probability calculations
- **Visual Analytics**: Beautiful gauge charts and probability visualizations
- **Comprehensive Input**: Support for all relevant customer features
- **Actionable Insights**: Provides recommendations based on prediction results
- **Professional Design**: Clean, modern UI with responsive layout

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Features Overview](#features-overview)
- [Model Information](#model-information)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd ANN-PROJECT
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Ensure Model Files are Present

Make sure you have the following files in the project root:
- `model.h5` - Trained TensorFlow model
- `label_encoder_gender.pkl` - Gender label encoder
- `OHE.pkl` - One-hot encoder for Geography
- `scaler.pkl` - StandardScaler for feature normalization

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Using the Application

1. **Input Customer Information**: Use the sidebar to enter customer details:
   - Geography (Country)
   - Gender
   - Age
   - Credit Score
   - Account Balance
   - Estimated Salary
   - Tenure (Years with bank)
   - Number of Products
   - Credit Card Status
   - Active Member Status

2. **Get Prediction**: Click the "🔮 Predict Churn" button

3. **View Results**: 
   - See the churn probability percentage
   - View visual charts and gauges
   - Read actionable recommendations

## 📁 Project Structure

```
ANN-PROJECT/
│
├── app.py                      # Main Streamlit application
├── config.py                   # Configuration settings
├── utils.py                    # Utility functions and model loader
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── model.h5                    # Trained TensorFlow model
├── label_encoder_gender.pkl    # Gender label encoder
├── OHE.pkl                     # One-hot encoder
├── scaler.pkl                  # Feature scaler
│
├── Churn_Modelling.csv         # Dataset (for reference)
├── experiments.ipynb           # Model training notebook
├── predicion.ipynb             # Prediction notebook
│
└── logs/                       # Training logs
```

## ✨ Features Overview

### 1. Modern User Interface
- Clean, professional design
- Intuitive sidebar navigation
- Responsive layout
- Color-coded results

### 2. Interactive Visualizations
- **Gauge Chart**: Shows churn probability with visual indicators
- **Bar Chart**: Horizontal bar representation of risk level
- **Color Coding**: Green for low risk, red for high risk

### 3. Comprehensive Input System
- Sliders for numeric inputs
- Dropdowns for categorical data
- Radio buttons for binary choices
- Input validation and helpful tooltips

### 4. Actionable Insights
- Automatic risk assessment
- Personalized recommendations
- Action items for high-risk customers
- Maintenance suggestions for low-risk customers

## 🤖 Model Information

### Architecture
- **Type**: Artificial Neural Network (ANN)
- **Framework**: TensorFlow/Keras
- **Input Features**: 11 features (after encoding)
- **Output**: Binary classification (Churn/No Churn)

### Features Used
1. Credit Score
2. Geography (One-hot encoded)
3. Gender (Label encoded)
4. Age
5. Tenure
6. Balance
7. Number of Products
8. Has Credit Card
9. Is Active Member
10. Estimated Salary

### Preprocessing
- **StandardScaler**: Normalizes numeric features
- **LabelEncoder**: Encodes gender (Male/Female)
- **OneHotEncoder**: Encodes geography (France/Spain/Germany)

## ⚙️ Configuration

Configuration settings can be modified in `config.py`:

- **Model Paths**: File locations for model and preprocessors
- **UI Settings**: Colors, layout, and styling
- **Input Ranges**: Validation ranges for user inputs
- **Churn Threshold**: Probability threshold for churn classification (default: 0.5)

## 🛠️ Development

### Code Structure

- **app.py**: Main application logic and UI components
- **utils.py**: Model loading and prediction utilities
- **config.py**: Centralized configuration management

### Adding New Features

1. Modify `config.py` for new configuration options
2. Update `utils.py` for new utility functions
3. Enhance `app.py` for UI changes

## 📊 Dataset

The model was trained on a customer churn dataset containing:
- 10,000 customer records
- 13 features per customer
- Binary churn labels (Exited: 0/1)

## 🔧 Troubleshooting

### Common Issues

**Issue**: Model file not found
- **Solution**: Ensure `model.h5` and all `.pkl` files are in the project root

**Issue**: Import errors
- **Solution**: Verify all dependencies are installed: `pip install -r requirements.txt`

**Issue**: Port already in use
- **Solution**: Use a different port: `streamlit run app.py --server.port 8502`

## 📝 License

This project is licensed under the MIT License.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [TensorFlow](https://www.tensorflow.org/)
- Visualizations by [Plotly](https://plotly.com/)

---

**Made with ❤️ for Customer Retention Analytics**

