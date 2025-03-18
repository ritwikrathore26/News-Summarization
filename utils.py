import requests
from deep_translator import GoogleTranslator
from textblob import TextBlob
from gtts import gTTS
import os
from keybert import KeyBERT

# ✅ Load KeyBERT Model
kw_model = KeyBERT()

# ✅ Set News API Key
NEWS_API_KEY = "93eea26916b04a068b4f28afaac0607b"

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

# ✅ Function to Extract Topics
def extract_topics(text):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=5)
    return [kw[0] for kw in keywords]

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


# ✅ Function to Generate Hindi Speech
def generate_tts(text):
    tts = gTTS(text=text, lang="hi")
    filename = "tts_output.mp3"
    tts.save(filename)
    return filename
