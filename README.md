# hha-data-ingestion

## this repo contains a couple key components: data folder, keys folder, requirements txt, a py file, and of course this read me mark down.



## the py file contains three sections (not including the initial package import section). In the first section, we bring in two tabs of a single xlsx file as two different dataframes. this xlsx file is included in the data folder. All source files were taken from Kaggle

## the second section has us using requests for the first time to bring in open source json APIs via the web. 

## the third section involves connecting to GCP via client and querying two public bigquery datasets.



## keys folder holds our GCP service account's api key and is thus included in gitignore

## requirements txt includes all the necessary packages to be installed via terminal based on the first week. only a handful are actually imported in python shell.