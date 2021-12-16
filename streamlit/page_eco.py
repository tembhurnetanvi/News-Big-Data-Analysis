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
    st.header("ECONOMY")
    DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv"
    data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
    data_pol = data[['title',"datetime"]]
    st.write('### Full Dataset', data_pol)
    int_val = st.number_input('Select a row for the article', min_value=0, max_value=49, step=1, key="int")
    title = st.header(data["title"][int_val])
    audio_backend = f'http://localhost:8000/economy/{x}/text-to-speech'
    audio = process_tts(audio_backend)
    if audio:
        st.audio(f'https://storage.googleapis.com/audio-output/economy_{int_val}.mp3', format='audio/ogg')
    author = st.write("By "+data["author"][int_val])
    datetime = st.write(data["datetime"][int_val])
    body = st.write(data["body"][int_val])
    article_url = st.write(data["url"][int_val])



def page_third():
    x=st.session_state.int
    st.session_state.int = x
    DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv"
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
        backend = f'https://news-analysis-px7gwe6txq-uk.a.run.app/economy/{}/sentiment'
        sentiment = process_sentiment(backend)
        st.write(sentiment)
        
    if nlp_option=="Summarization":
        st.write("# Summarization")
        backend = f'https://news-analysis-px7gwe6txq-uk.a.run.app/economy/{}/summarizer'
        summarize = process_summarization(backend)




@st.cache
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
    valid_result = result_dict["Sentiment"]
    return valid_result

@st.cache
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

@st.cache
def process_summarization(server_url: str):
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
    summ = result["summary_text"]
    return summ
        
if __name__ == "__main__":
    main()