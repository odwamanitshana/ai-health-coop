# AI Health Predictor: Diabetes Risk Assessment Tool

A machine learning web application that predicts the probability of diabetes risk based on clinical health metrics. Built with Streamlit and deployed on Streamlit Cloud.

## 🎯 Features

- **Interactive Web UI** - User-friendly interface for inputting clinical metrics
- **Real-time Predictions** - Instant diabetes risk probability assessment
- **Multiple Models** - Trained with Logistic Regression, Random Forest, and Neural Networks
- **Production Ready** - Deployed and accessible online
- **Open Source** - Full source code and trained models included

## 📊 Models & Performance

| Model | Accuracy | Status |
|-------|----------|--------|
| Logistic Regression | ~73% | Baseline |
| Random Forest | **~76%** | ✅ **Production** |
| Neural Network | ~76% | Experimental |

**Selected Model:** Random Forest – achieves production-level accuracy (~76%) with simpler deployment compared to the experimental neural network while maintaining strong performance

## 🚀 Quick Start

### Prerequisites
- Python 3.x (tested on 3.13)
- pip or conda

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/odwamanitshana/ai-health-predictor.git
   cd ai-health-predictor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Run Locally

**Launch the Streamlit app:**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📋 Usage

1. Enter 8 clinical metrics:
   - Pregnancies (count)
   - Glucose level (mg/dL)
   - Blood Pressure (mmHg)
   - Skin Thickness (mm)
   - Insulin level (mIU/mL)
   - BMI (kg/m²)
   - Diabetes Pedigree Function
   - Age (years)

2. Click **"Predict"** button

3. View results:
   - Diabetes probability (percentage)
   - Risk message based on the probability
   - Medical disclaimer

## 📁 Project Structure

```
ai-health-predictor/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── data/
│   └── diabetes.csv               # Pima Indians Diabetes Dataset (768 samples)
├── models/
│   ├── random_forest.pkl          # Production model
│   ├── scaler.pkl                 # Feature scaler
│   ├── logistic_regression.pkl    # Baseline model
│   └── diabetes_nn.keras          # Neural network model
├── notebooks/
│   └── 01_data_preparation.ipynb  # Data exploration & model training
├── tests/
│   └── compare_app_notebook.py    # Model comparison tests
└── docs/
    ├── project_reflection.md       # Detailed project reflection
    └── PRESENTATION.md             # Full presentation slides
```

## 🔍 Dataset

**Source:** Pima Indians Diabetes Dataset  
**Samples:** 768  
**Features:** 8 clinical measurements  
**Target:** Binary (Diabetes: Yes/No)  
**Split:** 70% train / 15% validation / 15% test

## 🛠️ Data Pipeline

1. **Loading & Exploration**
   - Inspected missing values and class balance
   - Analyzed feature distributions

2. **Feature Scaling**
   - Applied StandardScaler for Logistic Regression & Neural Network
   - Raw features for Random Forest

3. **Train/Validation/Test Split**
   - Stratified split to maintain class balance

## 📦 Dependencies

Key packages:
- **streamlit** - Web application framework
- **scikit-learn** - Machine learning models
- **tensorflow/keras** - Deep learning framework (for the experimental neural network model)
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **joblib** - Model serialization

See `requirements.txt` for complete list.

## 🌐 Deployment

The app is deployed on **Streamlit Cloud** and connected to this GitHub repository.

**Live App:** [AI Health Predictor on Streamlit Cloud](https://ai-health-predictor-i8szxik9c7k6sgeilydpui.streamlit.app/)

### Deploying Your Own Version

1. Push code to GitHub
2. Visit [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repo
4. Select this repository and `app.py` as the main file
5. Deploy!

## 📈 Model Training

To retrain models with new data:

1. Update `data/diabetes.csv`
2. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebooks/01_data_preparation.ipynb
   ```
3. Models will be saved to `models/`
4. Redeploy the app

## ⚠️ Important Disclaimer

This tool is for **educational and research purposes only**. It is **not** a substitute for professional medical advice, diagnosis, or treatment. Always consult with healthcare professionals for medical decisions.

## 🔮 Future Enhancements

- [ ] Add additional evaluation metrics (precision, recall, ROC-AUC)
- [ ] Multi-model comparison in UI
- [ ] Feature importance visualization
- [ ] Model calibration improvements
- [ ] Explainability features (SHAP values)
- [ ] Threshold tuning for risk categories
- [ ] Database integration for prediction tracking
- [ ] Mobile-responsive UI improvements

## 📝 Model Comparison Test

Run the test suite to compare all models:

```bash
python tests/compare_app_notebook.py
```

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing bugs, improving documentation, or adding new features, your help is appreciated.

### Getting Started

1. **Fork the repository**
   - Click the "Fork" button at the top right of this repository
   - This creates your own copy of the project

2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/ai-health-coop.git
   cd ai-health-coop
   ```

3. **Set up the development environment**
   ```bash
   # Create and activate virtual environment
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   
   # Install dependencies
   pip install -r requirements.txt
   ```

4. **Create a new branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

### Making Changes

1. **Make your changes**
   - Write clear, concise code
   - Follow existing code style and conventions
   - Add comments where necessary

2. **Test your changes**
   ```bash
   # Run the app locally
   streamlit run app.py
   
   # Run tests if available
   python tests/compare_app_notebook.py
   ```

3. **Commit your changes**
   ```bash
   git add .
   git commit -m "Clear description of your changes"
   ```
   
   **Commit Message Guidelines:**
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
   - Reference issue numbers if applicable

### Submitting Changes

1. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request**
   - Go to the original repository on GitHub
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill in the PR template with:
     - Clear description of changes
     - Related issue numbers
     - Screenshots (if UI changes)
     - Testing performed

3. **Wait for review**
   - Maintainers will review your PR
   - Address any requested changes
   - Once approved, your PR will be merged!

### Contribution Guidelines

**Code Quality:**
- Write clean, readable code
- Follow Python PEP 8 style guidelines
- Add docstrings to functions and classes
- Keep functions focused and modular

**Documentation:**
- Update README.md if you change functionality
- Comment complex logic
- Update requirements.txt if adding dependencies

**Testing:**
- Test your changes thoroughly
- Ensure existing functionality still works
- Add tests for new features when possible

**Types of Contributions:**
- 🐛 Bug fixes
- ✨ New features
- 📝 Documentation improvements
- 🎨 UI/UX enhancements
- ⚡ Performance improvements
- 🧪 Adding tests
- 🔧 Configuration improvements

### Getting Help

- 💬 Join discussions in the Issues section
- 📧 Reach out to maintainers for questions
- 📖 Check existing documentation and code examples

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help create a welcoming environment for all contributors

Thank you for contributing to AI Health Predictor! 🎉

## 📚 Documentation

- [Project Reflection](docs/project_reflection.md) - Detailed technical reflection
- [Full Presentation](docs/PRESENTATION.md) - Complete presentation slides
- [Jupyter Notebook](notebooks/01_data_preparation.ipynb) - Data exploration & modeling walkthrough

## 📄 License

This project is open source. Please refer to LICENSE file for details.

## 👤 Author

**Odwa Manitshana**  
Email: odwa.manitshana20@gmail.com

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Review the Jupyter notebook for implementation details

## 🎓 Learning Resources

This project demonstrates:
- End-to-end machine learning pipeline
- Model selection and evaluation
- Streamlit web application development
- Model deployment and cloud hosting
- Data preprocessing and scaling
- Ensemble vs. deep learning methods

---

**Last Updated:** January 23, 2026  
**Status:** Production Ready ✅
