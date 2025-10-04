import matplotlib.pyplot as plt
import os

def chart_type(types_counts, status_average, top_pokemon, log):
    log.info("Gerando relatorios...")

    #Verificando se já existe a pasta outputs
    os.makedirs("outputs", exist_ok=True)
    
    plt.figure(figsize=(10,6))
    types_counts.plot(kind="bar")
    plt.title("Quantidade de pokemons por tipo")
    plt.xlabel("Tipos")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    #Salvando os gráficos
    log.info("Exportando dados...")
    plt.savefig("outputs/grafico.png")
    plt.close()

    status_average.to_csv("outputs/mean_stats.csv", index=False, float_format="%.1f")
    top_pokemon.to_csv("outputs/relatorio_top_5_pokemon.csv", index=False, encoding="utf-8")

    files = [
        "outputs/grafico.png",
        "outputs/mean_stats.csv",
        "outputs/relatorio_top_5_pokemon.csv"
    ]

    for file in files:
        if os.path.exists(file):
            log.info(f"✅ Arquivo criado: {file}")
        else:
            log.warning(f"⚠️ Arquivo não criado {file}")

    log.info("Geracao de relatorios concluido!")


    