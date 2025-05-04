import streamlit as st
import json

def load_articles():
    articles = []
    for file_path in ['data/train_summarized_articles.jsonl', 'data/test_summarized_articles.jsonl']:
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                file_articles = json.load(f)
                articles.extend(file_articles)
            except json.JSONDecodeError as e:
                st.warning(f"⚠️ Failed to load {file_path}: {e}")
    return articles

def view_summarized_articles():
    st.title("📂 View Summarized Articles")

    articles = load_articles()

    if not articles:
        st.warning("No articles found!")
        return

    titles = [article.get('title', f"Article {i+1}") for i, article in enumerate(articles)]

    selected_title = st.selectbox("Select an article by title:", titles)

    selected_article = next((article for article in articles if article.get('title') == selected_title), None)

    if selected_article:
        st.subheader("📰 Article Information")

        st.markdown(f"**Title:** {selected_article.get('title', '')}")
        st.markdown(f"**Description:** {selected_article.get('description', '')}")
        st.markdown(f"**Author:** {selected_article.get('author', '')}")
        st.markdown(f"**Published at:** {selected_article.get('publishedAt', '')}")
        st.markdown(f"**Source:** {selected_article.get('source', '')}")
        st.markdown(f"[🔗 Link to article]({selected_article.get('url', '#')})")

        st.markdown("**🧾 Content:**")
        st.text_area(
                    label="",
                    value=selected_article.get('content', '') if selected_article.get('content', '') else "N/A",
                    height=300,
                    disabled=True, key = 1
                )

        st.markdown(f"**Length of content:** {selected_article.get('content_len', '')}")

        st.markdown("**🧾 Preprocessed content:**")
        st.text_area(
            label="",
            value=selected_article.get('clean_content', '') if selected_article.get('clean_content', '') else "N/A",
            height=300,
            disabled=True, key = 2
        )

        st.markdown(f"**Length of Preprocessed content:** {selected_article.get('clean_content_len', '')}")

        st.markdown("---")
        st.subheader("🔍 Summaries Comparison")

        for key, value in selected_article.items():
            if key.startswith("summary_"):
                model_name = key.replace("summary_", "")  # Remove prefix
                st.markdown(f"**{model_name}:**")
                st.info(value if value else "N/A")

def main():
    view_summarized_articles()
