from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title = "Business Metrics Monitoring System",
    description="Detects and explains anomalies in business metrics",
    version="0.1.0"
)

app.include_router(router)
