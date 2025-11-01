def combinations(arr, r):
    if r == 0:
        return [[]]
    if len(arr) < r:
        return []
    result = []
    for i in range(len(arr)):
        fixed = arr[i]
        for comb in combinations(arr[i+1:], r-1):
            result.append([fixed] + comb)
    return result

def knapsack_brute_force_combinations(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []
    
    # combinations of all possible sizes 0 to n
    for r in range(n+1):
        for comb in combinations(list(range(n)), r):
            total_weight = sum(weights[i] for i in comb)
            total_value = sum(values[i] for i in comb)
            if total_weight <= capacity and total_value > max_value:
                max_value = total_value
                best_combination = comb
    
    return best_combination, max_value

weights = [2, 3, 4, 5, 9, 7]
values = [3, 4, 8, 8, 10, 15]
capacity = 20

best_comb, max_val = knapsack_brute_force_combinations(weights, values, capacity)
print("Best combination (item indices):", best_comb)
print("Maximum value:", max_val)
