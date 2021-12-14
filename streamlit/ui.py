import streamlit as st
import pandas as pd

def main():
    pages = {
        "Welcome": page_first,
        "Article Selection": page_second,
        "Dashboard": page_third
    }

    if "page" not in st.session_state:
        st.session_state.update({
            # Default page
            "page": "Welcome",

            # Default widget values
            "text": "",

        })

    with st.sidebar:
        page = st.radio("Select your page", tuple(pages.keys()))

    pages[page]()


def page_first():
    st.subheader("Welcome!")
    st.markdown("____")
    st.header("News Analysis Application")
    st.markdown("____")
    st.subheader("This application helps to empower mind with day-to-day news.")
    st.write("This project for DAMG-7245 NEU guided by Prof. Krishna Murthy, made by Kartik Kumar and Tanvi Tembhurne")
    st.markdown("____")


def page_second():
    st.write('Please select the Category')
    pol=st.checkbox("Politics")
    # eco=st.checbox("Economy")
    if pol:
        DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv"
        data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
        data_pol = data[['title']]
        st.write('### Full Dataset', data_pol)
        int_val = st.number_input('Select a row for the article', min_value=0, max_value=49, value=5, step=1, key="text")
    else:
        st.write("No Categories Selected")
        # if eco:
        #     DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv"
        #     data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
        #     data_pol = data[['title']]
        #     st.write('### Full Dataset', data_pol)
        #     int_val = st.number_input('Select a row for the article', min_value=0, max_value=49, value=5, step=1, key="text")
        # else:
        #     st.write("No Categories Selected")


def page_third():
    x=st.session_state.text
    DATA_URL="https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv"
    data = st.cache(pd.read_csv)(DATA_URL, nrows=1000)
    st.header(data["title"][x])
    st.subheader(data["author"][x])
    st.write(data["datetime"][x])
    st.write(data["body"][x])
    st.write(data["url"][x])
    st.button("Summarization")
    st.button("Named Entity Recognization")
    st.button("Sentiment")



if __name__ == "__main__":
    main()
