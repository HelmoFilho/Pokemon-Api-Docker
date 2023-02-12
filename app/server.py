## -- Importing External Modules -- ##
from dotenv import load_dotenv
from fastapi import FastAPI

## -- Importing Internal Modules -- ##

load_dotenv("./config/.env")

description_v1 = """
Documentation to use the api

The following functions are implemented in this api:

* Returning info about a pokemon by name or id
"""

app = FastAPI(
    title = "A simple pokemon api",
    description = description_v1,
    docs_url = None,
    redoc_url = "/docs"    
)