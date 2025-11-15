from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Sample data: [difficulty, hash_rate, previous_success_rate]
# Labels: 0 (Low success), 1 (High success)
X = np.array([
    [4, 1000, 0.6],
    [5, 1100, 0.4],
    [6, 1200, 0.5],
    [4, 1050, 0.7],
])
y = np.array([1, 0, 0, 1])

model = RandomForestClassifier()
model.fit(X, y)

def predict_success(difficulty, hash_rate, success_rate):
    prediction = model.predict([[difficulty, hash_rate, success_rate]])
    return "High Success" if prediction[0] == 1 else "Low Success"

if __name__ == "__main__":
    difficulty = 4
    hash_rate = 1050
    success_rate = 0.7

    prediction = predict_success(difficulty, hash_rate, success_rate)
    print(f"AI Prediction: {prediction}")
