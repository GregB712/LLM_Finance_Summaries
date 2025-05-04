import streamlit as st

def main():
    st.title("📚 About This Project")

    st.markdown("""
    Welcome to the **Article Summarizer App**! 📰✨  
    This app allows users to fetch news articles either from a preloaded database or in real-time using the [NewsAPI](https://newsapi.org/), and generate concise summaries using powerful Transformer-based models.

    ### 🚀 It integrates:
    - 🔗 NewsAPI to fetch real-world articles
    - 🏗️ Database-backed storage of articles
    - 🤖 Transformer-based summarization models
    - 🧪 Multiple evaluation metrics including **ROUGE**, **BLEU**, **METEOR**, **BERTScore**, **Factual Consistency**
    - 📈 Visualizations and comparisons across models and datasets
    - 📝 Annotated dataset exploration
    - 📚 Educational material on metrics and hallucinations

    ### 🏗️ Tech Stack
    - [**Python 3.10+**](https://www.python.org/doc/)
    - [**Streamlit**](https://docs.streamlit.io/)
    - [**Docker**](https://docs.docker.com/)
    - [**Hugging Face Transformers**](https://huggingface.co/docs/transformers/index)
    - [**spaCy**](https://spacy.io/usage)
    - [**NewsAPI**](https://newsapi.org/docs/get-started)
    - [**Pandas**](https://pandas.pydata.org/docs/) / [**NumPy**](https://numpy.org/doc/)
    - [**Matplotlib**](https://matplotlib.org/stable/contents.html) / [**Plotly**](https://plotly.com/python/)
    - [**scikit-learn**](https://scikit-learn.org/stable/documentation.html)
    - [**NLTK**](https://www.nltk.org/) / [**Evaluate library**](https://huggingface.co/docs/evaluate/index)


    ### 👨‍💻 Developed By
    **Gregory Barbas**

    - 📧 Email: [gregorybarbas@gmail.com](mailto:gregorybarbas@gmail.com)
    - 💼 LinkedIn: [linkedin.com/in/gbarmpas](https://www.linkedin.com/in/gbarmpas)
    - 🖥️ GitHub: [github.com/GregB712](https://github.com/GregB712)

    For questions or contributions, feel free to reach out!

    ### 📌 Note
    - You must provide a valid NewsAPI key to use the live news feature.
    - Some models may take longer to load on first use. Models are preloaded for performance.

    Built with ❤️ using open-source technologies to empower summarization research.
    """)

    st.success("Thanks for using the Article Summarizer App! 🚀")

