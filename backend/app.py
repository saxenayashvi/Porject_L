import logging
from fastapi import FastAPI
from .routers import reports

logging.basicConfig(level=logging.INFO)
app = FastAPI(title="bi4bi API")
app.include_router(reports.router, prefix="/reports", tags=["reports"])