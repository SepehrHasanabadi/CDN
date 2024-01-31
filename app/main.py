from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.v1.routers import user
from scripts.init_db import init as init_db

app = FastAPI()

# CORS (Cross-Origin Resource Sharing) middleware for handling cross-origin requests
# Adjust origins, methods, and other CORS settings based on your requirements
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers from version 1 (v1)
app.include_router(user.router, prefix="/v1", tags=["users"])

app.add_event_handler("startup", init_db)
