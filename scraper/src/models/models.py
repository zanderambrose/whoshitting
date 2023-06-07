from typing import List 

from pydantic import BaseModel, Field


class Artist(BaseModel):
    name: str = Field(...)
    instrument: str = Field(...)


class VenueSchema(BaseModel):
    venu_name: str = Field(...)
    band_name: str = Field(...)
    sideman: List[Artist]

