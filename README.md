# Projeto PokeData

A ideia desse projeto com foco em Python para extração, transformação e geração de relatórios utilizando a [PokeAPI](https://pokeapi.co/) é é coletar dados de 100 Pokémon e modelar os dados para relatórios e insights.

---

##  Objetivo
Criar uma pipeline de dados que:
1. **Extrai** informações sobre Pokémons via API;
2. **Transforma** e analisa os dados coletados;
3. **Gera relatórios e gráficos** com estatísticas dos Pokémons.

---

##  Estrutura do Projeto
```
projeto_pokeapi/
│
├── data_extraction.py # Extração de dados da API
├── data_transformation.py # Limpeza e análise dos dados
├── report_generation.py # Geração de gráficos e relatórios
├── log.py # Configuração de logs
├── main.py # Script principal da pipeline
├── .env # Variáveis de ambiente
├── requirements.txt # Dependências do projeto
└── outputs/ # Saída dos arquivos gerados
```
---
## Tecnologias Utilizadas

- **Python 3.x**: Motor principal do projeto.

- **Requests**: Utilizando para consumir às APIs(PokeAPI).

- **Matplotlib**: Para gerar grafico e visualização dos relatórios.

- **Pandas**: Para manipulação e transformação dos dados.

- **Dotenv**: Carrregar às variaveis de ambiente.

- **logging**: Para registrar os logs do processo.
---
## Como Executar

### 1- Clonar o repositório

```bash
git clone https://github.com/BrunoAbr/pokeapi_project.git
cd pokemon-pipeline
```
## Docker
Este projeto é executado via Doceker

### 2 - Construindo imagem docker
No diretório raiz do projeto, execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t pokeapi_project .
```

### 3 - Rodando o Contêiner Docker

Após a construir a imagem, rodaremos o contêiner com:
```bash
docker run --rm -v $(pwd)/outputs:/app/outputs pokeapi_project
```
Dessa forma rodará o projeto dentro do contêiner, automaticamente instalando as dependências e executando o script.

### Concluído.

## Observação
O .env desse projeto ficará visível por não conter dados sensíveis.

## Autor
**Bruno Abreu**
[LinkedIn](https://www.linkedin.com/in/bruno-abreu-102291225/)
