#!/usr/bin/python3
from models.base_model import BaseModel


""" Amenity Model """
class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
