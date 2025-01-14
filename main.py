# import logging
# from hate_speech.utils import load_config, setup_logging, load_dataset
# from hate_speech.classify import initialize_llm, classify_comment
# from hate_speech.batch_processor import process_in_batches
# from hate_speech.evaluation import evaluate_model
# from langchain.prompts import PromptTemplate
# from hate_speech.prompts import PROMPT_TEMPLATE

# def main():
#     # Load configuration
#     config = load_config()
    
#     # # Setup logging
#     # setup_logging(config["LOG_FILE"])
#     # logging.info("Starting hate speech classification...")

#     # # Load dataset
#     # df = load_dataset(config["DATASET_PATH"])

#     # # Initialize LLM
#     # llm = initialize_llm(config)
#     # prompt_template = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["comment"])

#     # # Classify Roman Urdu comments
#     # logging.info("Classifying Roman Urdu comments...")
#     # df["predicted_label_roman_urdu"] = process_in_batches(
#     #     df, "Comment", classify_comment, llm, prompt_template, config["batch_size"]
#     # )

#     # # Classify Urdu comments
#     # logging.info("Classifying Urdu comments...")
#     # df["predicted_label_urdu"] = process_in_batches(
#     #     df, "Urdu", classify_comment, llm, prompt_template, config["batch_size"]
#     # )

#     # Evaluate results
#     logging.info("Evaluating Roman Urdu predictions...")
#     roman_metrics = evaluate_model(df["Toxic"], df["predicted_label_roman_urdu"], "Roman Urdu")
    
#     logging.info("Evaluating Urdu predictions...")
#     urdu_metrics = evaluate_model(df["Toxic"], df["predicted_label_urdu"], "Urdu")
#     logging.info(f"DataFrame shape before saving: {df.shape}")

#     # Save results
#     output_path = config["OUTPUT_PATH"]
#     df.to_csv(output_path, index=False)
#     logging.info(f"Results saved to {output_path}")

# if __name__ == "__main__":
#     main()

 
import logging
from hate_speech.utils import load_config, setup_logging, load_dataset
from hate_speech.classify import initialize_llm, classify_comment
from hate_speech.evaluation import evaluate_model
from langchain.prompts import PromptTemplate
from hate_speech.prompts import PROMPT_TEMPLATE

def process_and_evaluate_in_batches(df, column_name, classify_fn, llm, prompt_template, batch_size, toxic_column):
    predictions = []
    config = load_config()
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i + batch_size]
        batch_predictions = batch[column_name].apply(classify_fn, args=(llm, prompt_template))
        predictions.extend(batch_predictions)

        # Evaluate after processing the batch
        partial_df = df.iloc[:i + batch_size].copy()
        partial_df["predicted_label"] = predictions
        metrics = evaluate_model(partial_df[toxic_column], partial_df["predicted_label"], f"{column_name} (Batch {i // batch_size + 1})")
        
        # Log the metrics
        logging.info(f"Evaluation Metrics for Batch {i // batch_size + 1} ({column_name}): {metrics}")
          # Save results
        output_path = config["OUTPUT_PATH"]
        partial_df.to_csv(output_path, index=False)
        logging.info(f"Results saved to {output_path}")
    return predictions

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

    # Process and evaluate Roman Urdu comments in batches
    logging.info("Classifying Roman Urdu comments...")
    df["predicted_label_roman_urdu"] = process_and_evaluate_in_batches(
        df, "Comment", classify_comment, llm, prompt_template, config["batch_size"], "Toxic"
    )

    # Process and evaluate Urdu comments in batches
    logging.info("Classifying Urdu comments...")
    df["predicted_label_urdu"] = process_and_evaluate_in_batches(
        df, "Urdu", classify_comment, llm, prompt_template, config["batch_size"], "Toxic"
    )

    # # Save results
    # output_path = config["OUTPUT_PATH"]
    # df.to_csv(output_path, index=False)
    # logging.info(f"Results saved to {output_path}")

if __name__ == "__main__":
    main()
