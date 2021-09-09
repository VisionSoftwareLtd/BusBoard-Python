from getBusInfo import getBusInfo

def main():
    atcoCode = '490000077E'
    busInfo = getBusInfo(atcoCode)

    for bus in busInfo[:5]:
        print(f'Bus: {bus.busNumber} arriving at {bus.expectedArrivalTime}')

if __name__ == "__main__":
    main()
