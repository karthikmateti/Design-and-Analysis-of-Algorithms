def computeLPS(pattern):
    n = len(pattern)
    lps = [0] * n     # initialize LPS array with zeros
    length = 0        # length of previous LPS
    i = 1             # start from second character
    while i < n:
        if pattern[i] == pattern[length]:  # if match found
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:  # fallback to previous LPS value
                length = lps[length - 1]
            else:
                lps[i] = 0  # no match then set to 0
                i += 1
    return lps

pattern = "ABCBCABC"
lps_table = computeLPS(pattern)
print("Pattern:", pattern)
print("LPS Table:", lps_table)
