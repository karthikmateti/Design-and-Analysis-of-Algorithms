def combinations(arr, r):
    if r == 0:
        return [[]]
    # If array is empty or size less than required combinations
    if len(arr) < r:
        return []
    
    result = []
    for i in range(len(arr)):
        # Fix element
        fixed = arr[i]
        # Combine with combinations of remaining elements with size reduced by 1
        for comb in combinations(arr[i+1:], r-1):
            result.append([fixed] + comb)
    return result
nums = [1, 2, 3, 4]
print(combinations(nums, 2))
chars = ['a', 'b', 'c']
print(combinations(chars, 2))

mixed = [1, "b", 3.5]
print(combinations(mixed, 2))
