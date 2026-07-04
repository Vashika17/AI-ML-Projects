"""
train_model.py
---------------
End-to-end NLP pipeline for sentiment classification:

  1. Load labeled review data
  2. Preprocess text (lowercase, remove punctuation, remove stopwords)
  3. TF-IDF vectorization
  4. Train Logistic Regression + Naive Bayes classifiers
  5. Evaluate accuracy + confusion matrix
  6. Visualize: WordCloud (most frequent words) + confusion matrix

Run: python train_model.py
"""

import os
import re
import string
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
from wordcloud import WordCloud

CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

# A small, simple stopword list (avoids needing an internet download like NLTK's corpus)
STOPWORDS = set("""
a an the is it its this that of to in on for and or with as at by be are was were
i my me you your it's does do did not no very really just so
""".split())

# ------------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------------
df = pd.read_csv("reviews.csv")
print("Shape:", df.shape)
print("\nSentiment distribution:\n", df["sentiment"].value_counts())

# ------------------------------------------------------------------
# 2. PREPROCESS TEXT: lowercase, strip punctuation, remove stopwords
# ------------------------------------------------------------------
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    tokens = re.findall(r"\b[a-z]+\b", text)
    tokens = [t for t in tokens if t not in STOPWORDS]
    return " ".join(tokens)

df["clean_text"] = df["review_text"].apply(clean_text)
print("\nExample before/after cleaning:")
print("  Before:", df["review_text"].iloc[0])
print("  After :", df["clean_text"].iloc[0])

# ------------------------------------------------------------------
# 3. TF-IDF VECTORIZATION
# ------------------------------------------------------------------
vectorizer = TfidfVectorizer(max_features=500)
X = vectorizer.fit_transform(df["clean_text"])
y = df["sentiment"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ------------------------------------------------------------------
# 4. TRAIN MODELS
# ------------------------------------------------------------------
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

nb = MultinomialNB()
nb.fit(X_train, y_train)

# ------------------------------------------------------------------
# 5. EVALUATE
# ------------------------------------------------------------------
lr_pred = log_reg.predict(X_test)
nb_pred = nb.predict(X_test)

lr_acc = accuracy_score(y_test, lr_pred)
nb_acc = accuracy_score(y_test, nb_pred)

print(f"\nLogistic Regression accuracy: {lr_acc:.1%}")
print(f"Naive Bayes accuracy: {nb_acc:.1%}")

best_pred, best_name = (lr_pred, "Logistic Regression") if lr_acc >= nb_acc else (nb_pred, "Naive Bayes")
print(f"\nUsing {best_name} as final model")
print("\nClassification report:\n", classification_report(y_test, best_pred))

# ------------------------------------------------------------------
# 6. VISUALIZE: WordCloud + confusion matrix
# ------------------------------------------------------------------
all_text = " ".join(df["clean_text"])
wc = WordCloud(width=800, height=400, background_color="white", colormap="viridis").generate(all_text)
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Most Frequent Words Across All Reviews")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/wordcloud.png", dpi=120)
plt.close()

labels = sorted(y.unique())
cm = confusion_matrix(y_test, best_pred, labels=labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
disp.plot(cmap="Purples")
plt.title(f"Confusion Matrix ({best_name})")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/confusion_matrix.png", dpi=120)
plt.close()

print(f"\nCharts saved in ./{CHART_DIR}/")

# ------------------------------------------------------------------
# BONUS: quick function to score any new review text
# ------------------------------------------------------------------
def predict_sentiment(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    return log_reg.predict(vec)[0]

if __name__ == "__main__":
    sample = "The battery life is amazing and it charges so fast"
    print(f"\nSample prediction for: '{sample}'")
    print("Predicted sentiment:", predict_sentiment(sample))