import streamlit as st

def main():
    st.title("📰 Article Summarizer App")
    st.subheader("Your all-in-one solution for news summarization and evaluation")

    st.markdown("""
    Welcome to the **Article Summarizer App!**

    With this app, you can:
    - 🔍 Fetch news articles from **NewsAPI**
    - 🗃️ View articles stored in your **database**
    - ✨ **Preprocess** and clean article content
    - ✂️ **Summarize** articles using various models
    - 📊 **Evaluate** summaries with automated metrics
    - 📝 Explore annotated datasets and fine-tuned model results
    - 📚 Learn about evaluation metrics and summarization

    ---

    💡 Navigate through the pages from the left sidebar to get started!
    """)

    # st.image("https://images.unsplash.com/photo-1557426272-fc759fdf7a1e", caption="Bringing AI-powered summarization to your fingertips", use_column_width=True)

    st.markdown("---")

    st.info("🔧 **For setup instructions, check the `Setup & Installation` page in the sidebar.**")

    st.success("✨ Happy summarizing!")
