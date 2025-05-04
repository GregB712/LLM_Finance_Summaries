import streamlit as st
from utils.article_store import load_articles

def main():
    st.title("📂 Choose an Article from Database")
    st.markdown("Select an article below to preview its full content before summarizing.")

    articles = load_articles()
    if not articles:
        st.warning("⚠️ No articles found in the database.")
        return

    titles = [article["title"] for article in articles]

    selected_title = st.selectbox("Select an article", titles)

    selected_article = next((a for a in articles if a["title"] == selected_title), None)

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
                disabled=True,
            )

            st.session_state["selected_article"] = selected_article