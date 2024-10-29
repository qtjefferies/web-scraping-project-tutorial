import os
from bs4 import BeautifulSoup
import requests
import time
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

url = 'https://ycharts.com/companies/TSLA/revenues'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')
headers = [header.text for header in table.findAll('th')]
rows = table.find_all('tr')
    
    
data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    if cols:  # Only add rows with data
        data.append(cols)

# Step 5: Convert the extracted data into a pandas DataFrame
df = pd.DataFrame(data, columns=headers)

# Display the DataFrame
print(df)