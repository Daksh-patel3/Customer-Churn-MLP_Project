"""
Utility functions for model loading and prediction.
"""
import pickle
import logging
from pathlib import Path
from typing import Dict, Tuple, Optional
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

from config import (
    MODEL_PATH,
    LABEL_ENCODER_GENDER_PATH,
    ONE_HOT_ENCODER_PATH,
    SCALER_PATH
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModelLoader:
    """Handles loading of the trained model and preprocessors."""
    
    def __init__(self):
        self.model = None
        self.label_encoder_gender = None
        self.one_hot_encoder = None
        self.scaler = None
        self._load_all()
    
    def _load_all(self) -> None:
        """Load model and all preprocessors."""
        try:
            logger.info("Loading model and preprocessors...")
            self.model = tf.keras.models.load_model(str(MODEL_PATH))
            
            with open(LABEL_ENCODER_GENDER_PATH, 'rb') as f:
                self.label_encoder_gender = pickle.load(f)
            
            with open(ONE_HOT_ENCODER_PATH, 'rb') as f:
                self.one_hot_encoder = pickle.load(f)
            
            with open(SCALER_PATH, 'rb') as f:
                self.scaler = pickle.load(f)
            
            logger.info("Successfully loaded all components")
        except FileNotFoundError as e:
            logger.error(f"Required file not found: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading model/preprocessors: {e}")
            raise
    
    def predict(self, input_data: Dict) -> Tuple[float, bool]:
        """
        Predict churn probability for given input data.
        
        Args:
            input_data: Dictionary containing customer features
            
        Returns:
            Tuple of (probability, will_churn)
        """
        try:
            # Prepare input DataFrame
            df = pd.DataFrame({
                'CreditScore': [input_data['credit_score']],
                'Gender': [self.label_encoder_gender.transform([input_data['gender']])[0]],
                'Age': [input_data['age']],
                'Tenure': [input_data['tenure']],
                'Balance': [input_data['balance']],
                'NumOfProducts': [input_data['num_of_products']],
                'HasCrCard': [input_data['has_cr_card']],
                'IsActiveMember': [input_data['is_active_member']],
                'EstimatedSalary': [input_data['estimated_salary']]
            })
            
            # One-hot encode Geography
            geo_encoded = self.one_hot_encoder.transform([[input_data['geography']]])
            geo_encoded_df = pd.DataFrame(
                geo_encoded,
                columns=self.one_hot_encoder.get_feature_names_out(['Geography'])
            )
            
            # Combine data
            df = pd.concat([df.reset_index(drop=True), geo_encoded_df], axis=1)
            
            # Scale the data
            df_scaled = self.scaler.transform(df)
            
            # Predict
            prediction = self.model.predict(df_scaled, verbose=0)
            probability = float(prediction[0][0])
            will_churn = probability > 0.5
            
            return probability, will_churn
            
        except Exception as e:
            logger.error(f"Error during prediction: {e}")
            raise


# Global model loader instance
_model_loader: Optional[ModelLoader] = None


def get_model_loader() -> ModelLoader:
    """Get or create the global model loader instance."""
    global _model_loader
    if _model_loader is None:
        _model_loader = ModelLoader()
    return _model_loader

