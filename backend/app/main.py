from fastapi import FastAPI

app = FastAPI(
    title="Song Journey API",
    description="API for generating musical journeys between two songs.",
    version="0.1.0"
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}