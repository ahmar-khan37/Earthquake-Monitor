import requests

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