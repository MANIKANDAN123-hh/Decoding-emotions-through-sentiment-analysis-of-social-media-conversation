# Consolidate low-frequency sentiments
sentiment_counts = df['Sentiment'].value_counts()
low_frequency_sentiments = sentiment_counts[sentiment_counts < 10].index
df['cleaned_sentiment'] = df['Sentiment'].replace(low_frequency_sentiments, 'Other')

# Remove duplicate rows based on 'Text'
df.drop_duplicates(subset='Text', inplace=True, ignore_index=True)

# Verify the cleaning
print(df['cleaned_sentiment'].value_counts())
print(df.shape)
