import requests
import os
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv("base_url") #Buscando a url base da API

def get_pokemon_list(log):
    #Buscando lista inicial dos pokemons
    log.info("Buscando a lista de pokemons...")
    response = requests.get(f"{base_url}pokemon?limit=100&offset=0")
    data = response.json()
    pokemon_list = data["results"]
    
    #Verificando se tivemos sucesso em buscar a lista consultando a API
    if response.status_code==200:
        return pokemon_list
    log.error(f"Falha ao buscar lista de pokemons por API, erro: {response.status_code}")
    return []


def extract_pokemon_data(pokemon_list,log):
    #Buscando informações de cada pokemon
    pokemon_details = []
    log.info("Buscando dados de cada pokemon...")
    for pokemon in pokemon_list:
        try:
            pokemon_name = pokemon["name"]
            details_response = requests.get(f"{base_url}pokemon/{pokemon_name}") 
            details = details_response.json()
            if details:
                pokemon_details.append({
                    "ID": details["id"],
                    "Nome": details["name"].title(),
                    "Experiência Base": details["base_experience"],
                    "Tipos": [t["type"]["name"].title() for t in details["types"]],
                    "HP": details["stats"][0]["base_stat"],
                    "Ataque": details["stats"][1]["base_stat"],
                    "Defesa": details["stats"][2]["base_stat"]
                })
        except Exception as e:
            log.info(f"Erro: {e}, ao consultar o pokemon {pokemon_name}")
    log.info("Extracao de dados concluida")
    return pokemon_details