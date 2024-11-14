from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings
import uvicorn

class Settings(BaseSettings):
    app_version: str = "1.0"
    app_title: str = "FastAPI Demo Application"
    
    class Config:
        env_file = ".env"

settings = Settings()
app = FastAPI()

@app.get("/get_info")
async def get_info():
    try:
        return {
            "app_version": settings.app_version,
            "app_title": settings.app_title
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)