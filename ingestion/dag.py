import pandas as pd
from io import BytesIO
import os
from airflow import DAG
from google.cloud import storage
from airflow.operators.python import PythonOperator, task
from airflow.operators.bash import BashOperator
from google.oauth2.credentials import Credentials
import datetime as dt
import json
from google.cloud import secretmanager
client = secretmanager.SecretManagerServiceClient()
import requests


project_id="peak-text-334821"
# secret_id=""

# Build the resource name of the secret version.
# secret_name = f"projects/{project_id}/secrets/test-secret/versions/1"
# Access the secret version.
# secret_key = client.access_secret_version(request={"name": secret_name})
# payload = secret_key.payload.data.decode("UTF-8")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/home/airflow/gcs/data/peak-text-334821-eb7c45a6619a.json"
storage_client = storage.Client(project="peak-text-334821")
bucket = storage_client.get_bucket('news_articles_scraped')


def CNN_Politics(url="https://search.api.cnn.io/content?q=politics&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_politics = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_politics["category"] = 'politics'
    bucket.blob('CNN/politics.csv').upload_from_string(df_politics.to_csv(), 'text/csv')


def CNN_World(url="https://search.api.cnn.io/content?q=world&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_world = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_world["category"] = 'world'
    bucket.blob('CNN/world.csv').upload_from_string(df_world.to_csv(), 'text/csv')



def CNN_US(url="https://search.api.cnn.io/content?q=US&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_us = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_us["category"] = 'us'
    bucket.blob('CNN/us.csv').upload_from_string(df_us.to_csv(), 'text/csv')


def CNN_Opinion(url="https://search.api.cnn.io/content?q=opinion&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_opinion = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_opinion["category"] = 'opinion'
    bucket.blob('CNN/opinion.csv').upload_from_string(df_opinion.to_csv(), 'text/csv')

def CNN_Economy(url="https://search.api.cnn.io/content?q=economy&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_economy = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_economy["category"] = 'economy'
    bucket.blob('CNN/economy.csv').upload_from_string(df_economy.to_csv(), 'text/csv')



def CNN_Tech(url="https://search.api.cnn.io/content?q=tech&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_tech = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_tech["category"] = 'tech'
    bucket.blob('CNN/tech.csv').upload_from_string(df_tech.to_csv(), 'text/csv')

def CNN_Health(url="https://search.api.cnn.io/content?q=health&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"):
    data=[]
    with requests.Session() as req:
        for item in range(1, 1000, 100):
            try:
                r = req.get(url.format(item)).json()
                for a in r['result']:
                    if 'headline' in a.keys():
                        title=a['headline']
                    else:
                         title='Nan'   
                    if 'body' in a.keys():
                        body=a['body']
                    else:
                         title='Nan'
                    if 'lastPublishDate' in a.keys():
                        datetime=a['lastPublishDate']
                    else:
                         datetime='Nan'
                    if 'url' in a.keys():
                        url=a['url']
                    else:
                         url='Nan'
                    if 'byLine' in a.keys():
                        author=a['byLine']
                    else:
                         author='Nan'   
                    data.append([title, body, datetime, author, url])
            except:
                pass
    df_health = pd.DataFrame(data=data, columns=["title", "body", "datetime", "author", "url"])
    df_health["category"] = 'health'
    bucket.blob('CNN/health.csv').upload_from_string(df_health.to_csv(), 'text/csv')


with DAG(
    "gcs_cnn",
    start_date=dt.datetime(2021, 10, 10),
    schedule_interval='@once') as dag:


    t2 = PythonOperator(
        task_id="webscrape_CNN_Politics",
        python_callable=CNN_Politics
    )
    t4 = PythonOperator(
        task_id="webscrape_CNN_World",
        python_callable=CNN_World,
    )
    t6 = PythonOperator(
        task_id="webscrape_CNN_US",
        python_callable=CNN_US
    )
    t8 = PythonOperator(
        task_id='webscrape_CNN_Opinion',
        python_callable=CNN_Opinion
    )
    t10 = PythonOperator(
        task_id='webscrape_CNN_Economy',
        python_callable=CNN_Economy
    )
    t12 = PythonOperator(
        task_id='webscrape_CNN_Tech',
        python_callable=CNN_Tech
    )
    t14 = PythonOperator(
        task_id='webscrape_CNN_Health',
        python_callable=CNN_Health
    )

[t2, t4, t6, t8, t10, t12, t14]

