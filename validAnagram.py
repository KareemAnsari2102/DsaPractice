"""
Given Two strings s and t, return True id t is an anagram of s, and False otherwise 
"""
def validAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        print("False")
        return False
    
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)        
    for c in countS:
        if countS[c] != countT.get(c, 0):
            print("False")
            return False
    print("True")
    return True

validAnagram("track", "rackt")