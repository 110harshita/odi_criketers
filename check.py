import csv
import bs4 as bs
import urllib.request
import pandas as pd
import pip
import linecache

def max(line):
    str='https://en.wikipedia.org/wiki/List_of_'+line+'_ODI_cricketers'
    print(str)
    return str

def scrapped_data(line,string,i):
    sauce = urllib.request.urlopen(max(line)).read()
    soup = bs.BeautifulSoup(sauce, "html.parser")
    my_table = soup.find_all("table", class_="wikitable")[0]
    # my_table = soup.select('table.wikitable')[0]
    table_rows = my_table.find_all('tr')
    for tr in table_rows[2:]:
        try:
            f1_col = tr.find_all('a')[0].contents
            f4_col = tr.find_all(string)[i].contents
        except Exception as e:
            continue
        L = f1_col+f4_col
        L[-1] = L[-1].rstrip('\n')
        print(L)
        df_list.append(L)

df_list=[]
with open('countryname.txt', 'r') as csv_file:
    for line in csv_file:
        m = (line.count(','))
for i in range(m + 1):
    file = open('countryname.txt', 'r')
    for line in file.readlines():
        fname = line.rstrip().split(',')
    line = fname[i]
    print(line)
    if line in ("Canada","India","England","Ireland","Kenya","Namibia","Nepal","Netherlands","Oman","Papua_New_Guinea","Scotland","United_Arab_Emirates","United_States"):
        scrapped_data(line,'td', 4)
    elif line in ("Afghanistan","Hong_Kong"):
        scrapped_data(line,'span',4)
    elif line in ("African_XI","Bangladesh","Australia","New_Zealand","Pakistan","South_Africa","Sri_Lanka","West_Indies","Zimbabwe"):
        scrapped_data(line,'td',5)
    elif line in ("Bermuda"):
        scrapped_data(line,'span',6)
    else:
        scrapped_data(line,'td',6)

df_list = pd.DataFrame(df_list)
df_list.to_csv('odicriketers.csv', mode='w', header=False)
data = pd.read_csv('odicriketers.csv')
data.shape
print(df_list)
