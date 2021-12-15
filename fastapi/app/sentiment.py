from textblob import TextBlob
import pandas as pd

def convert_to_df(sentiment_result):
    sentiment_dict = {'polarity': sentiment_result.polarity,
                      'subjectivity': sentiment_result.subjectivity}
    sentiment_df = pd.DataFrame(
        sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df


def process_sentiment(raw_text):
    sentiment = TextBlob(raw_text).sentiment
    # st.write(sentiment)
    result = {}
    # Emoji
    if sentiment.polarity > 0:
        result["Sentiment"]= "Positive"
    elif sentiment.polarity < 0:
        result["Sentiment"]= "Negative"
    else:
        result["Sentiment"]= "Neutral"

    # st.write(type(sentiment))
    result_df = convert_to_df(sentiment)
    result["dataframe"]= result_df

    return result