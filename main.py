import json, os
import requests

from fastapi import FastAPI

import weaviate
from weaviate.embedded import EmbeddedOptions

from fastapi.middleware.cors import CORSMiddleware

def init_weaviate():
    app.weaviate_client = weaviate.Client(
        embedded_options=EmbeddedOptions(port=6666)
        
    )

def init_app():
  print("Initiating weaviateumesh")
  init_weaviate()
  print("Done Initiating weaviate")

  # Allow all origins  yes Umesh
  app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

app = FastAPI()
init_app()

@app.get("/")
def hello_world():
    return {"Hello": "World"}
