---
title: News
emoji: 🌍
colorFrom: green
colorTo: pink
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
# 📢 News Sentiment & Hindi TTS App

## 📌 Overview
This Streamlit app fetches news articles, performs sentiment analysis, extracts key topics, translates summaries to Hindi, and generates Hindi text-to-speech (TTS) audio. It also provides **detailed analysis reporting** and a **querying system** to search through stored news articles.

## 🚀 Features
- Fetches news from NewsAPI
- Performs sentiment analysis (Positive, Negative, Neutral)
- Extracts key topics using KeyBERT
- Provides **comparative analysis** of news coverage
- **Detailed analysis reporting** using charts and structured data
- **Querying system** to search for specific keywords in news articles
- Translates summaries to Hindi using Deep Translator
- Generates Hindi speech using gTTS

## 🛠 Installation & Setup

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/your-repo.git
cd your-repo
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Step 3: Set Up API Key**
1. Open `utils.py`.
2. Replace `NEWS_API_KEY` with your [NewsAPI](https://newsapi.org/) key.

### **Step 4: Run the Streamlit App**
```bash
streamlit run app.py
```

## 📂 Repository Structure
```
- app.py         # Main Streamlit app
- utils.py       # Utility functions (fetch news, sentiment analysis, etc.)
- requirements.txt  # Dependencies
- README.md      # Setup & usage instructions
```

## 📝 Notes
- Ensure you have a valid [NewsAPI](https://newsapi.org/) key.
- If TTS fails, install ffmpeg: `sudo apt install ffmpeg` (Linux/Mac).
- **To use the querying system**, enter a keyword in the search bar to filter news articles dynamically.
- **The detailed analysis report** includes sentiment distribution (pie chart) and top topics (data table).

## 📩 Contact
For support, create an issue in the repository!

🚀 **Enjoy analyzing news sentiment with Hindi TTS, detailed insights, and advanced search!** 🎤
