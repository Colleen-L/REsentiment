from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(headline):
    sentiment = analyzer.polarity_scores(headline)
    compound_score = sentiment['compound']
    
    if compound_score >= 0.05:
        label = "positive"
    elif compound_score <= -0.05:
        label = "negative"
    else:
        label = "neutral"
    
    return {"label": label, "score": compound_score}