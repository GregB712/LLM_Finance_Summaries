import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWSAPI_KEY")
BASE_URL = "https://newsapi.org/v2/everything"

def fetch_full_article_text(url):
    try:
        page = requests.get(url, timeout=5)
        soup = BeautifulSoup(page.content, "html.parser")
        
        # Extract paragraphs or main article tag
        paragraphs = soup.find_all("p")
        full_text = " ".join([p.get_text() for p in paragraphs])

        return full_text.strip()
    except Exception as e:
        print(f"Error fetching full text from {url}: {e}")
        return None

def get_apple_finance_articles(query, num_articles=5):
    #  Replace with your actual API key if using a paid news API
    _api_key = API_KEY
    _base_url = BASE_URL

    # Keywords and parameters for the API request
    query_params = {
        "q": query,
        "apiKey": _api_key,
        "from" : "2025-04-20& to 2025-04-30&",
        "language": "en",
        "sortBy": "relevancy",  # Sort results by relevancy
        "pageSize": num_articles  # Limit the number of results
    }

    try:
        response = requests.get(_base_url, params=query_params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        articles = []
        if data["status"] == "ok":
            for article in data["articles"]:
                source = article.get("source")
                author = article.get("author")
                publishedAt = article.get("publishedAt")
                title = article.get("title")
                description = article.get("description")
                url = article.get("url")
                content = fetch_full_article_text(url)

                if title and description and url: # Ensure article data exists
                    article_info = {
                        "source": source,
                        "author": author,
                        "publishedAt": publishedAt,
                        "title": title,
                        "description": description,
                        "url": url,
                        "content": content
                    }
                    articles.append(article_info)

        return articles
    except requests.exceptions.RequestException as e:
        print(f"Error fetching articles: {e}")
        return []

# def fetch_articles(query, page_size=10):
#     params = {
#         "q": query,
#         "pageSize": page_size,
#         "language": "en",
#         "apiKey": API_KEY
#     }
#     response = requests.get(BASE_URL, params=params)
#     if response.status_code != 200:
#         return []
#     data = response.json()
#     return data.get("articles", [])
