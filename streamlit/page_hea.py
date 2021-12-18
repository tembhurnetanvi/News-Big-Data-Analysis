from fastapi.app.main import health_tts
import streamlit as st
import pandas as pd
import spacy_streamlit
import spacy
from spacy import displacy
import requests
from requests.structures import CaseInsensitiveDict

nlp = spacy.load('en_core_web_sm')

def main():
    pages = {
    "Article Selection": page_second,
    "Dashboard": page_third
    
    }

    if "page" not in st.session_state:
        st.session_state.update({
            # Default page
            "page": "Article Selection",

            # Default widget values
            "int": 0,
            "options": ["NER","Summarization","Sentiment", "Tokenize"],
            "radio": "NER"
        })

    with st.sidebar:
        page = st.radio("Select your page", tuple(pages.keys()))

    pages[page]()


def page_second():
    st.header("HEALTH")
    DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/health.csv"
    data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
    data_pol = data[['title',"datetime"]]
    st.write('### Full Dataset', data_pol)
    int_val = st.number_input('Select a row for the article', min_value=0, max_value=49, step=1, key="int")
    title = st.header(data["title"][int_val])
    audio_backend = f'https://news-analysis-px7gwe6txq-ue.a.run.app/health/{int_val}/text-to-speech'
    audio = process_tts(audio_backend)
    if audio:
        st.audio(f'https://storage.googleapis.com/audio-output/health/{int_val}.mp3', format='audio/ogg')
    author = st.write("Author "+data["author"][int_val])
    datetime = st.write(data["datetime"][int_val])
    body = st.write(data["body"][int_val])
    article_url = st.write(data["url"][int_val])



def page_third():
    x=st.session_state.int
    st.session_state.int = x
    DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/health.csv"
    data = st.cache(pd.read_csv)(DATA_URL)
    nlp_option = st.radio("Services", st.session_state["options"], key="radio")
    
    if nlp_option=="NER":
        st.write("# NER")
        doc=nlp(data["body"][x])
        spacy_streamlit.visualize_ner(doc,labels=nlp.get_pipe('ner').labels, show_table=False)
        
    if nlp_option=="Tokenize":
        st.write("# Text Tokenization")
        doc=nlp(data["body"][x])
        spacy_streamlit.visualize_tokens(doc, attrs=["text", "pos_", "dep_", "ent_type_"])

    if nlp_option=="Sentiment":
        st.write("# Sentiment")
        backend = f'https://news-analysis-px7gwe6txq-ue.a.run.app/health/{x}/sentiment'
        sentiment = process_sentiment(backend)
        st.write(sentiment ["Sentiment"])
        st.write(sentiment["Subjectivity"])

    if nlp_option=="Summarization":
        st.write("# Summarization")
        backend = f'https://news-analysis-px7gwe6txq-ue.a.run.app/health/{x}/summarizer'
        summarize = process_summarization(backend)
        st.write(summarize)

def process_sentiment(server_url: str):
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    # headers["Content-Type"] = "application/json"
    # valid_text = {
    #         'text': input_text
    #     }
    # data = '{"text":'+input_text+'}'
    # data = '{"text":"'+text+'"}'
    data = ''
    resp = requests.post(server_url, headers=headers, data=data, verify=False, timeout=8000)
    result = resp.json()
    result_dict = result['sentiment']
    valid_sentiment = result_dict["Sentiment"]
    valid_subjectivity = result_dict["dataframe"]["value"]["1"]
    return {"Sentiment":valid_sentiment, "Subjectivity":valid_subjectivity}

def process_tts(server_url: str):
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    # headers["Content-Type"] = "application/json"
    # valid_text = {
    #         'text': input_text
    #     }
    # data = '{"text":'+input_text+'}'
    # data = '{"text":"'+text+'"}'
    data = ''
    resp = requests.post(server_url, headers=headers, data=data, verify=False, timeout=8000)
    result = resp.json()
    valid_result = result['Save']
    return True if valid_result=="Successful" else False

def process_summarization(server_url: str):
    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json"
    data = ''
    resp = requests.post(server_url, headers=headers, data=data, verify=False, timeout=8000)
    result = resp.json()
    summ = result["summary"][0]["summary_text"]
    return summ
        
if __name__ == "__main__":
    main()