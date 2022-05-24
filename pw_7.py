from flask import Flask
from geopy.geocoders import Nominatim
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def index():

    return "I wait u requests, he-he."


@app.route("/<cityname>")
def timezone(cityname):
    try:
        geolocator = Nominatim(user_agent="My_city")
        location = geolocator.geocode(cityname)
        url = f"http://api.timezonedb.com/v2.1/get-time-zone?key=WL15T3PNNA75&format=json&by=position&lat={location.latitude}&lng={location.longitude}"
        req = requests.get(url)
        data = req.json()
        gmt = int(data.get("gmtOffset") / 3600)
        gmt_str = f"UTC/GMT +{gmt}.00 hours"
        dst = "Yes" if data.get("dst") == "1" else f"No"
        time = datetime.utcfromtimestamp(data.get("timestamp")).strftime("date:%Y-%m-%d | time:%H:%M:%S")
        end = (f"Current Time = {time} | Time Zone = {data.get('zoneName')} |\
               GMT Offset = {gmt_str} |  DST = {dst} |\
               Country = {data.get('countryName')} | City = {data.get('cityName')} |\
               Region = {data.get('regionName')}")
        return end
    except True:
        return "Something went wrong, he-he."


if __name__ == '__main__':
    app.run()
