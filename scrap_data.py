import datetime as dt, pandas as pd, json, os
from bs4 import BeautifulSoup
from progress.bar import Bar


data = []

def scrap_data(file_name):
    file = open("data/" + file_name, "r", encoding="ISO-8859-1")
    # print(file.name)
    soup = BeautifulSoup(file, 'html.parser')
    file.close()

    h3hld = soup.find_all('h3')
    deschdl = soup.find_all('div', class_="BNeawe s3v9rd AP7Wnd")

    for i in range(0, len(h3hld)):
        data.append({
            'title': h3hld[i].text,
            'description': deschdl[i * 2].text
        })

files = os.listdir("./data/")

with Bar('Processing', max = len(files)) as bar:
    for fl in files:
        scrap_data(fl)
        bar.next()

df = pd.read_json(json.dumps(data))
ofname = input('Save as (Default: current timestamp)\t: ')
if len(ofname) < 3:
    ofname = 'scrp_'+str(dt.datetime.now())+'.csv'
else:
    ofname += '.csv'
df.to_csv(ofname, encoding='utf-8')