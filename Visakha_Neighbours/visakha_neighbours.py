import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import json  # library to handle JSON files
# convert an address into latitude and longitude values# to get coordinates
# from geopy.geocoders import Nominatim
# tranform JSON file into a pandas dataframe
# from pandas.io.json import json_normalize
url = "https://en.wikipedia.org/wiki/Category:Neighbourhoods_in_Visakhapatnam"
html = urlopen(url)
soup = BeautifulSoup(html.read(), 'lxml')
type(soup)
alllinks = soup.find_all('a')
lst = []
for title in alllinks:
    lst.append(title.get_text())
lst
str_test = str(lst)
str_test
neighbor = pd.DataFrame(lst, columns=['Neighbours'])
new = neighbor.drop(neighbor.index[:9])
neigh = new.drop(new.index[121:])
final = neigh.reset_index(drop=True)
df = pd.DataFrame(final)
df.to_excel("data.xlsx")
