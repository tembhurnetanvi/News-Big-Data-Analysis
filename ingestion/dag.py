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
import requests


def connect_GCS():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
# creds=Credentials.from_authorized_user_file("teak-formula-328301-c42aa6510882.json")
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    print('Successful connection')

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
    df_politics.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Politics.csv')

def CNN_Politics_to_GCS():
    df_politics= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Politics.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_politics.to_csv('gs://storm_event/CNN/CNN_Politics.csv')
    print('Successful upload')

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
    df_world.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_World.csv')

def CNN_World_to_GCS():
    df_world= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_World.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_world.to_csv('gs://storm_event/CNN/CNN_World.csv')
    print('Successful upload')

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
    df_us.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_US.csv')

def CNN_US_to_GCS():
    df_us= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_US.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_us.to_csv('gs://storm_event/CNN/CNN_US.csv')
    print('Successful upload')

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
    df_opinion.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Opinion.csv')

def CNN_Opinion_to_GCS():
    df_opinion= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Opinion.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_opinion.to_csv('gs://storm_event/CNN/CNN_Opinion.csv')
    print('Successful upload')        

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
    df_economy.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Economy.csv')

def CNN_Economy_to_GCS():
    df_economy= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Economy.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_economy.to_csv('gs://storm_event/CNN/CNN_Economy.csv')
    print('Successful upload')


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
    df_tech.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Tech.csv')

def CNN_Tech_to_GCS():
    df_tech= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Tech.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_tech.to_csv('gs://storm_event/CNN/CNN_Tech.csv')
    print('Successful upload')

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
    df_health.to_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Health.csv')

def CNN_Health_to_GCS():
    df_health= pd.read_csv('/mnt/c/DAGS/Project/cnn_data/CNN_Health.csv')
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="/mnt/c/DAGS/Google_Keys/teak-formula-328301-c42aa6510882.json" 
    storage_client = storage.Client(project="teak-formula-328301")
    bucket = storage_client.get_bucket('storm_event')
    df_health.to_csv('gs://storm_event/CNN/CNN_Health.csv')
    print('Successful upload')



with DAG(
    "gcs_cnn",
    start_date=dt.datetime(2021, 10, 10),
    schedule_interval='@once') as dag:

    t1 = PythonOperator(
        task_id="connect_to_gcs",
        python_callable=connect_GCS
    )

    t2 = PythonOperator(
        task_id="webscrape_CNN_Politics",
        python_callable=CNN_Politics
    )
    t3 =PythonOperator(
        task_id="CNN_Politics_to_GCS",
        python_callable=CNN_Politics_to_GCS
    )
    t4 = PythonOperator(
        task_id="webscrape_CNN_World",
        python_callable=CNN_World,
    )
    t5=PythonOperator(
        task_id="CNN_World_to_GCS",
        python_callable=CNN_World_to_GCS,
    )
    t6 = PythonOperator(
        task_id="webscrape_CNN_US",
        python_callable=CNN_US
    )
    t7 = PythonOperator(
        task_id='CNN_US_to_GCS',
        python_callable=CNN_US_to_GCS
    )
    t8 = PythonOperator(
        task_id='webscrape_CNN_Opinion',
        python_callable=CNN_Opinion
    )
    t9 = PythonOperator(
        task_id='CNN_Opinion_to_GCS',
        python_callable=CNN_Opinion_to_GCS
    )
    t10 = PythonOperator(
        task_id='webscrape_CNN_Economy',
        python_callable=CNN_Economy
    )
    t11 = PythonOperator(
        task_id='CNN_Economy_to_GCS',
        python_callable=CNN_Economy_to_GCS
    )
    t12 = PythonOperator(
        task_id='webscrape_CNN_Tech',
        python_callable=CNN_Tech
    )
    t13 = PythonOperator(
        task_id='CNN_Tech_to_GCS',
        python_callable=CNN_Tech_to_GCS
    )
    t14 = PythonOperator(
        task_id='webscrape_CNN_Health',
        python_callable=CNN_Health
    )
    t15 = PythonOperator(
        task_id='CNN_Health_to_GCS',
        python_callable=CNN_Health_to_GCS
    )

t1>>[t2, t4, t6, t8, t10, t12, t14]
t2>>t3
t4>>t5
t6>>t7
t8>>t9
t10>>t11
t12>>t13
t14>>t15

