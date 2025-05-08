import matplotlib.pyplot as plt

# Examine data types and missing values
print(df.info())

# Analyze sentiment distribution
sentiment_counts = df['Sentiment'].value_counts()
print(sentiment_counts)
plt.figure(figsize=(8, 6))
sentiment_counts.plot(kind='bar', color=['skyblue', 'salmon', 'lightgreen'])
plt.title('Distribution of Sentiment Labels')
plt.xlabel('Sentiment')
plt.ylabel('Count')
plt.show()

# Explore text data characteristics
df['text_length'] = df['Text'].astype(str).apply(len)
avg_text_length = df['text_length'].mean()
print(f"Average text length: {avg_text_length}")

plt.figure(figsize=(10, 6))
plt.hist(df['text_length'], bins=50, color='lightcoral')
plt.title('Distribution of Text Lengths')
plt.xlabel('Text Length')
plt.ylabel('Frequency')
plt.show()

# Analyze other relevant columns (example: Retweets vs. Sentiment)
plt.figure(figsize=(10, 6))
df.boxplot(column='Retweets', by='Sentiment', grid=False, showfliers=False, patch_artist=True,
            boxprops=dict(facecolor='lightblue'), medianprops=dict(color='black'))
plt.title('Retweets vs. Sentiment')
plt.suptitle('')  # Remove the default title
plt.xlabel('Sentiment')
plt.ylabel('Number of Retweets')
plt.show(
