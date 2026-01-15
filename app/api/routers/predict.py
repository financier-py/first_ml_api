from fastapi import APIRouter, Depends
from app.schemas.predict import PredictRequest, PredictResponse
from app.api.deps import get_model
from app.ml.model import MLModel

router = APIRouter(prefix='/predict', tags=['ml'])

@router.post("/", response_model=PredictResponse)
def predict(request: PredictRequest, model: MLModel = Depends(get_model)):
    result = model.predict(request.features)
    return PredictResponse(prediction=result)