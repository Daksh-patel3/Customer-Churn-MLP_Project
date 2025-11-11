"""
Customer Churn Prediction Application
A modern Streamlit app for predicting customer churn using Deep Learning.
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from typing import Dict
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from config import (
    APP_TITLE,
    APP_ICON,
    PAGE_LAYOUT,
    PRIMARY_COLOR,
    SUCCESS_COLOR,
    WARNING_COLOR,
    DANGER_COLOR,
    CHURN_THRESHOLD,
    INPUT_RANGES
)
from utils import get_model_loader

# Page configuration
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout=PAGE_LAYOUT,
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f77b4;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #1565c0;
    }
    .prediction-result {
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 2rem;
    }
    .churn-high {
        background-color: #ffebee;
        border: 2px solid #e74c3c;
    }
    .churn-low {
        background-color: #e8f5e9;
        border: 2px solid #2ecc71;
    }
    </style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    """Load the model with caching."""
    try:
        return get_model_loader()
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()


def create_probability_gauge(probability: float) -> go.Figure:
    """Create a gauge chart for churn probability."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probability * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Churn Probability (%)"},
        delta={'reference': 50},
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 100], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=40, b=20),
        paper_bgcolor="white",
        font={'color': "darkblue", 'family': "Arial"}
    )
    return fig


def create_probability_bar(probability: float) -> go.Figure:
    """Create a horizontal bar chart for churn probability."""
    colors = [DANGER_COLOR if probability > CHURN_THRESHOLD else SUCCESS_COLOR]
    fig = go.Figure(go.Bar(
        x=[probability * 100],
        y=['Churn Risk'],
        orientation='h',
        marker=dict(color=colors),
        text=[f"{probability * 100:.2f}%"],
        textposition='inside',
        textfont=dict(size=20, color='white')
    ))
    fig.update_layout(
        xaxis=dict(range=[0, 100], title="Probability (%)"),
        yaxis=dict(visible=False),
        height=150,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )
    return fig


