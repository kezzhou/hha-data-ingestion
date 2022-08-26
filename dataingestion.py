##### importing necessary packages #####

import pandas as pd ##import pandas to read xlsx source data tabs
import requests as rq
import json




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

