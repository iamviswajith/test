"""
given two string check if both of them are isometric
"abba" --> "egge" is isomorphic
"abbd" --> "egge" is non-isomorphic
"""

def isisometric(s,t):
    h1={}

    if len(s) != len(t):
        return False
    for i in range(len(s)):
        if s[i] not in h1:
            h1[s[i]] = t[i]
        if h1[s[i]] != t[i]:
            print("not isometric")
            return False
    return True


s = "abbd"
t = "egge"

print(isisometric(s,t))