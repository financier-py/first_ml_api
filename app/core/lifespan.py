from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.ml.model import MLModel

@asynccontextmanager
async def lifespan(app: FastAPI):
    model = MLModel("model.joblib")
    app.state.model = model
    yield 
