from fastapi import FastAPI
from utils import get_news, analyze_sentiment, generate_tts

app = FastAPI()

@app.get("/news/{company_name}")
def fetch_news(company_name: str):
    """Fetches and analyzes news about a company."""
    articles = get_news(company_name)
    if not articles:
        return {"detail": "No news found"}
    
    for article in articles:
        article["sentiment"] = analyze_sentiment(article.get("description", ""))
    
    return {"company": company_name, "articles": articles}

@app.post("/tts/")
def text_to_speech(text: str):
    """Converts text to Hindi speech."""
    filename = generate_tts(text)
    return {"audio_file": filename}
