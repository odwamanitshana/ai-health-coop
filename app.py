import os
import joblib
import numpy as np
import streamlit as st
from tensorflow import keras

# --------------------------
# Load models with error handling
# --------------------------
MODELS_DIR = "models"

FEATURE_NAMES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age",
]

@st.cache_resource
def load_models():
    """Load all available models with error handling."""
    models = {}
    
    # Load Random Forest
    try:
        rf_path = os.path.join(MODELS_DIR, "random_forest.pkl")
        models['Random Forest'] = joblib.load(rf_path)
    except Exception as e:
        st.warning(f"Could not load Random Forest model: {e}")
    
    # Load Logistic Regression
    try:
        lr_path = os.path.join(MODELS_DIR, "logistic_regression.pkl")
        models['Logistic Regression'] = joblib.load(lr_path)
    except Exception as e:
        st.warning(f"Could not load Logistic Regression model: {e}")
    
    # Load Neural Network
    try:
        nn_path = os.path.join(MODELS_DIR, "diabetes_nn.keras")
        models['Neural Network'] = keras.models.load_model(nn_path)
    except Exception as e:
        st.warning(f"Could not load Neural Network model: {e}")
    
    # Load Scaler (for Logistic Regression and Neural Network)
    scaler = None
    try:
        scaler_path = os.path.join(MODELS_DIR, "scaler.pkl")
        scaler = joblib.load(scaler_path)
    except Exception as e:
        st.warning(f"Could not load scaler: {e}")
    
    if not models:
        st.error("No models could be loaded. Please check the models directory.")
        st.stop()
    
    return models, scaler

models, scaler = load_models()

# --------------------------
# Streamlit UI
# --------------------------
st.title("🏥 Diabetes Risk Predictor")

st.write(
    "Enter patient information below. The model will estimate the probability "
    "that this patient has diabetes based on the Pima Indians Diabetes Dataset."
)

# Model selection
st.sidebar.header("⚙️ Model Settings")
selected_model = st.sidebar.selectbox(
    "Select Model",
    options=list(models.keys()),
    index=0,
    help="Choose which machine learning model to use for prediction"
)

# Display model info
model_info = {
    'Random Forest': "Best overall performance (~76% accuracy). Does not require feature scaling.",
    'Logistic Regression': "Baseline model (~73% accuracy). Fast and interpretable.",
    'Neural Network': "Deep learning model (~76% accuracy). Experimental."
}

if selected_model in model_info:
    st.sidebar.info(f"**{selected_model}**: {model_info[selected_model]}")


col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1, step=1)
    glucose = st.number_input(
        "Glucose (mg/dL)", 
        min_value=1, 
        max_value=300, 
        value=120, 
        step=1,
        help="Blood glucose level. Must be greater than 0."
    )
    blood_pressure = st.number_input(
        "Blood Pressure (mmHg)", 
        min_value=0, 
        max_value=200, 
        value=70, 
        step=1
    )
    skin_thickness = st.number_input(
        "Skin Thickness (mm)", 
        min_value=0, 
        max_value=100, 
        value=20, 
        step=1
    )

with col2:
    insulin = st.number_input(
        "Insulin (mIU/mL)", 
        min_value=0, 
        max_value=1000, 
        value=80, 
        step=1
    )
    bmi = st.number_input(
        "BMI (kg/m²)", 
        min_value=1.0, 
        max_value=80.0, 
        value=25.0, 
        step=0.1, 
        format="%.1f",
        help="Body Mass Index. Must be greater than 0."
    )
    dpf = st.number_input(
        "Diabetes Pedigree Function", 
        min_value=0.0, 
        max_value=3.0, 
        value=0.5, 
        step=0.01, 
        format="%.2f",
        help="Genetic likelihood of diabetes based on family history"
    )
    age = st.number_input(
        "Age (years)", 
        min_value=1, 
        max_value=120, 
        value=33, 
        step=1
    )

def validate_inputs(glucose, bmi, blood_pressure, age):
    """Validate critical inputs."""
    errors = []
    
    if glucose <= 0:
        errors.append("⚠️ Glucose level must be greater than 0")
    
    if bmi <= 0:
        errors.append("⚠️ BMI must be greater than 0")
    
    if blood_pressure <= 0:
        errors.append("⚠️ Blood Pressure should be greater than 0 for accurate prediction")
    
    if age <= 0:
        errors.append("⚠️ Age must be greater than 0")
    
    return errors


if st.button("Predict", type="primary", use_container_width=True):
    # Validate inputs
    validation_errors = validate_inputs(glucose, bmi, blood_pressure, age)
    
    if validation_errors:
        for error in validation_errors:
            st.error(error)
        st.stop()
    
    # Build feature vector
    input_values = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age,
    ]

    X_input = np.array(input_values).reshape(1, -1)
    
    try:
        # Get selected model
        model = models[selected_model]
        
        # Apply scaling for models that need it
        if selected_model in ['Logistic Regression', 'Neural Network']:
            if scaler is None:
                st.error("Scaler not available. Cannot use this model.")
                st.stop()
            X_input_scaled = scaler.transform(X_input)
            X_for_prediction = X_input_scaled
        else:
            # Random Forest uses raw features
            X_for_prediction = X_input
        
        # Make prediction
        if selected_model == 'Neural Network':
            prob_diabetes = float(model.predict(X_for_prediction, verbose=0)[0][0])
            pred_class = 1 if prob_diabetes >= 0.5 else 0
        else:
            prob_diabetes = model.predict_proba(X_for_prediction)[0, 1]
            pred_class = model.predict(X_for_prediction)[0]

        # Display results with enhanced UX
        st.markdown("---")
        st.subheader("📊 Prediction Results")
        
        # Display probability with metrics
        col_metric1, col_metric2, col_metric3 = st.columns(3)
        
        with col_metric1:
            st.metric(
                label="Diabetes Probability",
                value=f"{prob_diabetes:.1%}",
                delta=f"{prob_diabetes - 0.5:.1%} from threshold" if abs(prob_diabetes - 0.5) > 0.05 else None
            )
        
        with col_metric2:
            st.metric(
                label="Risk Level",
                value="HIGH" if pred_class == 1 else "LOW"
            )
        
        with col_metric3:
            st.metric(
                label="Model Used",
                value=selected_model.split()[0]
            )
        
        # Visual probability bar
        st.write("**Risk Assessment:**")
        st.progress(prob_diabetes)
        
        # Risk interpretation
        if prob_diabetes >= 0.75:
            st.error("🔴 **Very High Risk** - Strong indication of diabetes. Immediate medical consultation recommended.")
        elif prob_diabetes >= 0.5:
            st.warning("🟡 **High Risk** - Elevated probability of diabetes. Medical evaluation advised.")
        elif prob_diabetes >= 0.25:
            st.info("🔵 **Moderate Risk** - Some indicators present. Consider lifestyle changes and monitoring.")
        else:
            st.success("🟢 **Low Risk** - Low probability of diabetes based on current metrics.")
        
        # Medical disclaimer
        st.markdown("---")
        st.caption(
            "⚕️ **Medical Disclaimer:** This tool is for educational and research purposes only. "
            "It is **NOT** a substitute for professional medical advice, diagnosis, or treatment. "
            "Always consult with qualified healthcare professionals for medical decisions."
        )
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.exception(e)