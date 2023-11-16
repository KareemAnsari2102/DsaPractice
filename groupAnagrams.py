"""
Given an array of strings strs, group the anagrams together. you can return the answer in any order. 
"""
from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    
    res = defaultdict(list)
    
    for s in strs:
        count = [0] * 26
        
        for c in s:
            count[ord(c)- ord("a")] += 1
            
        res[tuple(count)].append(s)
    print(res.values())
    return res.values()

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])