from fastapi import Request
from app.ml.model import MLModel

def get_model(request: Request) -> MLModel:
    return request.app.state.model