'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''
from seperation_ofinputdata import seperation, execution
from flask import Flask, render_template, abort

app = Flask(__name__)


class Device:
    def __init__(self, key, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng


class School:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng


file = open("userlist.txt", "r")
ans = Device("", 0.0, 0.0, 0.0)
ans = execution(file)
schools = School('hv', ans.name, ans.lat, ans.lng)
#schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    return render_template('map.html', school=schools)


app.run(host='localhost', debug=True)
