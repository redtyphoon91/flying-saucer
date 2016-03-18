import webbrowser, sys
import requests,bs4
wt = "http://forecast.weather.gov/MapClick.php?lat=37.789425695040904&lon=-122.39481252507727#.VucCFkJ97cc"
#webbrowser.open(maps)
res = requests.get(wt)
try:
    res.raise_for_status()
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise    
except Exception as exc:
    print('There was a problem: %s' % (exc))
else:
    print arg, 'has', len(f.readlines()), 'lines'
    f.close()

#print(res.text[:250])
soup = bs4.BeautifulSoup(res.text,"lxml")
wt = soup.select('#current_conditions-summary')
print(wt)

wty = soup.select('[class=panel-title]')
print(wty[0].getText())

#print(elems[0])
#xpath - //*[@id="current_conditions-summary"]