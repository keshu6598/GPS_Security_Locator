from seperation_ofinputdata import seperation, execution


class Device:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng


file = open("userlist.txt", "r")
ans = Device("", 0.0, 0.0)
ans = execution(file)
print(ans.name)
print(ans.lat)
print(ans.lng)
