"""

KMP substring:
    construct a prefix arr

"""

text = "abcabcdxabcabcdabcy"
pattern = "abcdabc"
t_len = len(text)
p_len = len(pattern)
temp = [0]*p_len

i = 1
j = 0
while i<p_len and j < p_len:
    if pattern[i] == pattern[j]:
        temp[i] = j+1
        i+=1
        j+=1
    else:
        i+=1

i = j = 0

while j < p_len and i < t_len:
    if text[i] == pattern[j]:
        i+=1
        j+=1
    else:
        j = temp[j-1]
        if text[i] != pattern[j]:
            i+=1


if text[i-p_len:i] != pattern:
    print("pattern doesnt exist")
else:
    print("success!")
    print("\t",text)
    print("\t",text[:i-p_len]+'['+text[i-p_len:i]+']'+text[i:])
    print("\t",pattern)

# print(text[i-p_len:i], pattern)
