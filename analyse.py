import lxml.html
import bs4 as bs
import urllib.request
import pandas as pd
import csv
import json

def max(line):
    str='http://www.howstat.com/cricket/Statistics/Players/PlayerYears_ODI.asp?PlayerID=' +line
    print(str)
    return str

def scrapped_data(line):
    try:
        m=max(line)
        t = lxml.html.parse(m)
        sauce = urllib.request.urlopen(m).read()
        soup = bs.BeautifulSoup(sauce, "html.parser")
        my_table = soup.find_all("table", class_="TableLined")[0]
        table_rows = my_table.find_all('tr')
        for tr in table_rows[1:]:
            title=[]
            tittle = t.find(".//title").text
            title.append(tittle)
            f1_col = tr.find_all('a')[0].contents
            f4_col = tr.find_all('td')[7].contents
            f4_col_1 = [i.replace('\r\n', '') for i in f4_col]
            print(f4_col_1)
            print(f1_col)
            print(title)
            L = title+f1_col+f4_col_1
            L[-1] = L[-1].rstrip('\n')
            print(L)
            df_list.append(L)
    except Exception as e:
        print(" ")

df_list=[]
with open('playerid.txt', 'r') as csv_file:
    for line in csv_file:
        m = (line.count(','))
for i in range(m + 1):
    file = open('playerid.txt', 'r')
    for line in file.readlines():
        fname = line.rstrip().split(',')  # using rstrip to remove the \n
    line = fname[i]
    print(line)
    scrapped_data(line)
df_list = pd.DataFrame(df_list)
df_list.to_csv('odi.csv', mode='w', header=False)
data = pd.read_csv('odi.csv')
with open('odi.csv',newline='') as f:
    r = csv.reader(f)
    data = [line for line in r]
f = open( 'odi.csv', 'rU' )
reader = csv.DictReader( f, fieldnames = ('sr_no','name_of_the_player','year','runs'))
out = json.dumps( [ row for row in reader ] )
print ("JSON parsed!"  )
f = open( 'parsed.json', 'w')
f.write(out)
print ("JSON saved!")
print(df_list)