import webbrowser, sys
import requests,bs4

import webbrowser, sys
import requests,bs4

res = open('E:\\my_cookboook\\flyingSaucer\\best-movies-html.html','rb')
soup = bs4.BeautifulSoup(res.read(),'lxml')
#print(soup.prettify())
title = soup.select('.list_header')
wt = soup.select('.list_movie_localized_name')

playFile = open('E:\\my_cookboook\\flyingSaucer\\movies.txt', 'wb')
for movie in wt:
    try:
        print(movie.getText())
        playFile.write(bytes(movie.getText(),'utf-8'))
        playFile.write(bytes('\n','utf-8'))	
    except Exception as exc:
        print(exc)