from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def root():
    return {
        "name" : "Crime Inelligence Platform",
        "status" : "Healthy",
        "version" : "v1.0.0"
        }
    
