"""
given "ABC"

print
ABC
ACB
BAC
BCA
CBA
CAB

"""


def permute(s,l,r):
    if l == r:
        print(''.join(s))

    for i in range(l,r+1):
        s[l], s[i] = s[i], s[l]
        permute(s, l+1, r)
        s[l], s[i] = s[i], s[l]
# Driver program to test the above function

string = "ABC"
n = len(string)
a = list(string)
permute(a, 0, n - 1)