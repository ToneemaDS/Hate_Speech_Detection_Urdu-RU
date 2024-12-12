# Refined Prompt Template for Classification
PROMPT_TEMPLATE = """
You are an AI designed to classify comments for hate speech detection in Urdu and Roman Urdu languages. Your task is to classify comments as either "Toxic" or "Non-Toxic". Toxic comments are hateful, harmful, or offensive, and are labeled as 1. Non-Toxic comments are neutral or polite, and are labeled as 0.

Analyze the comment below and determine its label:
Comment: {comment}

Please respond with the label only (1 for Toxic or 0 for Non-Toxic).
"""
