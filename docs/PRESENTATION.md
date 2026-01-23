# AI Health Predictor: Diabetes Risk Assessment Tool
## Project Presentation

---

## 1. Executive Summary

**AI Health Predictor** is a web-based machine learning application that predicts the probability of diabetes risk based on clinical health metrics. The tool provides healthcare practitioners and individuals with a quick, data-driven risk assessment using the Pima Indians Diabetes Dataset.

### Key Highlights:
- ✅ **Deployed Web Application** built with Streamlit
- ✅ **3 ML Models Evaluated** (Logistic Regression, Random Forest, Neural Network)
- ✅ **High Accuracy** (~76% validation/test accuracy)
- ✅ **Simple User Interface** with 8 clinical input fields
- ✅ **Production-Ready Deployment** on Streamlit Cloud via GitHub

---

## 2. Problem Statement

### The Challenge
- Diabetes is a significant global health concern
- Early risk detection can enable preventive intervention
- Healthcare professionals need fast, data-driven decision support tools
- Existing tools are either overly complex or lack transparency

### The Solution
Build a lightweight, interpretable ML tool that:
- Accepts basic clinical measurements (glucose, BMI, age, etc.)
- Predicts diabetes probability with high accuracy
- Provides clear risk messaging
- Is accessible and deployable at scale

---

## 3. Dataset Overview

**Pima Indians Diabetes Dataset**
- **Size:** 768 samples with complete data
- **Features:** 8 clinical parameters
  - Pregnancies
  - Glucose level
  - Blood pressure
  - Skin thickness
  - Insulin level
  - BMI (Body Mass Index)
  - Diabetes Pedigree Function
  - Age

- **Target:** Binary outcome (diabetes: Yes/No)
- **Data Split:** 70% train / 15% validation / 15% test (stratified by outcome)

---

## 4. Methodology

### Data Preparation
1. **Loading & Exploration**
   - Inspected missing values and class balance
   - Analyzed feature distributions

2. **Feature Scaling**
   - Applied `StandardScaler` for models requiring normalization
   - Logistic Regression & Neural Network: scaled features
   - Random Forest: raw features (tree-based model)

3. **Train/Validation/Test Split**
   - Stratified split to maintain class balance across all sets
   - Enables robust evaluation on unseen data

### Model Development

#### Model 1: Logistic Regression
- **Type:** Linear baseline model
- **Features:** Scaled
- **Validation Accuracy:** ~73%
- **Rationale:** Interpretable baseline; fast training and inference

#### Model 2: Random Forest
- **Type:** Ensemble learning (100 decision trees)
- **Features:** Raw (no scaling required)
- **Validation Accuracy:** ~76%
- **Rationale:** Captures non-linear patterns; robust to outliers; **SELECTED FOR PRODUCTION**

#### Model 3: Neural Network (Keras)
- **Architecture:** Feed-forward network
  - Input layer: 8 features
  - Hidden layer 1: 16 neurons (ReLU)
  - Hidden layer 2: 8 neurons (ReLU)
  - Output layer: 1 neuron (Sigmoid)
- **Test Accuracy:** ~76%
- **Rationale:** Deep learning approach; similar performance to RF but higher complexity

### Model Selection
✅ **Random Forest chosen for production** because:
- Matches Neural Network performance (76%)
- Simpler deployment (scikit-learn)
- Faster training and inference
- More interpretable and maintainable
- No TensorFlow dependency overhead

---

## 5. Application Architecture

### Technology Stack
- **Framework:** Streamlit (Python web framework)
- **ML Framework:** scikit-learn (Random Forest)
- **Serialization:** joblib (model & scaler persistence)
- **Deployment:** Streamlit Cloud + GitHub

### Application Flow

```
User Input (8 clinical metrics)
         ↓
Streamlit UI
         ↓
Load Pre-trained Random Forest Model
         ↓
Generate Prediction & Probability
         ↓
Display Risk Assessment & Disclaimer
```

### User Interface Features
- **Input Fields:** 8 sliders/number inputs for clinical metrics
- **Predict Button:** Triggers inference on user data
- **Output:** 
  - Probability percentage
  - Risk category (High/Low)
  - Medical disclaimer

---

## 6. Results & Performance

### Model Comparison

| Model | Accuracy | Deployment Complexity | Inference Speed |
|-------|----------|----------------------|-----------------|
| Logistic Regression | 73% | Very Low | Very Fast |
| Random Forest | **76%** | **Low** | **Fast** |
| Neural Network | 76% | High | Medium |

