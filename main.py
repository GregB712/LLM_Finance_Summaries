import streamlit as st
import importlib
# from utils.summarizer import preload_models

PAGES = {
    "🏠 Home": "app.Home",
    # "📂 From Database": "app.Database",
    "🌐 Fetch Articles": "app.NewsAPI",
    "🧠 Summarize": "app.Summarize",
    "📖 View Summarized Articles": "app.ViewSummarizedArticles",
    "📊 Fine-tuned Model Metrics": "app.ViewFinetunedMetrics",
    "🧪 Fine-tuned Models Results": "app.FinetunedModelsResults",
    "⚙️ Project Setup & Installation": "app.Setup_and_Installation",
    "ℹ️ About": "app.About"
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page_module = importlib.import_module(PAGES[selection])
page_module.main()

# # Ensure models are loaded when the app starts
# with st.spinner("Loading models, please wait..."):
#     preload_models()
