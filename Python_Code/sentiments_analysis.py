import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from pathlib import Path

# ==========================================
# Amazon Reviews Sentiment Analysis Project
# ==========================================

# Project directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATASET_DIR = BASE_DIR / "Dataset"
CHARTS_DIR = BASE_DIR / "Charts"

# Load Dataset
print("Loading Amazon Reviews Dataset...")

df = pd.read_csv(
    DATASET_DIR / "amazon_reviews.csv",
    header=None,
    names=["Label", "Title", "Review"]
)

# Use first 5000 reviews for faster processing
df = df.head(5000)

print(f"Total Reviews Loaded: {len(df)}")

# ==========================================
# Sentiment Analysis Function
# ==========================================

def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply Sentiment Analysis
print("Analyzing Sentiments...")

df["Sentiment"] = df["Review"].apply(get_sentiment)

print("\nSample Output:")
print(df.head())

# Save Results
output_file = DATASET_DIR / "sentiment_results.csv"
df.to_csv(output_file, index=False)

# ==========================================
# Bar Chart
# ==========================================

sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(6,4))
sentiment_counts.plot(
    kind="bar",
    color=["green", "red", "gray"]
)

plt.title("Sentiment Analysis of Amazon Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.tight_layout()

plt.savefig(CHARTS_DIR / "sentiment_bar_chart.png")
plt.show()

# ==========================================
# Pie Chart
# ==========================================

plt.figure(figsize=(6,6))

sentiment_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Distribution")
plt.ylabel("")

plt.savefig(CHARTS_DIR / "sentiment_pie_chart.png")
plt.show()

# ==========================================
# Word Cloud
# ==========================================

text = " ".join(df["Review"].astype(str))

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(text)

plt.figure(figsize=(12,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Amazon Reviews")

plt.tight_layout()

plt.savefig(CHARTS_DIR / "wordcloud.png")
plt.show()

# ==========================================
# Sentiment Summary
# ==========================================

print("\n========== Sentiment Analysis Summary ==========\n")

print(df["Sentiment"].value_counts())

total_reviews = len(df)

positive = (df["Sentiment"] == "Positive").sum()
negative = (df["Sentiment"] == "Negative").sum()
neutral = (df["Sentiment"] == "Neutral").sum()

print("\nTotal Reviews :", total_reviews)
print("Positive Reviews :", positive)
print("Negative Reviews :", negative)
print("Neutral Reviews :", neutral)

print(f"\nPositive Percentage : {(positive/total_reviews)*100:.2f}%")
print(f"Negative Percentage : {(negative/total_reviews)*100:.2f}%")
print(f"Neutral Percentage : {(neutral/total_reviews)*100:.2f}%")

# ==========================================
# Public Opinion & Trend Analysis
# ==========================================

print("\n========== Public Opinion & Trends ==========\n")

if positive > negative:
    print("Overall public opinion is POSITIVE.")
    print("Customers are generally satisfied with the products.")
elif negative > positive:
    print("Overall public opinion is NEGATIVE.")
    print("Customers are dissatisfied with several products.")
else:
    print("Customer opinion is balanced.")

print("\nInsights:")
print("- Positive reviews indicate customer satisfaction.")
print("- Negative reviews highlight issues related to product quality, delivery, or packaging.")
print("- Neutral reviews represent factual or balanced opinions.")
print("- Businesses can use these insights to improve products and customer experience.")

print("\n============================================")
print("Amazon Reviews Sentiment Analysis Completed")
print("============================================")

print(f"\nResults saved to : {output_file}")
print(f"Bar Chart saved : {CHARTS_DIR / 'sentiment_bar_chart.png'}")
print(f"Pie Chart saved : {CHARTS_DIR / 'sentiment_pie_chart.png'}")
print(f"Word Cloud saved : {CHARTS_DIR / 'wordcloud.png'}")