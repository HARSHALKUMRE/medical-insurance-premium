from dataclasses import dataclass
from datetime import datetime
import pymongo
import json
import os, sys

TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

@dataclass
class EnvironmentVariable:
    """
    Because it allow us to declare a class without
    writing a __init__ function.
    """
    mongo_db_url = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
TARGET_COLUMN = "expenses"
print("env_var, mongo_db_url")