import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your new CSV
df = pd.read_csv(r"C:\Users\Khushi Singh\Desktop\FlyOrDie-ai\data\flight_sample_2022-09-01.csv.csv")

X = df[["aircraft_age", "weather_score", "delay_rate", "maintenance_flag"]]
y = df["risk_label"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model.pkl")
print("✅ Model trained and saved.")
