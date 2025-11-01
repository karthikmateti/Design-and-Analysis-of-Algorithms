import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return pair, min_dist

def closest_in_strip(strip, d):
    min_dist = d
    pair = None
    strip.sort(key=lambda p: p[1])  # sort by y-coordinate
    
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                pair = (strip[i], strip[j])
            j += 1
    return pair, min_dist

def closest_pair_rec(points_sorted_x):
    n = len(points_sorted_x)
    if n <= 3:
        return brute_force(points_sorted_x)
    
    mid = n // 2
    midpoint = points_sorted_x[mid][0]
    
    left_pair, left_dist = closest_pair_rec(points_sorted_x[:mid])
    right_pair, right_dist = closest_pair_rec(points_sorted_x[mid:])
    
    min_dist = min(left_dist, right_dist)
    if min_dist == left_dist:
        min_pair = left_pair
    else:
        min_pair = right_pair
    
    #strip of points close to midpoint
    strip = [p for p in points_sorted_x if abs(p[0] - midpoint) < min_dist]
    
    strip_pair, strip_dist = closest_in_strip(strip, min_dist)
    if strip_dist is not None and strip_dist < min_dist:
        return strip_pair, strip_dist
    else:
        return min_pair, min_dist

def closest_pair(points):
    points_sorted_x = sorted(points, key=lambda p: p[0])
    return closest_pair_rec(points_sorted_x)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
pair, dist = closest_pair(points)
print("Closest pair:", pair)
print("Distance:", dist)
