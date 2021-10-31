# Basic Packages and Skleaarn For modeling
import pandas as pd
import numpy as np
import time
import pickle

# pycaret packages
import pycaret
from pycaret import classification as clscaret
from pycaret import regression as regcaret
from pycaret.utils import check_metric


import tempfile
import os
import asyncio
import uvicorn
from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import HTMLResponse
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import List

from fastapi.middleware.cors import CORSMiddleware
from mlmodel import MlMain


app = FastAPI()
origins = ["http://localhost", "http://localhost:4200", "*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserMLInput(BaseModel):
    automl:str
    user_id: str
    experiment_id: str

@app.post("/diamondpred/automl/")
async def MLInference(user_input:UserMLInput):
    m = MlMain("regression")
    output = m.mlmain()
    return(output)