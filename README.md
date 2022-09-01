# HHA 507 // Week 1 // Assignment 1

# hha-data-ingestion

## this repo contains a couple key components: data folder, keys folder, requirements txt, a py file, and this read me md.



## the py file contains three sections (not including the initial package import section). In the first section, we bring in two tabs of a single xlsx file as two different dataframes. this xlsx file is included in the data folder. All source files were taken from Kaggle

## the second section has us using requests for the first time to bring in open source json APIs via the web. 

## the third section involves connecting to GCP via client and querying two public bigquery datasets.

## keys folder holds our GCP service account's api key and is thus included in gitignore



## .JSON API KEY FORMAT
## {  "type": "service_account",
## "project_id": "hha-data-ingestion-360803",
##  "private_key_id":
##  "private_key":
##  "client_email":
##  "client_id":
##  "auth_uri": 
##  "token_uri": 
##  "auth_provider_x509_cert_url":
##  "client_x509_cert_url":
##  }



## requirements txt includes all the necessary packages to be installed via terminal based on the first week. only a handful are actually imported in python shell.

## THERE MAY BE A COMPATIBILITY ISSUE WITH DB-DTYPES. In order to resolve this when running section 3, run command 'pip install db-dtypes' in terminal prior.
