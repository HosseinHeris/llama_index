
"""Mongo client."""

from typing import Any, Dict, List, Optional

from llama_index.readers.base import BaseReader
from llama_index.schema import Document
from llama_index.readers.mongo import SimpleMongoReader

class AzureCosmosMongoReader(SimpleMongoReader):
    def __init__(
        self,
        user: str,
        password: str,
        server: str,
        max_docs: int = 0,
        max_idle_ms: int = 120000,
        tls: str = "true", 
        auth_mechanism: str = "SCRAM-SHA-256",
        retrywrites: str = "false",
    ) -> None:
        # Construct the MongoDB connection string using the provided information
        mongo_conn = f"mongodb+srv://{user}:{password}@{server}?tls={tls}&authMechanism={auth_mechanism}&retrywrites={retrywrites}&maxIdleTimeMS={max_idle_ms}"
        try:
            import pymongo
            from pymongo import MongoClient
        except ImportError:
            raise ImportError(
                "`pymongo` package not found, please run `pip install pymongo`"
            )
        try:
            # Use the connection string to connect to Azure Cosmos DB
            self.client = MongoClient(mongo_conn)
        except Exception as e:
            raise ValueError("Error connecting to Azure Cosmos DB: " + str(e))
        self.max_docs = max_docs