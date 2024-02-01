from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import user
from app.api.v1.routers import file
from app.scripts.init_db import init as init_db

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

verson_1 = "/v1"

app.include_router(user.router, prefix=verson_1, tags=["users"])
app.include_router(file.router, prefix=verson_1, tags=["files"])

app.add_event_handler("startup", init_db)
