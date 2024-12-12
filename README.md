# Hate Speech Classification Project

This project is designed to classify hate speech in text data (Roman Urdu and Urdu) using a large language model (LLM). The project processes datasets in batches, performs classification using a pre-trained model, evaluates predictions, and stores results in a CSV file.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Setup](#setup)
4. [Modules](#modules)
5. [Running the Project](#running-the-project)
6. [Results](#results)
7. [Contributing](#contributing)

---

## Overview

Hate speech detection is crucial in moderating online content. This project leverages the `Ollama` LLM to classify comments into toxic and non-toxic categories. The project supports batch processing and evaluates model performance using metrics like accuracy.

---

## Project Structure

Thesis2/ ├── Dataset/ │ └── purutt.xlsx # Input dataset ├── Results/ │ └── classified_comments.csv # Output results ├── hate_speech/ │ ├── init.py # Package initialization │ ├── batch_processor.py # Batch processing logic │ ├── classify.py # Model initialization and classification │ ├── evaluation.py # Evaluation metrics │ ├── prompts.py # LLM prompts │ └── utils.py # Utility functions (config, logging, etc.) ├── config/ │ └── config.yaml # Configuration file ├── logs/ │ └── app.log # Log file ├── main.py # Main script for execution ├── README.md # Project documentation └── requirements.txt # Python dependencies


---

## Setup

### Clone the Repository

```bash
git clone <repository_url>
cd Thesis2

### Create a virtual environment

python -m venv hate_speech_env
source hate_speech_env/bin/activate   
# On Windows: hate_speech_env\Scripts\activate


