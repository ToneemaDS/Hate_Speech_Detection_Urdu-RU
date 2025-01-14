# # 
# 
# 
# ### Prompt Template1 ####

PROMPT_TEMPLATE = """Classify the following comment as Toxic(1) or non Toxic (0) {comment}"""

# 

# ### Prompt Template2 ###
# PROMPT_TEMPLATE = """
# You are an advanced AI trained to detect hate speech in comments written in Urdu and Roman Urdu. Hate speech includes any harmful, hateful, or offensive language that targets individuals or groups based on their race, religion, ethnicity, gender, or other characteristics. This includes:

# - **Harassment:** Insults, threats, or slurs targeting specific people or communities.
# - **Offensive Language:** Profanities, harmful stereotypes, or dehumanizing language.
# - **Incitement to Violence or Discrimination:** Encouraging harm or exclusion of individuals or groups.

# Your task is to label the following comment:
# - **Toxic (1):** If the comment contains hate speech, as defined above.
# - **Non-Toxic (0):** If the comment is neutral, polite, or constructive.

# **Comment**: {comment}

# Please provide only the label (`1` for Toxic, `0` for Non-Toxic).
# """

# 
# ### Prompt Template3 ###

# PROMPT_TEMPLATE = """
# Your task is to classify the following comment as either Toxic (1) or Non-Toxic (0). Toxic comments are harmful and critical to detect. Misclassifying them as Non-Toxic can result in harm, harassment, or exclusion. 

# **Toxic (1):**
# - Language intended to harm, insult, or provoke.
# - Encourages violence, spreads misinformation, or dehumanizes others.

# **Non-Toxic (0):**
# - Comments that are neutral, polite, or lack hateful intent.

# **Comment**: {comment}

# Respond only with `1` for Toxic or `0` for Non-Toxic.
# """

###Prompt Template4 ###

# PROMPT_TEMPLATE = """
# Detect hate speech in the comment below. Label the comment as:

# - Toxic (1): Harmful, hateful, or offensive (e.g., slurs, harassment, incitement to violence).
# - Non-Toxic (0): Neutral, polite, or lacking hateful intent.

# Do not ignore subtle toxicity. If the comment shows harmful intent, label it as `1`.

# Comment: {comment}

# Respond only with `1` for Toxic or `0` for Non-Toxic.
# """

###Prompt Template5 ###

# PROMPT_TEMPLATE = """
# Classify the comment below as either:
# - 1 (toxic): Hateful, harmful, abusive, insulting, demeaning, disgusting,hurting, discriminating or offensive.
# - 0 (non-toxic): Neutral, loving, admiring, pleasing, or polite.

# Comment: {comment}

# Respond only with `1` or `0`.
# """


##################Few Shot Prompt##########

# PROMPT_TEMPLATE = """
# You are an advanced AI trained to classify comments as either toxic or non-toxic. 

# Classify the comment below based on the following criteria:
# - **1 (toxic)**: Hateful, harmful, abusive, insulting, demeaning, disgusting, hurtful, discriminating, or offensive.
# - **0 (non-toxic)**: Neutral, loving, admiring, pleasing, polite, or non-offensive.

# Here are some examples for reference:

# **Example 1:**
# Comment: Lambi nakh wali acha howa ab ni ati ha boha bad ikhlak
# Toxic: 1

# **Example 2:**
# Comment: Par sabse Pehle apna WhatsApp number send karo main tumhare saath baat karna chahata hoon
# Toxic: 0

# **Example 3:**
# Comment: Esko pani daboo kar 3 minat rakha jaye khud pata chal jaye ga k mrta ha k nhi
# Toxic: 1

# **Example 4:**
# Comment: Bhai intro audio kyu change kar diya!??????
# Toxic: 0

# Now classify the following comment:

# **Comment**: {comment}

# Respond only with `1` or `0`.
# """

