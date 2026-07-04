# AI-Powered Sentiment Analysis & NLP Pipeline

Classifies customer product reviews as positive, negative, or neutral using
a classic NLP pipeline: clean text → TF-IDF → classical ML classifier.

## What it does
1. **Load** a labeled dataset of customer reviews (`reviews.csv`)
2. **Preprocess text** — lowercase, strip punctuation, tokenize, remove stopwords
   (a small custom stopword list, no external download needed)
3. **Vectorize** with TF-IDF (`TfidfVectorizer`)
4. **Train** Logistic Regression and Naive Bayes classifiers
5. **Evaluate** — accuracy + full classification report, picks the better model
6. **Visualize** — WordCloud of most frequent words + confusion matrix
7. **Bonus** — a `predict_sentiment()` function to score any new sentence

## How to run
```bash
pip install pandas scikit-learn matplotlib wordcloud
python generate_data.py   # creates reviews.csv (200 labeled reviews)
python train_model.py     # cleans text, trains models, prints metrics, saves charts
```

## Files
- `generate_data.py` — creates a synthetic labeled review dataset
- `train_model.py` — the NLP pipeline: clean → vectorize → train → evaluate → visualize
- `reviews.csv` — the dataset (200 reviews: 80 positive, 80 negative, 40 neutral)
- `charts/wordcloud.png`, `charts/confusion_matrix.png`



