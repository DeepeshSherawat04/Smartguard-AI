from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from preprocess import load_and_preprocess
from sklearn.ensemble import RandomForestClassifier

DATA_PATH = "dataset/health_data.csv"

X, y, _ = load_and_preprocess(DATA_PATH)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, max_depth=6)
model.fit(X_train, y_train)

preds = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, preds))
print(classification_report(y_test, preds))
