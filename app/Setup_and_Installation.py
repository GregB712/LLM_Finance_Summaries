import streamlit as st

def main():
    st.title("⚙️ Project Setup & Installation")

    st.markdown("""
    Welcome to the **Article Summarizer App**!

    This app summarizes news articles from NewsAPI or your own database, preprocesses content, and evaluates summarization models.

    Below you'll find everything you need to install and run the project locally or via Docker.
    """)

    st.header("📥 Clone the repository")

    st.code("""
    git clone https://github.com/GregB712/LLM_Finance_Summaries.git
    cd LLM_Finance_Summaries
    """, language="bash")

    st.subheader("⚠️ Note:")
    st.markdown("- Make sure to activate your virtual environment if using one.")
    st.markdown("- If you're running on Windows WSL, ensure Docker Desktop integration is enabled.")

    st.header("🐳 Run with Docker")

    st.subheader("🔍 **Steps to build and run Docker image:**")
    st.code("""
    # Build the Docker image
    docker build -t summarizer-app .

    # Run the app
    docker run -p 8501:8501 --env-file .env summarizer-app
    """, language="bash")

    st.markdown("✅ The app will be available at [http://localhost:8501](http://localhost:8501)")

    st.header("🗂️ Project Structure")

    st.code("""
    LLM_Finance_Summaries
    ├── Dockerfile
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
    ├── data
    ├── main.py
    ├── notebooks
    ├── requirements.txt
    └── utils
        ├── __init__.py
        ├── article_store.py
        ├── config.py
        ├── news_fetcher.py
        ├── newsapi.py
        ├── preprocessor.py
        └── summarizer.py
    """)

    st.header("🔑 Environment Variables (.env file)")

    st.markdown("You need to create a `.env` file with your API key:")
    st.code("""
    NEWS_API_KEY=your_newsapi_key_here
    """)

    st.header("💬 Example usage")

    st.markdown("""
    - Start the app
    - Go to **NewsAPI** page to check how to fetch articles
    - Use **Summarize** page to preprocess and summarize articles from the database
    - View summaries or evaluation metrics for the experiments executed

    ---

    📖 For detailed instructions, check the [GitHub repository](https://github.com/YourUsername/your-repo-name).
    """)

    st.success("🎉 Done! Feel free to contact me if you have any questions.")

