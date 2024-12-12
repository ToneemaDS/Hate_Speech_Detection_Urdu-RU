def process_in_batches(df, column_name, classify_fn, llm, prompt_template, batch_size, save_path):
    predictions = []
    for i in range(0, len(df), batch_size):
        batch = df.iloc[i:i + batch_size]
        batch_predictions = batch[column_name].apply(classify_fn, args=(llm, prompt_template))
        predictions.extend(batch_predictions)

        # Save intermediate results
        df.loc[i:i + batch_size - 1, "predicted_label"] = batch_predictions
        df.to_csv(save_path, index=False)
        
        logging.info(f"Processed batch {i // batch_size + 1}/{(len(df) + batch_size - 1) // batch_size} and saved checkpoint.")
    return predictions
