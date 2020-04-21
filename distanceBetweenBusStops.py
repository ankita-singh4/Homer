def distanceBetweenBusStops(distance, start, destination):
    sumClockwise =0
    sumAntiClockwise = 0
    des = destination
    for i in range(0, des):
        sumClockwise += distance[i]
    for i in reversed(range(len(distance) - des)):
        print(i, len(distance))
        sumAntiClockwise += distance[i]
    print(sumAntiClockwise, sumClockwise)
    return min(sumClockwise, sumAntiClockwise)


distance = [1,2,3,4]
start = 0
destination = 3
print(distanceBetweenBusStops(distance, start, destination))
