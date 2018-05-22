class Device:
    def __init__(self, name, lat, lng):
        self.name = name
        self.lat = lat
        self.lng = lng


def convertor(degg):
    a = ""
    b = ""
    c = ""
    for i in range(0, 2):
        a = a + degg[i]
    print(a)
    for i in range(2, 4):
        b = b + degg[i]
    print(b)
    for i in range(4, 9):
        c = c + degg[i]
    print(c)
    c1 = float(c)
    c1 = c1 / 1000
    c1 = float(a) + float(b) / 60 + c1 / 3600
    print(c1)
    return c1


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
    lonf = convertor(lon)
    latf = convertor(lat)
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

