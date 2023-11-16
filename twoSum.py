"""
 given an array of integers nums and an integer target, return indices of the two numbers 
 such that they add up to target.
"""
def twosum(nums: list[int], target: int) -> [int]:
    map = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in map:
            print(map[diff], i)
            return[map[diff], i]
        map[n] = i
    return
        
twosum([2, 7, 11, 15], 9)