### Key Metrics
- **Validation Accuracy (RF):** 76%
- **Test Accuracy (RF):** 76%
- **Inference Time:** < 10ms per prediction
- **Model Size:** ~3MB (easily deployable)

---

## 7. Deployment

### Current Setup
- **Repository:** GitHub (source code + trained models)
- **Platform:** Streamlit Cloud
- **Environment:** Reproducible via `requirements.txt`
- **Status:** Live and accessible

### Deployment Process
1. Trained models saved as `.pkl` files (Random Forest, scaler)
2. Neural Network model saved as `.keras` file
3. `requirements.txt` specifies all dependencies
4. GitHub integration with Streamlit Cloud for automatic updates

---

## 8. Key Learnings & Insights

### Technical Learnings
✓ **Environment Management**
  - Virtual environments crucial for reproducibility
  - Alignment between Jupyter kernel and project environment
  - Resolved TensorFlow installation issues

✓ **Model Selection**
  - Complexity ≠ Performance (on small tabular datasets)
  - Simpler models often better for production

✓ **Deployment**
  - Packaging ML projects with dependencies
  - Streamlit Cloud simplifies deployment
  - Model serialization is essential for reproducibility

### Data Science Insights
- Random Forest provides strong baseline without neural network overhead
- Feature scaling importance depends on algorithm type
- Train/validation/test split prevents overfitting detection

---

## 9. Future Enhancements

### Short-term
- 📊 Add additional evaluation metrics (precision, recall, ROC-AUC, confusion matrix)
- 🔄 Multi-model comparison UI (display predictions from all 3 models)
- 📈 Add feature importance visualization

### Medium-term
- 🎯 Implement threshold tuning for different risk categories
- 🔍 Add explainability features (SHAP values, feature importance)
- 📋 Model calibration improvements
- 📱 Mobile-responsive UI enhancements

### Long-term
- 💾 Database integration for tracking predictions
- 🔐 User authentication and data privacy
- 🌍 Multi-language support
- 🏥 Integration with healthcare systems/EHRs

---

## 10. Impact & Use Cases

### For Healthcare Professionals
- Quick risk assessment during patient intake
- Data-driven second opinion
- Population health screening

### For Individuals
- Personal health awareness
- Preventive health planning
- Educational tool for understanding risk factors

### For Researchers
- Benchmark for diabetes prediction models
- Open-source reference implementation
- Educational resource for ML deployment

---

## 11. Project Deliverables

✅ Trained machine learning models (3 variants)  
✅ Production-ready Streamlit web application  
✅ Complete data pipeline & preprocessing code  
✅ Jupyter notebook with data exploration & modeling  
✅ Comprehensive documentation  
✅ GitHub repository with deployment configuration  
✅ Test suite for model comparison  

---

## 12. Conclusion

The **AI Health Predictor** successfully demonstrates:
- **End-to-end ML project execution** (data → model → deployment)
- **Production-ready application** accessible to end users
- **Best practices** in model selection, deployment, and documentation
- **Real-world impact** potential in healthcare decision support

### Key Metrics
- 🎯 **76% Accuracy** on diabetes risk prediction
- 🚀 **Live Deployment** accessible via web
- 📦 **Reproducible Environment** with full dependency tracking
- 💡 **Scalable Architecture** ready for enhancements

---

## Contact & Resources

- **Repository:** [GitHub Link]
- **Live App:** [Streamlit Cloud Link]
- **Data Source:** Pima Indians Diabetes Dataset (UCI Machine Learning Repository)
- **Developer:** Odwa Manitshana

---

## Appendix: Technical Specifications

### Environment
- Python 3.9+
- TensorFlow/Keras
- scikit-learn
- Streamlit
- pandas, numpy

### File Structure
```
ai-health-predictor/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Project dependencies
├── data/
│   └── diabetes.csv               # Dataset
├── models/
│   ├── random_forest.pkl          # Production model
│   ├── scaler.pkl                 # Feature scaler
│   ├── logistic_regression.pkl    # Baseline model
│   └── diabetes_nn.keras          # Neural network model
├── notebooks/
│   └── 01_data_preparation.ipynb  # Data exploration & modeling
├── tests/
│   └── compare_app_notebook.py    # Model comparison tests
└── docs/
    ├── project_reflection.md       # Detailed reflection
    └── PRESENTATION.md             # This file
```

---

**Presented by:** Odwa Manitshana  
**Date:** January 23, 2026  
**Status:** Production Ready
