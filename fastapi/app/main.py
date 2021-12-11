
import uvicorn
from fastapi import FastAPI
from starlette.responses import Response
from pydantic import BaseModel
from google.cloud import storage
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_md")


def ner_spacy(text):
    doc1 = nlp(text)
    for ent in doc1.ents:
        yield ent.text, ent.label_


app = FastAPI(
    title = "NEW API",
    description = "NER extracts labels from the text"
)

class Text(BaseModel):
    text: str

@app.get("/")
def read_root():
     
    return {"message": "Welcome from the API"}

@app.get("/read")
def read_df():
    df = pd.read_csv('https://storage.googleapis.com/digital-sprite-299519/squark_churn_training_data.csv')
    print(df.head())
    sample_list = list(df.head())
    return {"df head": sample_list}

# @app.post("/summary")
# def get_summary(text: Text):
#     """Get summary from text"""
#     # print(text.text)
#     summary = summarize(text.text)
#     # summary = summarize(text)
#     result = {"Summary from transformers": summary}
#     return result

@app.post("/ner")
def get_ner(text: Text):
    """Get ner from text"""
    # print(text.text)
    output_spacy = list(ner_spacy(text.text))
    # output_spacy = list(ner_spacy(text))
    result = {"NER from Spacy": output_spacy}
    return result


@app.get('/ner')
def ner_text(text: str):
    output_spacy = list(ner_spacy(text))
    result = {"NER from Spacy": output_spacy}
    return result

# @app.get('/summary')
# def summarize_text(text: str):
#     summary = summarize(text)
#     result = {"Summary from transformers": summary}
#     return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)