from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    features: list[float] = Field(min_length=3, max_length=3)

class PredictResponse(BaseModel):
    prediction: float