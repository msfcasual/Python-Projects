from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Example text data
texts = [
    "I love Python programming, it is so much fun!",
    "I hate getting stuck on bugs in my code.",
    "I feel so neutral about debugging, it’s okay.",
    "Python is an amazing language to learn!",
    "I am really frustrated with my progress."
]

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)  # Removed the colon here
    return blob.sentiment.polarity  # Polarity score: -1 (negative) to 1 (positive)

# Apply sentiment analysis to each text
sentiments = [analyze_sentiment(text) for text in texts]

# Create a DataFrame to store the text and sentiment data
df = pd.DataFrame({
    'text': texts,
    'sentiment': sentiments
})

# Classify sentiment as Positive, Negative, or Neutral
def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

df['sentiment_class'] = df['sentiment'].apply(classify_sentiment)

# Display the DataFrame
print(df)

# Visualize the sentiment distribution
plt.figure(figsize=(8, 6))
sns.countplot(x='sentiment_class', data=df, palette='coolwarm')

plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()
