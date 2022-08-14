from traceback import print_tb
import uuid
import requests, urllib, datetime as dt, time
from progress.bar import Bar

q = str(input("Search : "))
pages = int(input("Pages : "))
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


# https://in.news.search.yahoo.com/search;_ylt=AwrKEtUwmPhi1ykfZHW7HAx.;_ylu=Y29sbwNzZzMEcG9zAzEEdnRpZAMEc2VjA3BpdnM-?p=morgan+stanley&fr2=piv-web&fr=sfp
# https://in.news.search.yahoo.com/search;_ylt=AwrXoCE1mPhiwQIAXCTAHAx.;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=morgan+stanley&fr=sfp&fr2=piv-web&b=11&pz=10&xargs=0
# https://in.news.search.yahoo.com/search;_ylt=AwrXoCFWmPhiXQMAgCHAHAx.;_ylu=Y29sbwNncTEEcG9zAzEEdnRpZAMEc2VjA3BhZ2luYXRpb24-?p=morgan+stanley&pz=10&fr=sfp&fr2=piv-web&b=21&pz=10&xargs=0