import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from preprocess import load_and_preprocess

DATA_PATH = "dataset/health_data.csv"

def train_model():
    X, y, scaler = load_and_preprocess(DATA_PATH)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=6,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Save model & scaler
    joblib.dump(model, "../app/models/disease_model.pkl")
    joblib.dump(scaler, "../app/models/scaler.pkl")

    print("✅ Model and scaler saved successfully")

if __name__ == "__main__":
    train_model()
