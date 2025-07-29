# References: 1.2. System Architecture & Implementation Plan
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import the main API router we just created
from .api.v1.api import api_router

# Initialize the FastAPI application
app = FastAPI(title="Frank API", openapi_url="/api/v1/openapi.json")

# Configure CORS (Cross-Origin Resource Sharing) middleware
# This is crucial for allowing the frontend (running on a different port)
# to communicate with the backend API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, this should be restricted to the frontend's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health", tags=["Health"])
async def health_check():
    """
    A simple health check endpoint to confirm the API is running.
    """
    return {"status": "ok"}

# Include the main API router. All other routes will be nested under this.
app.include_router(api_router, prefix="/api/v1")