def main():
    """Main application function."""
    # Header
    st.markdown(f'<h1 class="main-header">{APP_ICON} {APP_TITLE}</h1>', unsafe_allow_html=True)
    st.markdown(
        '<p class="sub-header">Predict customer churn using advanced deep learning models</p>',
        unsafe_allow_html=True
    )
    
    # Load model
    model_loader = load_model()
    
    # Sidebar for inputs
    with st.sidebar:
        st.header("📝 Customer Information")
        st.markdown("---")
        
        # Geography
        geography = st.selectbox(
            "🌍 Geography",
            options=model_loader.one_hot_encoder.categories_[0],
            help="Select the customer's country"
        )
        
        # Gender
        gender = st.selectbox(
            "👤 Gender",
            options=model_loader.label_encoder_gender.classes_,
            help="Select the customer's gender"
        )
        
        st.markdown("---")
        
        # Age
        age = st.slider(
            "🎂 Age",
            min_value=INPUT_RANGES['age']['min'],
            max_value=INPUT_RANGES['age']['max'],
            value=INPUT_RANGES['age']['default'],
            help="Customer's age"
        )
        
        # Credit Score
        credit_score = st.slider(
            "💳 Credit Score",
            min_value=INPUT_RANGES['credit_score']['min'],
            max_value=INPUT_RANGES['credit_score']['max'],
            value=INPUT_RANGES['credit_score']['default'],
            help="Customer's credit score (300-850)"
        )
        
        st.markdown("---")
        
        # Balance
        balance = st.number_input(
            "💰 Balance",
            min_value=float(INPUT_RANGES['balance']['min']),
            max_value=float(INPUT_RANGES['balance']['max']),
            value=float(INPUT_RANGES['balance']['default']),
            step=1000.0,
            format="%.2f",
            help="Customer's account balance"
        )
        
        # Estimated Salary
        estimated_salary = st.number_input(
            "💵 Estimated Salary",
            min_value=float(INPUT_RANGES['estimated_salary']['min']),
            max_value=float(INPUT_RANGES['estimated_salary']['max']),
            value=float(INPUT_RANGES['estimated_salary']['default']),
            step=1000.0,
            format="%.2f",
            help="Customer's estimated annual salary"
        )
        
        st.markdown("---")
        
        # Tenure
        tenure = st.slider(
            "📅 Tenure (Years)",
            min_value=INPUT_RANGES['tenure']['min'],
            max_value=INPUT_RANGES['tenure']['max'],
            value=INPUT_RANGES['tenure']['default'],
            help="Number of years the customer has been with the bank"
        )
        
        # Number of Products
        num_of_products = st.slider(
            "📦 Number of Products",
            min_value=INPUT_RANGES['num_of_products']['min'],
            max_value=INPUT_RANGES['num_of_products']['max'],
            value=INPUT_RANGES['num_of_products']['default'],
            help="Number of bank products the customer uses"
        )
        
        st.markdown("---")
        
        # Has Credit Card
        has_cr_card_option = st.radio(
            "💳 Has Credit Card?",
            options=["Yes", "No"],
            help="Does the customer have a credit card?"
        )
        has_cr_card = 1 if has_cr_card_option == "Yes" else 0
        
        # Is Active Member
        is_active_member_option = st.radio(
            "✅ Is Active Member?",
            options=["Yes", "No"],
            help="Is the customer an active member?"
        )
        is_active_member = 1 if is_active_member_option == "Yes" else 0
        
        st.markdown("---")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📊 Prediction Results")
        
        # Prepare input data
        input_data: Dict = {
            'geography': geography,
            'gender': gender,
            'age': age,
            'credit_score': credit_score,
            'balance': balance,
            'estimated_salary': estimated_salary,
            'tenure': tenure,
            'num_of_products': num_of_products,
            'has_cr_card': has_cr_card,
            'is_active_member': is_active_member
        }
        
        # Predict button
        if st.button("🔮 Predict Churn", type="primary", use_container_width=True):
            with st.spinner("Analyzing customer data..."):
                try:
                    probability, will_churn = model_loader.predict(input_data)
                    
                    # Display results
                    st.markdown("---")
                    
                    # Probability gauge
                    st.subheader("Churn Probability")
                    fig_gauge = create_probability_gauge(probability)
                    st.plotly_chart(fig_gauge, use_container_width=True)
                    
                    # Probability bar
                    fig_bar = create_probability_bar(probability)
                    st.plotly_chart(fig_bar, use_container_width=True)
                    
                    # Result message
                    result_class = "churn-high" if will_churn else "churn-low"
                    result_icon = "⚠️" if will_churn else "✅"
                    result_text = "HIGH RISK - Customer is likely to churn" if will_churn else "LOW RISK - Customer is unlikely to churn"
                    result_color = DANGER_COLOR if will_churn else SUCCESS_COLOR
                    
                    st.markdown(
                        f"""
                        <div class="prediction-result {result_class}">
                            <h2 style="color: {result_color}; margin-bottom: 1rem;">
                                {result_icon} {result_text}
                            </h2>
                            <h3 style="color: {result_color}; font-size: 2.5rem; margin: 0;">
                                {probability * 100:.2f}%
                            </h3>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # Recommendations
                    st.markdown("---")
                    st.subheader("💡 Recommendations")
                    
                    if will_churn:
                        st.warning("""
                        **Action Required:**
                        - Consider offering retention incentives
                        - Schedule a customer success call
                        - Review customer satisfaction metrics
                        - Offer personalized product recommendations
                        - Provide exclusive offers or discounts
                        """)
                    else:
                        st.success("""
                        **Customer Status:**
                        - Customer shows low churn risk
                        - Continue providing excellent service
                        - Consider upselling opportunities
                        - Maintain regular engagement
                        """)
                    
                except Exception as e:
                    st.error(f"An error occurred during prediction: {str(e)}")
                    st.exception(e)
    
    with col2:
        st.header("📈 Customer Summary")
        st.markdown("---")
        
        # Display input summary
        st.metric("Age", f"{age} years")
        st.metric("Credit Score", f"{credit_score}")
        st.metric("Balance", f"${balance:,.2f}")
        st.metric("Salary", f"${estimated_salary:,.2f}")
        st.metric("Tenure", f"{tenure} years")
        st.metric("Products", f"{num_of_products}")
        
        st.markdown("---")
        
        # Additional info
        info_dict = {
            "Geography": geography,
            "Gender": gender,
            "Credit Card": "Yes" if has_cr_card else "No",
            "Active Member": "Yes" if is_active_member else "No"
        }
        
        for key, value in info_dict.items():
            st.text(f"{key}: {value}")
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #666; padding: 2rem;'>
            <p>Built with ❤️ using Streamlit and TensorFlow</p>
            <p>Customer Churn Prediction System v1.0</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
