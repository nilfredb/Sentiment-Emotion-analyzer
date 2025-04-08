import streamlit as st
import pandas as pd
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from transformers import pipeline

# === PAGE SETUP ===
st.set_page_config(page_title="Sentiment & Emotion Analyzer", layout="wide")

# === HEADER ===
st.markdown("""
# 🧠 Sentiment & Emotion Analyzer
Analyze user feedback for sentiment and emotional tone using modern NLP models.

Upload a CSV of comments, and this dashboard will do the rest! 🚀
""")

# === LOAD MODELS ===
@st.cache_resource
def load_distilbert_pipeline():
    return pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

@st.cache_resource
def load_emotion_pipeline():
    return pipeline("text-classification", 
                    model="j-hartmann/emotion-english-distilroberta-base", 
                    return_all_scores=False)

classifier = load_distilbert_pipeline()
emotion_classifier = load_emotion_pipeline()

# === ANALYSIS FUNCTIONS ===
def get_sentiment(text):
    blob = TextBlob(str(text))
    return blob.sentiment.polarity

def analyze_distilbert(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']
    polarity = score if label == "POSITIVE" else -score
    return polarity, label

def get_emotion(text):
    result = emotion_classifier(text)[0]
    return result["label"], result["score"]

# === TABS ===
tab1, tab2, tab3, tab4 = st.tabs(["📤 Upload", "💬 Sentiment", "🎭 Emotions", "📊 Visualizations"])

with tab1:
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)

        if "comment" not in df.columns:
            st.error("CSV must contain a 'comment' column.")
        else:
            st.success("File uploaded successfully!")
            st.dataframe(df.head())

            with st.expander("ℹ️ Tips"):
                st.markdown("Make sure your CSV has a `comment` column containing the user feedback text.")

with tab2:
    if uploaded_file and "comment" in df.columns:
        st.subheader("Sentiment Analysis")

        method = st.radio("Select Sentiment Engine", ("TextBlob", "DistilBERT"))

        if method == "TextBlob":
            df["polarity"] = df["comment"].apply(get_sentiment)
            df["sentiment"] = df["polarity"].apply(
                lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Neutral"
            )
        else:
            df[["polarity", "sentiment"]] = df["comment"].apply(
                lambda x: pd.Series(analyze_distilbert(x))
            )

        st.dataframe(df[["comment", "sentiment", "polarity"]])
        st.bar_chart(df["sentiment"].value_counts())

with tab3:
    if uploaded_file and "comment" in df.columns:
        st.subheader("Emotion Detection")

        df[["emotion", "emotion_score"]] = df["comment"].apply(
            lambda x: pd.Series(get_emotion(x))
        )

        st.dataframe(df[["comment", "emotion", "emotion_score"]])
        st.bar_chart(df["emotion"].value_counts())

with tab4:
    if uploaded_file and "comment" in df.columns:
        st.subheader("Word Cloud")
        all_text = " ".join(df["comment"].astype(str))
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate(all_text)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)

        st.subheader("Download Results")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download as CSV", data=csv, file_name="results.csv", mime="text/csv")

# === FOOTER ===
st.markdown("""
---
Made with ❤️ by [Nilfred](https://github.com/nilfredb) • Powered by Python & Streamlit
""")
