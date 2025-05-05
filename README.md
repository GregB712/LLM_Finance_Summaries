# 📰 LLM_Finance_Summaries

Welcome to the **Article Summarizer App!** ✨  
This project leverages **Large Language Models (LLMs)** to generate concise summaries of financial and news articles, with tools for evaluation, visualization, and interactive exploration.

## 📚 About This Project

This app allows users to fetch articles either from a **preloaded database** or in **real-time using the NewsAPI**, and generate concise summaries using **powerful Transformer-based models**.

### 🚀 Features:

-   🔗 Fetch real-world articles using **NewsAPI**
    
-   🏗️ Store articles in a **database-backed storage**
    
-   🤖 Summarize articles using **Transformer-based models** (e.g., BART, Pegasus, BigBird)
    
-   🧪 Evaluate summaries with **ROUGE, BLEU, METEOR, BERTScore, Factual Consistency**
    
-   📈 Visualize and compare model performance across datasets
    
-   📝 Explore and annotate datasets
    
-   📚 Educational materials on evaluation metrics and hallucinations
    

## 🏗️ Tech Stack

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
    

----------

## ⚙️ Project Setup & Installation

### 📥 Clone the repository

```bash
git clone https://github.com/GregB712/LLM_Finance_Summaries.git
cd LLM_Finance_Summaries

```

✅ **Important Setup Steps:**

1.  **Create a folder for models:**
    

```bash
mkdir models

```

👉 Place your NLP / LLM models inside the `models/` folder.

2.  **Create a `.env` file with your NewsAPI key:**
    

In the project root:

```env
NEWS_API_KEY=your_newsapi_key_here

```

----------

### 🐍 Install dependencies

If not using Docker:

```bash
pip install -r requirements.txt

```

> ⚠️ Activate your virtual environment if you're using one.

----------

### 🐳 Run with Docker

1.  **Build the Docker image:**
    

```bash
docker build -t summarizer-app .

```

2.  **Run the Docker container:**
    

```bash
docker run -p 8501:8501 --env-file .env summarizer-app

```

✅ Access the app at [http://localhost:8501](http://localhost:8501/)

----------

## 🗂️ Project Structure

```
LLM_Finance_Summaries
├── Dockerfile
├── LICENSE
├── README.md
├── REPORTS
│   ├── REPORT.html
│   ├── REPORT.md
│   └── REPORT.pdf
├── app
│   ├── About.py
│   ├── Database.py
│   ├── FinetunedModelsResults.py
│   ├── Home.py
│   ├── NewsAPI.py
│   ├── Setup_and_Installation.py
│   ├── Summarize.py
│   ├── ViewFinetunedMetrics.py
│   ├── ViewSummarizedArticles.py
│   └── __init__.py
├── app.py
├── assets
│   ├── 1_Article_Summarizer_App.png
│   ├── 2_Fetch_Articles_From_NewsAPI.png
│   ├── 3_Article_Summarizer.png
│   ├── 4_View_Summarized_Articles.png
│   ├── 5_Fine-tuned_Model_Metrics.png
│   ├── 6_Finetuned_Models_Results.png
│   ├── 7_Project_Setup_Installation.png
│   ├── 8_About_This_Project.png
│   └── Summaries_Comparison.png
├── data
│   ├── articles.json
│   ├── bart-large-cnn
│   │   ├── summarized_articles_bart-large-cnn.json
│   │   ├── summary_metrics_bart-large-cnn.csv
│   │   ├── test_bart-large-cnn.jsonl
│   │   └── train_bart-large-cnn.jsonl
│   ├── pegasus-cnn_dailymail
│   │   ├── summarized_articles_pegasus-cnn_dailymail.json
│   │   ├── summary_metrics_pegasus-cnn_dailymail.csv
│   │   ├── test_pegasus-cnn_dailymail.jsonl
│   │   └── train_pegasus-cnn_dailymail.jsonl
│   ├── pegasus-multi_news
│   │   ├── summarized_articles_pegasus-multi_news.json
│   │   ├── summary_metrics_pegasus-multi_news.csv
│   │   ├── test_pegasus-multi_news.jsonl
│   │   └── train_pegasus-multi_news.jsonl
│   ├── pegasus-xsum
│   │   ├── summarized_articles_pegasus-xsum.json
│   │   ├── summary_metrics_pegasus-xsum.csv
│   │   ├── test_pegasus-xsum.jsonl
│   │   └── train_pegasus-xsum.jsonl
│   ├── test_summarized_articles.jsonl
│   └── train_summarized_articles.jsonl
├── main.py
├── models <-- You need to create this manually and add your models
│   ├── facebook-bart-large-cnn
│   │   ├── config.json
│   │   ├── generation_config.json
│   │   ├── merges.txt
│   │   ├── model.safetensors
│   │   ├── special_tokens_map.json
│   │   ├── tokenizer.json
│   │   ├── tokenizer_config.json
│   │   └── vocab.json
│   └── google-pegasus-cnn_dailymail
│       ├── config.json
│       ├── generation_config.json
│       ├── model.safetensors
│       ├── special_tokens_map.json
│       ├── spiece.model
│       ├── tokenizer.json
│       └── tokenizer_config.json
├── notebooks
│   ├── LLM_Finance_Summaries_Dataset.ipynb
│   ├── LLM_Finance_Summaries_Metrics.ipynb
│   └── LLM_Finance_Summaries_Train.ipynb
├── requirements.txt
├── utils
│   ├── __init__.py
│   ├── article_store.py
│   ├── newsapi.py
│   ├── preprocessor.py
│   └── summarizer.py
└── .env                    <-- You need to create this manually with your API key

```

----------

## 💬 Example Usage

1.  Start the app (either via Docker or `streamlit run main.py`)
    
2.  Go to the **NewsAPI** page in the app to fetch new articles
    
3.  Use the **Summarize** page to preprocess and summarize articles from the database
    
4.  View **summarized articles** or **evaluation metrics** for completed experiments
    
5.  Explore **finetuned model results** and **annotated datasets**
    

----------

## 👨‍💻 Developed By

**Gregory Barbas**  
📧 Email: [gregorybarbas@gmail.com](mailto:gregorybarbas@gmail.com)  
💼 [LinkedIn](https://linkedin.com/in/gbarmpas)  
🖥️ [GitHub](https://github.com/GregB712)

For questions or contributions, feel free to reach out!

----------

## 📌 Notes

-   You must provide a valid **NewsAPI key** in the `.env` file to use the live news feature.
    
-   Some models may take longer to load on first use. Models are preloaded for performance.

----------

## 📝 License

This project is licensed under the **MIT License**.
