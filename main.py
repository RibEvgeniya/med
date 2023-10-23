from fastapi import FastAPI
from api.handlers.clients import clients_router

app = FastAPI()

app.include_router(clients_router, prefix="/clients", tags=["clients"])