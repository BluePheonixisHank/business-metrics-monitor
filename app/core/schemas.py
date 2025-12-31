from pydantic import BaseModel
from datetime import datetime

class BusinessMetric(BaseModel):
    timestamp: datetime
    region: str
    product: str
    revenue: float
    active_users: int