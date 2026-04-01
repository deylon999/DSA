def min_stops(stations, total, tank):
    stops = []
    current = 0

    stations = [0] + stations + [total]

    for i in range(1, len(stations)):
        if stations[i] - stations[i-1] > tank:
            print("маршрут возможен")
            return None
    
    while current < total:
        farthest = current
        next_stop = -1
        for j in range(i+1, len(stations)):
            if stations[j] - current <= tank:
                farthest = stations[j]
                next_stop = j
            else:
                break
        
        if next_stop == -1 or farthest == current:
            print("маршрут невозможен")
            return None

        if farthest < total:
            stops.append(farthest)
        current = farthest
        i = next_stop
    
    return stops