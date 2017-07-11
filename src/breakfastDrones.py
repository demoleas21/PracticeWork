def findMissingDrone(listOfIds):
    droneCount = {}
    for drone in listOfIds:
        droneCount[str(drone)] = droneCount.get(str(drone), 0) + 1
    for uniqueKey in droneCount:
        if droneCount[uniqueKey]:
            return uniqueKey
    return None


def main():
    delivery_id_confirmations = [1, 5, 5, 4, 4, 4, 4, 1, 3, 2, 2]
    print findMissingDrone(delivery_id_confirmations)

main()
