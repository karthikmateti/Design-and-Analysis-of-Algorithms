text=input("enter a string:")  # take input string from user
pattern="the" # pattern
n=len(text)
m=len(pattern)

indices=[]  #list to store
for i in range(n-m+1):
    if text[i:i+m]==pattern:  #compare substring with pattern
        indices.append(i)

if indices:
    print("pattern found at indices:",indices)  
else:
    print("pattern not found.")  #if no match found