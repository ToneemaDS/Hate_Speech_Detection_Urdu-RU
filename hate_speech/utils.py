import pandas as pd
import logging
import yaml

# Load configuration
def load_config(config_path="config/config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

# Setup logging
def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("Logging setup complete.")

# Load dataset
def load_dataset(file_path):
    try:
        df = pd.read_excel(file_path)
        logging.info(f"Dataset loaded successfully from {file_path}.")
        return df
    except Exception as e:
        logging.error(f"Error loading dataset: {e}")
        raise
