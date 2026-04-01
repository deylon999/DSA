stations = [120, 260, 410, 560, 730, 890, 1040, 1190, 1360, 1520, 1680, 1840, 
            2010, 2170, 2330, 2480, 2650, 2810, 2970, 3140, 3300, 3460, 3630, 
            3790, 3950, 4120, 4280, 4440, 4610, 4770, 4930, 5100, 5260, 5420, 
            5590, 5750, 5910, 6080, 6240, 6400, 6570, 6730, 6890, 7060, 7220, 
            7380, 7550, 7710, 7870, 8040, 8200, 8360, 8530, 8690, 8850, 9020, 
            9180, 9340, 9510, 9670, 9830, 10000, 10160, 10320]

def min_stops(stations, total, tank):
    all_stations = [0] + stations + [total]
    for i in range(1, len(all_stations)):
        if all_stations[i] - all_stations[i-1] > tank:
            print("Маршрут невозможен: расстояние между заправками превышает запас хода")
            return None
    
    stops = []
    current = 0
    idx = 0
    
    while current < total:
        farthest_idx = idx
        farthest_dist = current
        for j in range(idx + 1, len(all_stations)):
            if all_stations[j] - current <= tank:
                farthest_idx = j
                farthest_dist = all_stations[j]
            else:
                break
        
        if farthest_idx == idx:
            print("Маршрут невозможен: недостаточно топлива")
            return None
        
        if farthest_dist >= total:
            break
        stops.append(farthest_dist)
        current = farthest_dist
        idx = farthest_idx
    
    return stops

total_distance = 10451
tank_capacity = 500

result = min_stops(stations, total_distance, tank_capacity)

if result:
    print(f"Количество остановок: {len(result)}")
    print(f"Заправки на расстояниях: {result}")