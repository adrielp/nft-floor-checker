import requests
import json


from typing import Optional
from fastapi import FastAPI
# find a way to use requests and json from fastapi instead of having to import separately
#from fastapi import requests, get, json
from pydantic import BaseModel


app = FastAPI()

class Collection(BaseModel):
    """
    This is a class that simply extends the BaseModel pydantic class intaking
    the common name value.
    """
    name: str

"""
Setup a put request for the FastAPI application to get the collection stats
"""
@app.put("/collection/{collection}/stats")

async def get_collection_stats(collection_name: str) -> dict:
    """
    This function takes in the collection name from the API, makes an API outbound
    to another API endpoint, and returns the information based on that request.
    """
    url: str = f"https://api.opensea.io/api/v1/collection/{collection_name}/stats"
    headers: dict = {"Accept": "application/json"}
    resp  = requests.get(url, headers=headers)
    data: dict = resp.json()
    parsed_data = process_data(collection_name, data)
    return {"OpenSea Collection Data": parsed_data}

"""
Setup a put request for the FastAPI application to retrieve collection data.
"""
@app.put("/collection/{collection}")

async def get_collection(collection_name: str) -> dict:
    """
    This function takes in the collection name from the API, makes an API outbound
    to another API endpoint, and returns the information based on that request.
    """
    url: str = f"https://api.opensea.io/api/v1/collection/{collection_name}"
    resp  = requests.get(url)
    data: dict = resp.json()
    parsed_data = process_data(collection_name, data)
    return {"OpenSea Collection Data": parsed_data}

def process_data(collection_name: str, data: dict) -> dict:
    """
    This function takes in the raw response from the get_collection function
    and parses through the data, reformatting it into the necessary components.
    """
    parsed_data: dict = {
        "Collection Name": collection_name,
    }
    parsed_data |= data
    return parsed_data
