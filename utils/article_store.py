import json
from pathlib import Path

DATA_PATH = Path("data/articles.json")

def load_articles():
    if not DATA_PATH.exists():
        return []
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def get_article_by_title(title):
    articles = load_articles()
    for article in articles:
        if article["title"] == title:
            return article
    return None
