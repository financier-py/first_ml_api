import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

def train():
    # пока фейк данные

    X = np.array([
        [1.0, 2.0, 3.0],
        [2.0, 3.0, 4.0],
        [3.0, 4.0, 5.0],
        [4.0, 5.0, 6.0],
    ])
    y = np.array([1.0, 2.0, 3.0, 4.0])

    model = LinearRegression()
    model.fit(X, y)
    print(f"Веса модельки: {model.coef_} и отступ: {model.intercept_}")

    joblib.dump(model, "model.joblib")
    print("Model has been saved :)")

if __name__ == "__main__":
    train()