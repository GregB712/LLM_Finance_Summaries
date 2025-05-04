import streamlit as st
from utils.newsapi import get_apple_finance_articles

def main():
    st.title("🌐 Fetch Articles from NewsAPI")
    st.markdown("Search for recent articles by keyword and select one to summarize.")

    
    with st.form("search_form"):
        query = st.text_input("🔍 Enter a search term (e.g., AI, climate change, economy):", value="Apple Finance")
        num_articles = st.slider("Number of articles", min_value=1, max_value=20, value=5)
        submitted = st.form_submit_button("Search")

    if submitted:
        with st.spinner("🔄 Fetching articles..."):
            try:
                articles = get_apple_finance_articles(query, num_articles)
                if not articles:
                    st.warning("No articles found.")
                else:
                    st.session_state["news_articles"] = articles
                    st.session_state["selected_news_title"] = articles[0]["title"]
            except Exception as e:
                st.error(f"Error fetching articles: {e}")

    # Only show dropdown if we have stored articles
    if "news_articles" in st.session_state:
        articles = st.session_state["news_articles"]
        titles = [article["title"] for article in articles]

        selected_title = st.selectbox(
            "Select an article:",
            titles,
            index=titles.index(st.session_state.get("selected_news_title", titles[0])),
            key="selected_news_title"
        )

        selected_article = next((a for a in articles if a["title"] == selected_title), None)
        if selected_article:
            with st.container():
                st.markdown(f"### 📰 {selected_article['title']}")
                st.markdown(f"**Description**: {selected_article.get('description', 'No description available.')}")
                st.markdown(f"**Published at**: {selected_article.get('publishedAt', 'Unknown')}")
                st.markdown(f"**Author**: {selected_article.get('author', 'Unknown')}")
                st.markdown(f"**Source**: {selected_article.get('source', {}).get('name', 'Unknown')}")
                st.markdown(f"[🔗 Read full article]({selected_article.get('url')})")

                st.markdown("#### 🧾 Full Content:")
                st.text_area(
                    label="",
                    value=selected_article.get("content", "No content available."),
                    height=300,
                    disabled=True,
                )

                # Save in session for use in summarization
                st.session_state["selected_article"] = selected_article
