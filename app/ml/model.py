import joblib
import numpy as np

class MLModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)
    
    def predict(self, features: list[float]) -> float:
        X = np.array(features).reshape(1, -1)
        prediction = self.model.predict(X)
        return float(prediction[0])