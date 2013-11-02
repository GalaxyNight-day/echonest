import os
from pyechonest import config
config.ECHO_NEST_API_KEY="NGUUJCPVC61WKHRKN"
import datetime

import urllib
from pandas import DataFrame
from datetime import datetime, timedelta
from pytz import timezone
import pytz
import urllib
from pandas import read_html

from pandas import read_csv
from StringIO import StringIO
import requests
url='https://docs.google.com/spreadsheet/pub?key=0AphHrqy-sY9gdE9RalNhR0FEb1RMMkp5cWRadkVwVEE&output=csv'
r=requests.get(url)
data = r.content
df = read_csv(StringIO(data))


import sys
from pyechonest import song

def get_tempo(artist, title):
    "gets the tempo for a song"
    results = song.search(artist=artist, title=title, results=1, buckets=['audio_summary'])
    if len(results) > 0:
        return results[0].audio_summary
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) <> 3:
        print "Usage: python tempo.py 'artist name' 'song title'"
    else:
        tempo = get_tempo(sys.argv[1], sys.argv[2])
        if tempo:
            print 'Tempo for', sys.argv[1], sys.argv[2], 'is', tempo
        else:
            print "Can't find Tempo for artist:", sys.argv[1], 'song:', sys.argv[2]
        



datetime.datetime.now()


from pandas import *
import numpy
fill=numpy.zeros(5427).reshape((603, 9))


past=datetime.datetime.now()
now=datetime.datetime.now()


past=datetime.datetime.now()
now=datetime.datetime.now()
k=589
flag=1
while (flag==1) :
    import datetime
    if(((now.second+now.minute*60)) > (past.second+past.minute*60)+61) : 
        n=k
        m=n+19
        past=datetime.datetime.now()

        for i in range(n,m):
        
            meta=get_tempo(df['artist'][i],df['song'][i])
        
        
            if((meta)==None):
                print('no')
                
            else:
                Src=array([meta['energy'],meta['liveness'],meta['tempo'],meta['speechiness'],meta['acousticness'],meta['duration'],meta['loudness'],meta['valence'],meta['danceability']])
                fill[i,]=Src
        k=k+19
        if(k>622) :
            flag=0
    else : 
        now=datetime.datetime.now()
                
                
                
                
                
