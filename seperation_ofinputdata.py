class Device:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng


def seperation(data):
    ans = []
    imi_no = ""
    lat = ""
    lon = ""
    n = len(data)
    for i in range(6, n):
        if(data[i] == ','):
            break
        imi_no = imi_no + data[i]
    for i in range(i + 11, i + 20):
        lat = lat + data[i]
    for i in range(i + 1, i + 10):
        lon = lon + data[i]
    lonf = float(lon)
    latf = float(lat)
    lonf = lonf / 10000000
    latf = latf / 10000000
    ans = Device("", 0.0, 0.0)
    ans.name = imi_no
    ans.lat = latf
    ans.lng = lonf
    return ans


def execution(file):
    lines = []
    for line in file:
        lines.append(line)
    data = lines[0]
    ans = seperation(data)
    return ans
