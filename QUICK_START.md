# Quick Start Guide

## 🚀 Get Started in 3 Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
# Windows
run.bat

# Linux/Mac
chmod +x run.sh
./run.sh

# Or directly
streamlit run app.py
```

### 3. Use the Application
- Open your browser (usually opens automatically)
- Fill in customer information in the sidebar
- Click "🔮 Predict Churn"
- View results and recommendations

## 📋 Required Files

Make sure these files are in the project root:
- ✅ `model.h5`
- ✅ `label_encoder_gender.pkl`
- ✅ `OHE.pkl`
- ✅ `scaler.pkl`

## 🎯 Key Features

- **Interactive UI**: Modern, user-friendly interface
- **Real-time Predictions**: Instant churn probability
- **Visual Analytics**: Beautiful charts and gauges
- **Actionable Insights**: Recommendations based on predictions

## ❓ Troubleshooting

**Port already in use?**
```bash
streamlit run app.py --server.port 8502
```

**Model not found?**
- Ensure all `.h5` and `.pkl` files are in the project root
- Check file names match exactly (case-sensitive)

**Import errors?**
```bash
pip install --upgrade -r requirements.txt
```

---

For detailed documentation, see [README.md](README.md)

