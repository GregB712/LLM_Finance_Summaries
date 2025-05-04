import re

# @st.cache_data
def preprocess_text(text):
    if not text:
        return ""
    text = re.sub(r"<.*?>", "", text)  # remove HTML tags
    text = re.sub(r"\s+", " ", text) # normalize whitespace
    text = re.sub(r"\[[^]]*\]", "", text)  # remove [references]
    text = re.sub(r"\([^)]*\)", "", text)  # remove (comments)
    text = re.sub(r"http\S+", "", text)    # remove URLs
    return text.strip()