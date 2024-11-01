from pydantic import BaseModel, HttpUrl


class AddCountrySchema(BaseModel):
    name: str
    url: str


class AddCitySchema(BaseModel):
    name: str
    url: str
    country_id: int

