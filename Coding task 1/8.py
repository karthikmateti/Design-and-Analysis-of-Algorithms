import time

# ---Naive String Search ---
def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    comparisons = 0
    indices = []

    for i in range(n - m + 1):
        match = True
        for j in range(m):
            comparisons += 1  # count each character
            if text[i+j] != pattern[j]:
                match = False
                break
        if match:
            indices.append(i)  # store starting index of match
    return indices, comparisons

# --- KMP Algorithm ---
def compute_lps(pattern):
    n = len(pattern)
    lps = [0]*n  #LPS array
    length = 0
    i = 1

    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]  #fall back
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    comparisons = 0
    indices = []

    i = j = 0
    while i < n:
        comparisons += 1 #count character
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:  #pattern found
            indices.append(i-j)
            j = lps[j-1] #move pattern index using LPS
        elif i < n and text[i] != pattern[j]: #mismatch
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return indices, comparisons

#-- Main Program --
text = "CATSABCBCABCDOGSABCBCABC"
pattern = "ABCBCABC"

# Naive search
start_time = time.time()
naive_indices, naive_comp = naive_search(text, pattern)
naive_time = round(time.time() - start_time, 6)

# KMP search
start_time = time.time()
kmp_indices, kmp_comp = kmp_search(text, pattern)
kmp_time = round(time.time() - start_time, 6)

#Results
print("Naive Search Results:")
print("Indices Found:", naive_indices)
print("Comparisons:", naive_comp)
print("Time Taken (s):", naive_time)
print("\nKMP Search Results:")
print("Indices Found:", kmp_indices)
print("Comparisons:", kmp_comp)
print("Time Taken (s):", kmp_time)
