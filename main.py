import requests
from datetime import datetime, timezone

URL="https://earthquake.usgs.gov/fdsnws/event/1/query"

def fetch_earthquakes():
    params={
        'format':'geojson',
        'minlatitude':23,
        'maxlatitude':37,
        'minlongitude':60,
        'maxlongitude':78,
        'orderby':'time',
        'limit':10
    }

    response=requests.get(URL,params=params)
    return response.json()

if __name__ == '__main__':
    data=fetch_earthquakes()
    print(len(data['features']), 'earthquakes found')


def parse_earthquakes(data):
    quakes=[]

    for feature in data['features']:
        props=feature['properties']
        time=datetime.fromtimestamp(props['time']/1000, tz=timezone.utc)
        quakes.append({
            'magnitude': props['mag'],
            'place': props['place'],
            'time':time.strftime('%Y-%m-%d %H:%M'),
        })

    return quakes


if __name__ == '__main__':
    data=fetch_earthquakes()
    quakes=parse_earthquakes(data)
    print(len(quakes),' Earthquakes Found')
    for q in quakes:
         print(q["magnitude"], "|", q["place"], "|", q["time"])