'''
A Web application that shows Google Maps around schools, using
the Flask framework, and the Google Maps API.
'''
from seperation_ofinputdata import seperation, execution
from flask import Flask, render_template, abort
from server import SERVER

app = Flask(__name__)


class Device:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng


class School:
    def __init__(self, key, name, lat, lng):
        self.key = key
        self.name = name
        self.lat = lat
        self.lng = lng


#schools_by_key = {school.key: school for school in schools}


@app.route("/")
def index():
    while True:

      text =str(SERVER())
      #file = open("userlist.txt", "r")
      print(text)
      ans = Device("", 0.0, 0.0)
      #ans = execution(file)
      ans = seperation(text)
      schools = School('hv', ans.name, ans.lat, ans.lng)
      return render_template('map.html', school=schools)


#app.run(host='localhost', debug=True)
if __name__=='__main__':
    #socketio.run(app, host='192.168.110.90',port=4000)
    app.run('192.168.110.90',4000) 

