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
        'limit':300
    }

    try: 
        response=requests.get(URL,params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except response.requests.exception.RequestException as error:
        print('Could not Fetch Data')
        return None

if __name__ == '__main__':
    data=fetch_earthquakes()
    


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

def filter_pakistan(quakes):
    return [q for q in quakes if "Pakistan" in q["place"]]


if __name__ == "__main__":
    data = fetch_earthquakes()
    if data is None:
        raise SystemExit(1)
    quakes = parse_earthquakes(data)
    quakes = filter_pakistan(quakes)
    quakes.sort(key=lambda q: q["magnitude"], reverse=True)

    print("Recent Earthquakes near Pakistan")
    print("--------------------------------")
    for q in quakes:
        print(q["magnitude"], "|", q["place"], "|", q["time"])