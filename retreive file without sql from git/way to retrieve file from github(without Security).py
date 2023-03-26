import pandas as pd
import requests
import io

# Username of your GitHub account

username = 'REPLACE-THIS-WITH-YOUR-GITHUB-ACCOUNT-USERNAME'

# Personal Access Token (PAO) from your GitHub account

token = 'REPLACE-THIS-WITH-YOUR-GITHUB-ACCOUNT-PAO'

# Creates a re-usable session object with your creds in-built

github_session = requests.Session()
github_session.auth = (username, token)
    
# Downloading the csv file from your GitHub

url = "REPLACE-THIS-WITH-THE-LINK-OF-THE-CSV-FILE" # Make sure the url is the raw version of the file on GitHub
download = github_session.get(url).content

# Reading the downloaded content and making it a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe to make sure everything is good

print (df.head())