from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name:int
    type:str

    class Config:
        orm_mode = True
