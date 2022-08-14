import requests, urllib, datetime as dt, time
from progress.bar import Bar
import uuid

q = ''
while len(q) < 3:
    q = str(input("Search : "))

pages = input("Pages : ")
while len(pages) < 1:
    pages = input("Pages : ")

pages = int(pages)

results_per_page = 10
token = str(uuid.uuid4())

with Bar('Processing', max=pages) as bar:
    for i in range(0, pages):
        f = {'q' : q, 'source': 'lnms', 'tbm': 'nws', 'start':  results_per_page * i}
        url = "https://www.google.com/search?" + urllib.parse.urlencode(f)
        r = requests.get(url, allow_redirects=True)
        open('data/' + token + '_' + q.replace(' ','_') + '__' + str(dt.datetime.now()) + '.html', 'wb').write(r.content)
        # print("page scanned : {page} ".format(page=i))
        bar.next()

print("Done.\ttoken : {}".format(token))