import pandas as pd

def categorize_experience(exp):
    if exp < 50:
        return "Fraco"
    elif 50 <= exp <= 100:
        return "Médio"
    else:
        return "Forte"
    
def transform_pokemon_data(pokemon_details): #Adicionando uma nova coluna "Categoria", e criando dataframe por tipo
    df = pd.DataFrame(pokemon_details)
    df["Categoria"] = df["Experiência Base"].apply(categorize_experience)
    types_df = df.explode("Tipos")
    types_counts = types_df["Tipos"].value_counts()
    return df, types_df, types_counts

def get_top_pokemon(df, n=5): #buscando os 5 pokemons com maior experiencia base
    return df.nlargest(n, "Experiência Base")

def calculate_statistics(types_df): #Calcuando a media de ataque, defesa e HP de pokemons agrupando por tipo
    status_average = types_df.groupby("Tipos")[["Ataque", "Defesa", "HP"]].mean().reset_index()
    return status_average