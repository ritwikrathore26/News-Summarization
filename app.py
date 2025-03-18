import streamlit as st
import requests
from deep_translator import GoogleTranslator
from textblob import TextBlob
from gtts import gTTS
import os
from utils import get_news, analyze_sentiment, generate_tts, extract_topics, comparative_analysis,search_articles
import pandas as pd
import plotly.express as px


# 🎨 Streamlit UI
st.title("📢 News Sentiment & Hindi TTS App")
company = st.text_input("Enter company name").strip()

search_term = st.text_input("🔍 Search in articles (optional)").strip()
if search_term:
    articles = search_articles(articles, search_term)
    if not articles:
        st.warning(f"⚠️ No articles found containing '{search_term}'.")


if st.button("Get News & Audio"):
    if not company:
        st.error("❌ Company name cannot be empty!")
        st.stop()
    
    st.write(f"📡 Fetching news for: {company}")
    articles = get_news(company)
    
    if not articles:
        st.warning(f"⚠️ No news found for `{company}`.")
        st.stop()
    
    news_summaries = []
    topics_list = []
    
    for article in articles[:10]:  # Limit to 10 articles
        title = article.get("title", "No Title")
        summary = article.get("description", "No Summary")
        sentiment = analyze_sentiment(summary)
        topics = extract_topics(summary)
        
        st.markdown(f"**📌 {title}**")
        st.write(f"📄 **Summary:** {summary}")
        st.write(f"💬 **Sentiment:** {sentiment}")
        st.write(f"🔖 **Topics:** {', '.join(topics)}")
        st.write("---")
        
        news_summaries.append(summary)
        topics_list.extend(topics)
    
    # ✅ Translate to Hindi
    summary_text = " ".join(news_summaries)
    translated_text = GoogleTranslator(source="en", target="hi").translate(summary_text)
    
    st.write("### 🔊 Hindi Translation:")
    st.write(translated_text)
    
    # ✅ Generate TTS Audio
    audio_file = generate_tts(translated_text)
    st.write("### 🎧 Listen to Hindi Audio:")
    st.audio(audio_file)
    
    # ✅ Display Comparative Analysis
    st.write("### 📊 Comparative Analysis")
    comparison_result = comparative_analysis(articles)


    # Convert sentiment distribution to DataFrame
    sentiment_df = pd.DataFrame(comparison_result["Sentiment Distribution"].items(), columns=["Sentiment", "Count"])

    # Visualizing Sentiment Distribution
    st.write("### 📊 Sentiment Analysis Report")
    fig = px.pie(sentiment_df, names="Sentiment", values="Count", title="Sentiment Distribution")
    st.plotly_chart(fig)

    # Displaying Top Topics
    st.write("### 🔍 Top Topics Covered")
    topic_df = pd.DataFrame(comparison_result["Top Topics Covered"], columns=["Topic", "Mentions"])
    st.dataframe(topic_df)

    
    # ✅ Clean up temporary audio file after playing
    os.remove(audio_file)
