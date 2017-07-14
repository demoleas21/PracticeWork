def findMissingDrone(listOfIds):
    droneCount = {}
    for drone in listOfIds:
        droneCount[str(drone)] = droneCount.get(str(drone), 0) + 1
    for uniqueKey in droneCount:
        if droneCount[uniqueKey] == 1:
            return int(uniqueKey)
    return None
