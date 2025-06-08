
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

def train_model():
    # Load preprocessed data
    data = pd.read_csv('dataset/processed_train.csv')

    # Split into features (X) and labels (y)
    X = data.drop('label', axis=1)
    y = data['label']

    # Split into train and validation sets
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_val)

    # Evaluation
    print("Confusion Matrix:\n", confusion_matrix(y_val, y_pred))
    print("\nClassification Report:\n", classification_report(y_val, y_pred))
    print("Accuracy Score:", accuracy_score(y_val, y_pred))

    # Save the model
    joblib.dump(model, 'models/intrusion_model.pkl')
    print("\nModel saved to 'models/intrusion_model.pkl'.")

if __name__ == "__main__":
    train_model()
