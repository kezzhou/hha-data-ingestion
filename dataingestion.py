from termios import TAB1
import pandas as pd ##we import pandas to read the datasets we've compiled

df = pd.read_excel('/Users/kevinzhou/Documents/GitHub/hha-data-ingestion/data/data.xlsx', sheet_name=TAB1)