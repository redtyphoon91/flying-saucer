import webbrowser, sys
import requests
maps = "https://automatetheboringstuff.com/files/rj.txt"
#webbrowser.open(maps)
res = requests.get(maps)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
#print(res.text[:250])
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)