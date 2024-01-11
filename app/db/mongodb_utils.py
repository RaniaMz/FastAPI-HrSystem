import logging

from dotenv import dotenv_values
from motor.motor_asyncio import AsyncIOMotorClient

from .mongodb import db

# from pymongo import mongo_client, MongoClient
# import pymongo

config = dotenv_values(".env")


async def connect_to_mongo():
    logging.info("Connecting to database...")
    db.client = AsyncIOMotorClient(str(config["DB_URI"]),
                                   maxPoolSize=int(config["MAX_CONNECTIONS_COUNT"]),
                                   minPoolSize=int(config["MIN_CONNECTIONS_COUNT"]))
    logging.info("Database connected！")


async def close_mongo_connection():
    logging.info("Closing database connection...")
    db.client.close()
    logging.info("Database closed！")
