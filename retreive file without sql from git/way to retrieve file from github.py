import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account

url = "REPLACE-THIS-WITH-THE-URL-OF-THE-CSV-FILE" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print (df.head())