def knapsack_brute_force(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = None
    
    # There are 2^n possible subsets of items
    for i in range(2**n):
        binary = bin(i)[2:].zfill(n)  # binary representation of subset
        total_weight = 0
        total_value = 0
        
        # Check which items are included
        for j in range(n):
            if binary[j] == '1':
                total_weight += weights[j]
                total_value += values[j]
        
        # Check total weight is within capacity
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = binary
    
    return best_combination, max_value

weights = [2, 3, 4, 5, 9, 7]
values = [3, 4, 8, 8, 10, 15]
capacity = 20

best_comb, max_val = knapsack_brute_force(weights, values, capacity)
print("Best combination:", best_comb)
print("Maximum value:", max_val)
