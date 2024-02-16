import streamlit as st
import pandas as pd

data = pd.read_csv('../../news_harbor/data/sentiment_data.csv')

def filter_articles_with_info(sentiment):
    articles = data[data['Sentiment'] == sentiment]['Description'].tolist()
    urls = data[data['Sentiment'] == sentiment]['URL'].tolist()
    sources = data[data['Sentiment'] == sentiment]['Source Name'].tolist()
    return zip(articles, urls, sources)

def main():
    st.title('News Harbor')
    st.write('A harbor for sentimented news articles')

    sentiments = ['Positive', 'Neutral', 'Negative', 'Very Negative', 'Very Positive']

    selected_sentiment = st.sidebar.radio('Select Sentiment', sentiments)

    st.subheader(selected_sentiment)
    articles_with_urls = filter_articles_with_info(selected_sentiment)
    for article, url, source in articles_with_urls:
        st.write(f"**Article:** {article}")
        st.write(f"**Source:** {source}")
        st.write(f"**URL:** [{url}]({url})")
        st.markdown("---")

if __name__ == '__main__':
    main()
    print(data.columns)
