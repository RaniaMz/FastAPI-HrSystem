from fastapi import FastAPI
from api.user import router as user_router
from api.candidate import router as candidate_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(candidate_router, prefix="/candidates", tags=["candidates"])


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def read_health():
    return {"status": "OK"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
