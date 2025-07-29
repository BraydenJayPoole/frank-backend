# References: 4.1. API Specification (Versioning)
# This router aggregates all endpoint routers for version 1 of the API.
from fastapi import APIRouter

from .endpoints import auth

api_router = APIRouter()

# Include the authentication router
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Other endpoint routers (invoices, banking, etc.) will be included here as they are built.
