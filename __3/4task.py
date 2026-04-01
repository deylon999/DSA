def greedy_schedule(events):
    events.sort(key= lambda x: x['end'])

    selected = []
    last_end = 0

    for event in events:
        if event['start'] >= last_end:
            selected.append(event)
            last_end = event['end']
    
    return selected

