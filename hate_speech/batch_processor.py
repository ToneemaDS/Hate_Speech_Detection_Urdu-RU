import logging

def process_in_batches(df, column_name, classify_fn, llm, prompt_template, batch_size):
    predictions = []
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i + batch_size]
        batch_predictions = batch[column_name].apply(classify_fn, args=(llm, prompt_template))
        predictions.extend(batch_predictions)
        logging.info(f"Processed batch {i // batch_size + 1}/{(len(df) + batch_size - 1) // batch_size}")
    return predictions
