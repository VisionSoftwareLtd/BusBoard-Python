import requests

class BusArrival:
    def __init__(self, busNumber, expectedArrivalTime):
        self.busNumber = busNumber
        self.expectedArrivalTime = expectedArrivalTime

def getBusInfo(atcoCode):
    appId = 'f87f46ad'
    appKey = '053321f8d9a6af06b9c6227e9446f256'
    r = requests.get(f'http://transportapi.com/v3/uk/bus/stop/{atcoCode}/live.json?app_id={appId}&app_key={appKey}')
    response = r.json()
    departures = response["departures"]
    busInfo = []
    for departure in departures:
        for departureEntry in departures[departure]:
            busInfo.append(BusArrival(departure, departureEntry["expected"]["arrival"]["time"]))

    busInfo.sort(key=lambda busArrival: busArrival.expectedArrivalTime)

    return busInfo
