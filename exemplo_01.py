import requests
from pydantic import BaseModel

class PokemonSchame(BaseModel): #Contrato de dados, schema de dados, a view da minha API
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int) -> PokemonSchame:
    response = requests.get(f"https://pokeapi.co/api/v2/______/{id}")
    data = response.json()
    data_types = data['types']  
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchame(name=data['name'], types=types)

if __name__ == "__main__":
    print (pegar_pokemon(10))
    print (pegar_pokemon(6))
    print (pegar_pokemon(13))