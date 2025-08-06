from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"])

@app.get("/health")
def get_health_check():
    return {"success": True, "message": "everything is working fine."}