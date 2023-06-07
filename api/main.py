import re
from fastapi import FastAPI
import motor.motor_asyncio

app = FastAPI()

@app.get("/")
def venue():

    return {"detail": "found"}

@app.get("/venue/{venue_name}")
def venue(venue_name: str):

    return {venue_name: "world"}
