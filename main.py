import requests

class BusArrival:
    def __init__(self, busNumber, expectedArrivalTime):
        self.busNumber = busNumber
        self.expectedArrivalTime = expectedArrivalTime

def main():
    atcoCode = '490000077E'
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

    for bus in busInfo[:5]:
        print(f'Bus: {bus.busNumber} arriving at {bus.expectedArrivalTime}')

if __name__ == "__main__":
    main()
