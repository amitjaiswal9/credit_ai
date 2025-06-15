"""Model training script."""

import pandas as pd
from joblib import dump
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

from .feature_engineering import prepare_features


def train_model(data_path: str, model_path: str = "model.pkl"):
    """Load data, train a model, and save it to ``model_path``."""
    df = pd.read_csv(data_path)
    df = prepare_features(df)
    X = df.drop("target", axis=1)
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    print(classification_report(y_test, preds))
    dump(model, model_path)
    return model


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python -m ml_model.model_training <data_path> [model_path]")
    model_file = sys.argv[2] if len(sys.argv) > 2 else "model.pkl"
    train_model(sys.argv[1], model_file)
