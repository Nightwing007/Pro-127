from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

table = requests.get(url)
print(table)

soup = bs(table.text,'html.parser')

star_table = soup.find('table')

temp_l= []
t_row = star_table.find_all('tr')

for tr in t_row:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_l.append(row)



Star_names = []
Distance =[]
Mass = []
Radius =[]
Lum = []

for i in range(1,len(temp_l)):
    Star_names.append(temp_l[i][1])
    Distance.append(temp_l[i][3])
    Mass.append(temp_l[i][5])
    Radius.append(temp_l[i][6])
    Lum.append(temp_l[i][7])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('bright_stars.csv')