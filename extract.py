import requests
import pandas as pd
from sqlalchemy import create_engine

# API URL
url =  "https://jsonplaceholder.typicode.com/users"

# Data Extraction
response = requests.get(url)

data = response.json()

# Conversion to Dataframe : as data is list of dictonaries
users = []

for user in data :
    users.append({
        "id" : user["id"],
        "name" : user["name"],
        "username" : user["username"],
        "email" : user["email"],
        "city" :user["address"]["city"]
    })

df = pd.DataFrame(users)

# DB Connection
engine = create_engine("postgresql+psycopg2://postgres:root@localhost:5433/etl_demo")

# Load Data into DB
df.to_sql("raw_users", engine, if_exists="append", index=False)

print("Data Loaded Successfully")