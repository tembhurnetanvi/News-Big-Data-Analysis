import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response
from pydantic import BaseModel
from google.cloud import storage
import spacy
import pandas as pd
import json
from sentiment import process_sentiment
from gtts import gTTS
import os
from transformers import pipeline

summarizer1 = pipeline("summarization",model="t5-small", tokenizer="t5-small")

summarizer2 = pipeline("summarization")


# from google.cloud import secretmanager

# project_id = "90036660605"

# client = secretmanager.SecretManagerServiceClient()
# name = f"projects/{project_id}/secrets/app-key/versions/1"
# response = client.access_secret_version(name=name)
# my_secret_value = response.payload.data.decode("UTF-8")
# with open("./app-key.json", 'w') as f:
#     json.dump(my_secret_value, f)


# # def secret_hello(request):
# #     if "Again" in my_secret_value:
# #         return "We meet again!\n"

# #     return "Hello there.\n"
    
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./app-key.json"


def parse_dataframe(df):
    result = df.to_json(orient="records")
    parsed=json.loads(result)
    return parsed


app = FastAPI(
    title = "NEW API",
    description = "API helps analyze news articles"
)

# class Text(BaseModel):
#     text: str

@app.get("/")
def read_root():     
    return {"message": "Welcome from the API"}


# POLITICS
@app.get("/politics/{row_id}")
def read_politics(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/politics/{row_id}/sentiment")
def politics_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}

@app.post("/politics/{row_id}/text-to-speech")
def politics_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./politics_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'politics/{row_id}.mp3')
    blob.upload_from_filename(f'./politics_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./politics_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/politics/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}
# WORLD
@app.get("/world/{row_id}")
def read_world(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/world.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/world/{row_id}/sentiment")
def world_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/world.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}

@app.post("/world/{row_id}/text-to-speech")
def world_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/world.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./world_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'world/{row_id}.mp3')
    blob.upload_from_filename(f'./world_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./world_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/world/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/world.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']

    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}


# ECONOMY
@app.get("/economy/{row_id}")
def read_economy(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/economy/{row_id}/sentiment")
def economy_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}


@app.post("/economy/{row_id}/text-to-speech")
def economy_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./economy_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'economy/{row_id}.mp3')
    blob.upload_from_filename(f'./economy_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./economy_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/economy/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']

    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}


# HEALTH
@app.get("/health/{row_id}")
def read_health(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/health.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/health/{row_id}/sentiment")
def health_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/health.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}


@app.post("/health/{row_id}/text-to-speech")
def health_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/health.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./health_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'health/{row_id}.mp3')
    blob.upload_from_filename(f'./health_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./health_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/health/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/health.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']

    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}

# TECH
@app.get("/tech/{row_id}")
def read_tech(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/tech.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/tech/{row_id}/sentiment")
def tech_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/tech.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}


@app.post("/tech/{row_id}/text-to-speech")
def tech_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/tech.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./tech_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'tech/{row_id}.mp3')
    blob.upload_from_filename(f'./tech_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./tech_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/tech/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/tech.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']

    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}

# USA
@app.get("/us/{row_id}")
def read_us(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/us.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/us/{row_id}/sentiment")
def us_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/us.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}


@app.post("/us/{row_id}/text-to-speech")
def us_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/us.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./us_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'us/{row_id}.mp3')
    blob.upload_from_filename(f'./us_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./us_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/us/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/us.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']

    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}

#OPINION
@app.get("/opinion/{row_id}")
def read_opinion(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/opinion.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/opinion/{row_id}/sentiment")
def opinion_sentiment(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/opinion.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    sentiment_result = process_sentiment(body)
    return {"sentiment": sentiment_result}


@app.post("/opinion/{row_id}/text-to-speech")
def opinion_tts(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/opinion.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    tts = gTTS(body)
    tts.save(f'./opinion_{row_id}.mp3')
    storage_client = storage.Client()
    buckets = list(storage_client.list_buckets())
    bucket = storage_client.get_bucket("audio-output")
    blob = bucket.blob(f'opinion/{row_id}.mp3')
    blob.upload_from_filename(f'./opinion_{row_id}.mp3')
    blob.make_public()
    os.remove(f'./opinion_{row_id}.mp3')
    return {"Save": "Successful"}

@app.post("/opinion/{row_id}/summarizer")
def summarizers(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/opinion.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']

    if len(body)>=5000:
        
        summ1=summarizer1(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary":summ1}
    else:
        summ2=summarizer2(body,  max_length=130, min_length=30, do_sample=False)
        return {"summary": summ2}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)