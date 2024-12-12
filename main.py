import logging
from hate_speech.utils import load_config, setup_logging, load_dataset
from hate_speech.classify import initialize_llm, classify_comment
from hate_speech.batch_processor import process_in_batches
from hate_speech.evaluation import evaluate_model
from langchain.prompts import PromptTemplate
from hate_speech.prompts import PROMPT_TEMPLATE

def main():
    # Load configuration
    config = load_config()
    
    # Setup logging
    setup_logging(config["LOG_FILE"])
    logging.info("Starting hate speech classification...")

    # Load dataset
    df = load_dataset(config["DATASET_PATH"])

    # Initialize LLM
    llm = initialize_llm(config)
    prompt_template = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["comment"])

    # Classify Roman Urdu comments
    logging.info("Classifying Roman Urdu comments...")
    df["predicted_label_roman_urdu"] = process_in_batches(
        df, "Comment", classify_comment, llm, prompt_template, config["batch_size"]
    )

    # Classify Urdu comments
    logging.info("Classifying Urdu comments...")
    df["predicted_label_urdu"] = process_in_batches(
        df, "Urdu", classify_comment, llm, prompt_template, config["batch_size"]
    )

    # Evaluate results
    logging.info("Evaluating Roman Urdu predictions...")
    roman_metrics = evaluate_model(df["Toxic"], df["predicted_label_roman_urdu"], "Roman Urdu")
    
    logging.info("Evaluating Urdu predictions...")
    urdu_metrics = evaluate_model(df["Toxic"], df["predicted_label_urdu"], "Urdu")
    logging.info(f"DataFrame shape before saving: {df.shape}")

    # Save results
    output_path = config["OUTPUT_PATH"]
    df.to_csv(output_path, index=False)
    logging.info(f"Results saved to {output_path}")

if __name__ == "__main__":
    main()


 
