def checkStraightLine(coordinates):
    # print( coordinates[1][0], coordinates[0][0], coordinates[1][1], coordinates[0][1])
    try:
        gradient = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
    except:
        gradient = float("inf")
    for i in range(2, len(coordinates) -1):
        print(coordinates[i+1][0], coordinates[i][0], coordinates[i+1][1], coordinates[i][1])
        if gradient * (coordinates[i+1][0] - coordinates[i][0]) != coordinates[i+1][1]- coordinates[i][1]:
            return False
    return True


coordinates = [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]
print(checkStraightLine(coordinates))