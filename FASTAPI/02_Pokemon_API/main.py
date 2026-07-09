# 02 Pokemon API
# This is a beginner FastAPI project.
# The goal is to learn how APIs return data.

from fastapi import FastAPI


# Create the FastAPI app.
# The app is what Uvicorn runs.
app = FastAPI(
    title="Pokemon Learning API",
    description="A beginner FastAPI project for learning REST APIs.",
    version="0.1.0",
)


# This is the home route.
# A route is a URL the API responds to.
# GET means the user is asking to read data.
@app.get("/")
def root():
    return {
        "message": "Welcome to the Pokemon Learning API!",
        "docs": "Go to /docs to test the API.",
    }


# This is a simple health check route.
# Health checks are used to see if an API is running.
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "The Pokemon API is running.",
    }