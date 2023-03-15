import requests
import pandas as pd
from bs4 import BeautifulSoup
from web_scrapping_news.new import New

response = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(response.content, "html5lib")
titles = soup.findAll("span", attrs={"class": "titleline"})
subtexts = soup.findAll("td", attrs={"class": "subtext"})
elements = {"title": [], "score": [], "date": [], "comments": []}

for i in range(len(titles)):
    element = New(titles[i], subtexts[i])

    elements["title"].append(element.title)
    elements["score"].append(element.score)
    elements["date"].append(element.date)
    elements["comments"].append(element.comments)

df_info = pd.DataFrame(elements)
# Muestra algo de info
print(df_info.head())
# Muestra las columnas
print(df_info.info())
# Convierte el dataframe en u ncsv
df_info.to_csv("news.csv", encoding="utf-8")
# Lo mismo que el anterior, pero sin indices
df_info.to_csv("news_no_index.csv", index=False, encoding="utf-8")
