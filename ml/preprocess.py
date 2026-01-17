import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess(path: str):
    df = pd.read_csv(path)

    # Replace invalid zero values with median
    cols_with_zero = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
    for col in cols_with_zero:
        df[col] = df[col].replace(0, df[col].median())

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler
