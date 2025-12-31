from fastapi import APIRouter
from typing import List
from app.core.schemas import BusinessMetric

router = APIRouter()

@router.post("/metrics/ingest")
def ingest_metrics(metrics: List[BusinessMetric]):
    return {
        "message": "Metrics recieved successfully",
        "rows_recieved": len(metrics)
    }