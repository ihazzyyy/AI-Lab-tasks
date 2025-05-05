graph = {
    'A' : {'B': 5, 'C': 10},
    'B' : {'A': 5, 'C': 3},
    'C' : {'A': 10, 'B': 3}
}

def request_ride(source, destination):
    if source not in graph or destination not in graph[source]:
        print('Invalid route, Using default 5 km ')
        return 5,'km'
    distance = graph[source][destination]
    print(f'Distance from {source} to {destination}: {distance} km')
    return distance
