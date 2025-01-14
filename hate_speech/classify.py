from langchain_ollama import OllamaLLM as Ollama
from langchain.prompts import PromptTemplate
from hate_speech.prompts import PROMPT_TEMPLATE
import logging

def initialize_llm(config):
    try:
        llm = Ollama(
            model=config["model_name"],
            base_url=config["base_url"],
            temperature=config["temperature"],
        )
        logging.info(f"Initialized LLM with model {config['model_name']}.")
        return llm
    except Exception as e:
        logging.error(f"Error initializing LLM: {e}")
        raise

def classify_comment(comment, llm, prompt_template):
    try:
        prompt = prompt_template.format(comment=comment)
        response = llm.invoke(prompt).strip()
        if "1" in response:
            return 1
        else: 
            return 0
        # else:
        #     logging.warning(f"Unexpected response: {response}")
        #     return 0  # Default to 0 for invalid responses
    except Exception as e:
        logging.error(f"Error during classification: {e}")
        return 0  # Default to 0 on error

