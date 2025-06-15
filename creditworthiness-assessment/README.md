# Creditworthiness Assessment Application

This application is a modular framework for assessing creditworthiness using
machine learning models, policy rules, and external integrations.

## Directory Structure

- `chatbot/` – chatbot interface code
- `data/` – sample data for development
- `integrations/` – APIs for external services
- `ml_model/` – feature engineering and model training scripts
- `rule_engine/` – policy rules definitions
- `explainability/` – tools for model explainability
- `utils/` – utility functions such as logging
- `app.py` – entry point for the application
- `requirements.txt` – Python dependencies

## Quickstart

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train the example model using the sample dataset:
   ```bash
   python -m ml_model.model_training data/sample_data/sample.csv model.pkl
   ```
3. Run the application and check a customer's eligibility:
   ```bash
   python app.py 12345
   ```
