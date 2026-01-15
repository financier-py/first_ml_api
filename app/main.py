from fastapi import FastAPI
from app.core.lifespan import lifespan
from app.api.routers import predict, health

app = FastAPI(lifespan=lifespan)

app.include_router(predict.router)
app.include_router(health.router)