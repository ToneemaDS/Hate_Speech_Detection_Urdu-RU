# # Refined Prompt Template for Classification
# PROMPT_TEMPLATE = """
# You are an AI designed to classify comments for hate speech detection in Urdu and Roman Urdu languages. Your task is to classify comments as either "Toxic" or "Non-Toxic". Toxic comments are hateful, harmful, or offensive, and are labeled as 1. Non-Toxic comments are neutral or polite, and are labeled as 0.

# Analyze the comment below and determine its label:
# Comment: {comment}

# Please respond with the label only (1 for Toxic or 0 for Non-Toxic).
# """
# Refined Prompt Template for Classification


PROMPT_TEMPLATE = """
You are an advanced AI trained to detect hate speech in comments written in Urdu and Roman Urdu. Hate speech includes, but is not limited to, the following:

1. **Targeted Harassment**: Insults, threats, or derogatory remarks aimed at a person or group based on their race, religion, ethnicity, gender, sexual orientation, or other characteristics.
2. **Offensive Language**: Usage of profanities, slurs, or harmful stereotypes.
3. **Incitement to Violence**: Comments encouraging physical harm, harassment, or violent acts against individuals or groups.
4. **Discrimination**: Language promoting exclusion or dehumanization of a particular community or individual.
5. **Misinformation with Harmful Intent**: Spreading false information designed to harm individuals or communities.

Your task is to classify each comment based on these criteria as either:
- **"Toxic"**: Includes any of the above characteristics and is harmful, hateful, or offensive (label as `1`).
- **"Non-Toxic"**: Neutral, polite, or constructive, lacking any hateful intent (label as `0`).

Carefully analyze the comment below and respond with the appropriate label:

**Comment**: {comment}

**Guidelines**:
- Focus on the intent and tone of the comment.
- If uncertain, default to "Non-Toxic" (0).
- Provide only the label (`1` for Toxic, `0` for Non-Toxic).

Please respond with the label only.
"""
