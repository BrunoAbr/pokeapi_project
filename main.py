#Importando os módulos
from data_extraction import extract_pokemon_data, get_pokemon_list 
from data_transformation import transform_pokemon_data, get_top_pokemon, calculate_statistics
from report_generation import chart_type
from log import setup_logger

def main():
    #Iniciando os registro de logs para caso a pipeline apresente algum erro.
    log = setup_logger()
    try:
        log.info("Iniciando pipeline Pokemon data...")
        #Passo 1: realizando a extração de dados
        pokemon_list = get_pokemon_list(log)  
        pokemon_details = extract_pokemon_data(pokemon_list, log)

        #Passo 2: transformação de dados
        df, types_df, types_counts = transform_pokemon_data(pokemon_details)
        top_pokemon = get_top_pokemon(df)
        status_avarege = calculate_statistics(types_df)

        #passo 3: gerando gráficos
        chart_type(types_counts, status_avarege, top_pokemon, log)

        log.info("Pipeline executada com sucesso!")
    except Exception as e:
        log.error(f"Erro na pipeline: {e}")

if __name__ == "__main__":
    main()