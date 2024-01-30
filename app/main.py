from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.routers import user

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

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
