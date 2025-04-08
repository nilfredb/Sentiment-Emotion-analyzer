# 🧠 Sentiment & Emotion Analyzer

A modern, interactive dashboard built with Python and Streamlit to analyze user feedback through **sentiment analysis** and **emotion detection**, using both classical and transformer-based NLP models.

---

## 🚀 Features

- 📤 Upload a CSV file with user comments
- 💬 Analyze sentiment using:
  - TextBlob (lightweight rule-based)
  - DistilBERT (transformer-based)
- 🎭 Detect emotions: joy, anger, sadness, fear, surprise, neutral
- 📊 Visualize results with bar charts and word clouds
- 📥 Download enriched data as CSV

---

## 🧰 Tech Stack

- **Python**
- **Streamlit** – for UI
- **TextBlob** – basic sentiment analysis
- **HuggingFace Transformers** – DistilBERT and DistilRoBERTa models
- **Pandas** – data manipulation
- **Matplotlib** & **WordCloud** – data visualization

---

## 📷 Screenshot

![screenshot](screenshot.png)

> *(Optional: Add a real screenshot of your running app here)*

---

## 📂 File Format

Make sure your CSV has at least one column named **`comment`** containing user-generated text.

```csv
comment
I love the product!
Terrible service, very disappointed.
It was okay, nothing special.
```

---

## 🔧 Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/sentiment-dashboard.git
cd sentiment-dashboard
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

4. **Run the app**

```bash
streamlit run app.py
```

---

## ☁️ Deployment (optional)

You can deploy it easily using:
- [Streamlit Cloud](https://share.streamlit.io/)
- [Render](https://render.com)
- [Hugging Face Spaces](https://huggingface.co/spaces)

---

## 📄 License

This project is open-source under the **MIT License**.

---

## 🙌 Author

Made with ❤️ by [Nilfred Báez](https://github.com/yourusername)

> If you found this useful, give it a ⭐ on GitHub!