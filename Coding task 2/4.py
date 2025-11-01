from itertools import permutations

def calculate_distance(path, distance_matrix):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i+1]]
    # To complete the cycle return to the starting city
    total_distance += distance_matrix[path[-1]][path[0]]
    return total_distance

def travelling_salesman_brute_force(distance_matrix):
    n = len(distance_matrix)
    cities = list(range(n))
    
    min_distance = float('inf')
    best_path = None
    
    #all possible orderings of cities excluding the starting city
    for perm in permutations(cities[1:]):
        path = [cities[0]] + list(perm)
        dist = calculate_distance(path, distance_matrix)
        if dist < min_distance:
            min_distance = dist
            best_path = path
    return best_path, min_distance

distance_matrix = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 17],
    [15, 35, 0, 30, 28],
    [20, 25, 30, 0, 22],
    [25, 17, 28, 22, 0]
]

path, min_dist = travelling_salesman_brute_force(distance_matrix)
print("Optimal path:", path)
print("Minimum distance:", min_dist)
