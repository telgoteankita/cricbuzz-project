import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
url = "https://www.cricbuzz.com/cricket-match/live-scores"

# Step 2: Add headers (important)
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Step 3: Get webpage
response = requests.get(url, headers=headers)

# Step 4: Convert into readable format
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Print title
print("Page Title:", soup.title.text)


import requests
from bs4 import BeautifulSoup

url = "https://www.cricbuzz.com/cricket-series/ipl-2026"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Step: Find all match titles
import pandas as pd   # add at top if not added

print("\nClean Match Data:\n")

text = soup.get_text(separator="\n")
lines = text.split("\n")

matches = []

for line in lines:
    line = line.strip()
    
    if " vs " in line:
        matches.append(line)

# Convert to DataFrame
df = pd.DataFrame(matches, columns=["Match"])

print(df)

# Split Match column into Team1 and Team2
df[['Team1', 'Team2']] = df['Match'].str.split(' vs ', expand=True)

print("\nSplit Data:\n")
print(df)    


# Split Match column into Team1 and Team2
df[['Team1', 'Team2']] = df['Match'].str.split(' vs ', expand=True)

print("\nSplit Data:\n")
print(df)

# Save to CSV
df.to_csv("matches.csv", index=False)

print("\nData saved to matches.csv")

