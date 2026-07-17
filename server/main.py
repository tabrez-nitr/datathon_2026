from fastapi import FastAPI 
from app.api.v1.endpoints.router import api_router 

app = FastAPI(
    title="Crime Intelligence Platform",
    version = "1.0.0",
)
app.include_router(api_router)

@app.get("/")
def root():
    return {
        "message" : "Welcome to the Crime Intelligence Platform",
        "status" : "running"
        }


