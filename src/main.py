"""neuro-bridge-platform-api-1db - AI Infrastructure Component"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"service": "neuro-bridge-platform-api-1db", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
