import webbrowser, sys
import requests,bs4
wt = "http://goodmovieslist.com/best-movies/best-movies-of-2015.html"
res = requests.get(wt)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

playFiles = open('E:\\my_cookboook\\flyingSaucer\\best-movies-html.txt', 'wb')
for chunk in res.iter_content(100000):
        playFiles.write(chunk)
        