import logging
import os

def setup_logger():
    os.makedirs("outputs", exist_ok=True)
    log_file_path = "outputs/pipeline.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger("PokemonPipeline")