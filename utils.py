import requests
from deep_translator import GoogleTranslator
from textblob import TextBlob
from gtts import gTTS
import os
from keybert import KeyBERT

from sentence_transformers import SentenceTransformer

# ✅ Set News API Key
NEWS_API_KEY = "93eea26916b04a068b4f28afaac0607b"

# ✅ Ensure the model is available
MODEL_PATH = "/home/user/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/"

if not os.path.exists(MODEL_PATH):
    print("🔄 Downloading KeyBERT model...")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    model.save(MODEL_PATH)

# ✅ Load KeyBERT with the correct model path
kw_model = KeyBERT(SentenceTransformer(MODEL_PATH))

def extract_topics(text):
    """Extracts key topics from text using KeyBERT."""
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=5)
    return [kw[0] for kw in keywords]



# ✅ Function to Fetch News
def get_news(company):
    url = f"https://newsapi.org/v2/everything?q={company}&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        return articles
    else:
        return []

# ✅ Function for Sentiment Analysis
def analyze_sentiment(text):
    sentiment_score = TextBlob(text).sentiment.polarity
    if sentiment_score > 0:
        return "Positive"
    elif sentiment_score < 0:
        return "Negative"
    else:
        return "Neutral"



# ✅ Function to Perform Comparative Analysis
def comparative_analysis(articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    topic_counts = {}

    for article in articles:
        summary = article.get("description", "")

        if summary is None or not isinstance(summary, str):
            summary = ""  # ✅ Replace None with an empty string
        
        sentiment = analyze_sentiment(summary)
        topics = extract_topics(summary)

        sentiment_counts[sentiment] += 1
        for topic in topics:
            topic_counts[topic] = topic_counts.get(topic, 0) + 1

    return {
        "Sentiment Distribution": sentiment_counts,
        "Top Topics Covered": sorted(topic_counts.items(), key=lambda x: x[1], reverse=True)
    }

def search_articles(articles, keyword):
    """Search for articles containing the keyword in title or summary."""
    if not keyword:
        return articles  # If no keyword, return all articles
    
    results = [article for article in articles if keyword.lower() in article.get("description", "").lower()]
    return results



# ✅ Function to Generate Hindi Speech
def generate_tts(text):
    tts = gTTS(text=text, lang="hi")
    filename = "tts_output.mp3"
    tts.save(filename)
    return filename
