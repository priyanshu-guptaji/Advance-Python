import math

def getfare(source, destination):
    path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    stops = ["TH", "GA", "IC", "HA", "TE", "LU", "NI", "CA"]

    s = stops.index(source)
    d = stops.index(destination)

    distance = 0

    while s != d:
        distance += path[s]
        s += 1

        if s == len(stops):
            s = 0

    fare = math.ceil(distance * 5 / 1000)
    return fare


source = input()
destination = input()

print(getfare(source, destination))