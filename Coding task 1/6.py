def computeLPS(pattern):
    n = len(pattern)
    lps = [0] * n     # initialize LPS array with zeros
    length = 0         # length of previous LPS
    i = 1              # start from second character

    while i < n:
        if pattern[i] == pattern[length]:  # characters match
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # fall back to previous LPS
            else:
                lps[i] = 0
                i += 1
    return lps

# KMP search function
def KMP_search(text, pattern):
    lps = computeLPS(pattern)
    n = len(text)
    m = len(pattern)
    i = 0 #index for text
    j = 0  #index for pattern
    indices = []  # store starting indices of matches
    while i < n:
        if text[i] == pattern[j]: # if characters matched move both forward
            i += 1
            j += 1

        if j == m: 
            # Pattern found at index i-j
            indices.append(i - j)
            j = lps[j - 1]    # move to next possible match using LP
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]  
            else:
                i += 1

    return indices
text = "CATSABCBCABCDOGSABCBCABC"
pattern = "ABCBCABC"

# Perform KMP search
matches = KMP_search(text, pattern)
if matches:
    print(f"Pattern '{pattern}' found at indices:", matches)
else:
    print(f"Pattern '{pattern}' not found in text.")   #no match found
