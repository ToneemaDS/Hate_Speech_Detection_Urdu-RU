import logging
from concurrent.futures import ThreadPoolExecutor

def process_batch(batch, column_name, classify_fn, llm, prompt_template):
    return batch[column_name].apply(classify_fn, args=(llm, prompt_template))

def process_in_batches(df, column_name, classify_fn, llm, prompt_template, batch_size):
    predictions = []

    with ThreadPoolExecutor() as executor:
        futures = []
        for i in range(0, len(df), batch_size):
            batch = df.iloc[i:i + batch_size]
            future = executor.submit(process_batch, batch, column_name, classify_fn, llm, prompt_template)
            futures.append(future)
        
        for i, future in enumerate(futures):
            try:
                batch_predictions = future.result()
                predictions.extend(batch_predictions)
                logging.info(f"Processed batch {i + 1}/{len(futures)}")
            except Exception as e:
                logging.error(f"Error processing batch {i + 1}: {e}")
                # Handle or skip the batch in case of errors

    return predictions
