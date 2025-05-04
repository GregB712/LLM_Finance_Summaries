import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_PATHS = {
    "facebook/bart-large-cnn": "./models/facebook-bart-large-cnn",
    # "facebook/bart-large-xsum": "./models/facebook-bart-large-xsum",
    # "google/pegasus-xsum": "./models/google-pegasus-xsum",
    # "google/pegasus-multi_news": "./models/google-pegasus-multi_news",
    # "google/bigbird-pegasus-large-arxiv": "./models/google-bigbird-pegasus-large-arxiv",
    "google/pegasus-cnn_dailymail": "./models/google-pegasus-cnn_dailymail",
}

@st.cache_resource
def load_all_models():
    models = {}
    tokenizers = {}
    for name, path in MODEL_PATHS.items():
        model = AutoModelForSeq2SeqLM.from_pretrained(path)
        tokenizer = AutoTokenizer.from_pretrained(path)
        models[name] = model
        tokenizers[name] = tokenizer
    return models, tokenizers


def summarize_text(text, model_name, models, tokenizers, **generate_kwargs):
    tokenizer = tokenizers[model_name]
    model = models[model_name]

    inputs = tokenizer([text], max_length=1024, return_tensors="pt", truncation=True)

    summary_ids = model.generate(
        inputs["input_ids"],
        num_beams=4,
        length_penalty=2.0,
        max_length=130,
        min_length=30,
        early_stopping=True,
        **generate_kwargs
    )

    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)