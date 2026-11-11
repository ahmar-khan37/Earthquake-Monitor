Earthquake Monitor

A small Python tool that fetches live earthquake data from the USGS API and lists recent earthquakes near Pakistan, strongest first.

Features
- Fetches live data from the USGS Earthquake API
- Filters earthquakes located in Pakistan
- Shows magnitude, place and time (UTC)
- Sorts results by magnitude
- Handles network and API errors gracefully

Installation

```
git clone https://github.com/ahmar-khan37/Earthquake-Monitor.git
cd Earthquake-Monitor
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Usage

```
python main.py
```

Sample Output

```
Recent Earthquakes near Pakistan
--------------------------------
5.7 | 47 km WNW of Khuzdar, Pakistan | 2026-10-17 05:06
4.4 | 31 km SE of Dalbandin, Pakistan | 2026-10-22 23:26
4.3 | 26 km SSW of Sann, Pakistan | 2026-10-26 05:45
```

Data Source
[USGS Earthquake Catalog API](https://earthquake.usgs.gov/fdsnws/event/1/)
