"""Feature engineering utilities for creditworthiness models."""

import pandas as pd

def prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    """Perform simple feature engineering on the dataset."""
    engineered = df.copy()
    # Example feature: debt to income ratio
    if {'debt', 'income'} <= set(df.columns):
        engineered['debt_to_income'] = df['debt'] / df['income'].replace({0: 1})
    return engineered
