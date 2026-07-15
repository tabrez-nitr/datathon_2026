from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def check_server():
    return {"message": "Server is running"}
    
