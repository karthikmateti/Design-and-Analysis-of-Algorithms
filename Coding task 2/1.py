def permutations(arr):
    if len(arr) <= 1:
        return [arr[:]]
    result = []
    for i in range(len(arr)):
        # Takes element out
        first = arr[i]
        rest = arr[:i] + arr[i+1:]
        #all permutations of the rest
        for p in permutations(rest):
            result.append([first] + p)
    return result

nums = [1, 2, 3]
print(permutations(nums))
chars = ['a', 'b', 'c']
print(permutations(chars))
mixed = [1, "b", 3.5]
print(permutations(mixed))
