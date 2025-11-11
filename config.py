"""
Configuration file for the Customer Churn Prediction application.
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent

# Model and preprocessor paths
MODEL_PATH = BASE_DIR / 'model.h5'
LABEL_ENCODER_GENDER_PATH = BASE_DIR / 'label_encoder_gender.pkl'
ONE_HOT_ENCODER_PATH = BASE_DIR / 'OHE.pkl'
SCALER_PATH = BASE_DIR / 'scaler.pkl'

# App configuration
APP_TITLE = "Customer Churn Prediction"
APP_ICON = "📊"
PAGE_LAYOUT = "wide"

# UI Configuration
PRIMARY_COLOR = "#1f77b4"
SUCCESS_COLOR = "#2ecc71"
WARNING_COLOR = "#f39c12"
DANGER_COLOR = "#e74c3c"

# Churn threshold
CHURN_THRESHOLD = 0.5

# Input validation ranges
INPUT_RANGES = {
    'age': {'min': 18, 'max': 100, 'default': 40},
    'credit_score': {'min': 300, 'max': 850, 'default': 650},
    'balance': {'min': 0, 'max': 250000, 'default': 0},
    'estimated_salary': {'min': 0, 'max': 200000, 'default': 50000},
    'tenure': {'min': 0, 'max': 10, 'default': 5},
    'num_of_products': {'min': 1, 'max': 4, 'default': 1}
}

