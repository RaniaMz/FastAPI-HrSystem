import os

from fastapi import FastAPI, Depends
from starlette.datastructures import CommaSeparatedStrings
from starlette.middleware.cors import CORSMiddleware
from app.api import user, candidate, utils
from dotenv import dotenv_values
from app.utils.auth import has_access
from app.db.mongodb_utils import connect_to_mongo, close_mongo_connection

app = FastAPI(title="User Candidate System API", )
config = dotenv_values(".env")

ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))

PROTECTED = [Depends(has_access)]

# include all routes
app.include_router(utils.router)
app.include_router(user.router)
app.include_router(candidate.router, dependencies=PROTECTED)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect_to_mongo)
app.add_event_handler("shutdown", close_mongo_connection)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)
