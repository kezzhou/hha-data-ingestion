##### importing necessary packages #####

import pandas as pd ## import pandas to read xlsx source data tabs
import requests as rq ## used to pull api datasets from the web
import json ## used to visualize public api datasets
from google.cloud import bigquery




##### section 1 - reading xlsx files with pandas #####

tab1 = pd.read_excel('/Users/kevinzhou/Documents/GitHub/hha-data-ingestion/data/data.xlsx', sheet_name='tab1') ## here we use pandas or pd to read the first sheet of our data source xlsx file

tab1 ## df function helps us to visualize how it will look

tab2 = pd.read_excel('/Users/kevinzhou/Documents/GitHub/hha-data-ingestion/data/data.xlsx', sheet_name='tab2') ## we repeat defining the function df but this time with tab2

tab2 ## we execute df again here to visualize the tab2 dataset




##### section 2 - bringing in public API datasets with requests #####

apiDataset = rq.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data') ## we bring in public cms json api with requests and the appropriate url

apiDataset = apiDataset.json() ## we then use json package to visualize api dataset for us

apiDataset ## we can then simply run the function to see the results




##### section 3 - bigquery datasets #####

client = bigquery.Client.from_service_account_json('/Users/kevinzhou/Documents/GitHub/hha-data-ingestion/keys/hha-data-ingestion-360803-a453da9d036b.json') ## here we create a client to essentially log into our gcp and access the respective project the service account governs

query_job = client.query("SELECT * FROM `hha-data-ingestion-360803.us_census_data.population_by_zip_2000` LIMIT 100") ## here we use client query which wraps an sql query that selects all columns from the us census public dataset I've chosen to use. The selection is limited to the first 100 rows

results = query_job.result() ## results is defined as a function that displays the results of our above query

bigquery1 = pd.DataFrame(results.to_dataframe()) ## the above results are then framed within a dataframe with this function


## here we can repeat these steps a second time with a second public bigquery dataset that was added to the gcp project

query_job = client.query("SELECT * FROM `hha-data-ingestion-360803.historical_air_quality.air_quality_annual_summary` LIMIT 100") ## this time we use a dataset about air quality

results = query_job.result()

bigquery2 = pd.DataFrame(results.to_dataframe())

## when attempting to run lines 43 or 52, error quotes needing to install db_dtypes even though when install is run in terminal, it reports already fulfilled.
## this may be a compability issue