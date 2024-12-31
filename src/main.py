from fastapi import FastAPI
from api.endpoints import generated_endpoints
import uvicorn

app = FastAPI(
    title="API-Architect Generated API",
    description="Automatically generated API endpoints",
    version="1.0.0"
)

# Include generated routes
app.include_router(generated_endpoints.router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
