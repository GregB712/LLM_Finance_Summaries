import streamlit as st
from utils.summarizer import summarize_text
from utils.preprocessor import preprocess_text
from utils.article_store import load_articles
from utils.summarizer import load_all_models

@st.cache_resource
def get_cached_models():
    return load_all_models()

def main():
    st.title("🧠 Article Summarizer")

    models, tokenizers = get_cached_models()

    # Get articles from both sources
    all_articles = load_articles()
    if not all_articles:
        st.warning("⚠️ No articles found in the database.")
        return

    titles = [article["title"] for article in all_articles]

    selected_title = st.selectbox("Select an article", titles, key = 1)

    selected_article = next((a for a in all_articles if a["title"] == selected_title), None)

    if selected_article:
        with st.container():
            st.markdown(f"### 📰 {selected_article['title']}")
            st.markdown(f"**Description**: {selected_article.get('description', 'No description.')}")
            st.markdown(f"**Published at**: {selected_article.get('publishedAt', 'Unknown')}")
            st.markdown(f"**Author**: {selected_article.get('author', 'Unknown')}")
            st.markdown(f"**Source**: {selected_article.get('source', {}).get('name', 'Unknown')}")
            st.markdown(f"[🔗 Link to article]({selected_article.get('url', '#')})")

            st.markdown("#### 🧾 Full Content:")
            st.text_area(
                label="",
                value=selected_article.get("content", "No content available."),
                height=300,
                disabled=True, key = 4
            )

            st.session_state["selected_article"] = selected_article

    if not all_articles:
        st.warning("No articles available. Please use 'From Database' or 'NewsAPI' first.")
        return

    if selected_article:
        content = selected_article.get("content", "")
        # st.markdown("### 📜 Original Content")
        # st.text_area("", content, height=300, disabled=True, key = 5)

        if st.button("🧹 Preprocess"):
            cleaned = preprocess_text(content)
            st.session_state["preprocessed_text"] = cleaned
            st.session_state["selected_for_summary"] = cleaned

        if "preprocessed_text" in st.session_state:
            st.markdown("### 🧼 Preprocessed Content")
            
            # Editable text area for preprocessed content
            preprocessed_content = st.text_area(
                "Edit Preprocessed Content (optional):",
                st.session_state["preprocessed_text"],
                height=300, key = 6
            )

            st.session_state["selected_for_summary"] = preprocessed_content

            st.markdown("### ✨ Choose a summarization model:")
            model_name = st.selectbox("Model", [
                "facebook/bart-large-cnn",
                "google/pegasus-cnn_dailymail"
            ], key = 3)

            if st.button("⚡ Summarize"):
                with st.spinner("Summarizing..."):
                    try:
                        summary = summary = summarize_text(
                            st.session_state["selected_for_summary"],
                            model_name=model_name,
                            models=models,
                            tokenizers=tokenizers
                        )
                        st.markdown("### 📝 Summary:")
                        st.success(summary)
                    except Exception as e:
                        st.error(f"Summarization failed: {e}")
