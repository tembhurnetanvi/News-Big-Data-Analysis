import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import Response
from pydantic import BaseModel
from google.cloud import storage
import spacy
import pandas as pd
import json
from ner import ner_spacy
# from summarizer import summarize

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


@app.post("/politics/{row_id}/ner")
def politics_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}

# @app.post("/politics/{row_id}/summary")
# def politics_ner(row_id: int):
#     df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/politics.csv', index_col=0)
#     new_df = df.filter(items = [row_id], axis=0)
#     parsed_row = parse_dataframe(new_df)
#     body = parsed_row[0]['body']
#     summary = summarize(body)
#     return {"TF summary": summary}

# WORLD
@app.get("/world/{row_id}")
def read_world(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/world.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/world/{row_id}/ner")
def world_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/world.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}


# ECONOMY
@app.get("/economy/{row_id}")
def read_economy(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/economy/{row_id}/ner")
def economy_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/economy.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}


# HEALTH
@app.get("/health/{row_id}")
def read_health(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/health.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/health/{row_id}/ner")
def health_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/health.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}


# TECH
@app.get("/tech/{row_id}")
def read_tech(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/tech.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/tech/{row_id}/ner")
def tech_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/tech.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}


# USA
@app.get("/us/{row_id}")
def read_us(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/us.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/us/{row_id}/ner")
def us_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/us.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}


#OPINION
@app.get("/opinion/{row_id}")
def read_opinion(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/opinion.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    return {"df": parsed_row}


@app.post("/opinion/{row_id}/ner")
def opinion_ner(row_id: int):
    df = pd.read_csv('https://storage.googleapis.com/news_articles_scraped/CNN/opinion.csv', index_col=0)
    new_df = df.filter(items = [row_id], axis=0)
    parsed_row = parse_dataframe(new_df)
    body = parsed_row[0]['body']
    entities = ner_spacy(body)
    return {"entities": entities}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)