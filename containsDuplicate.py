"""
given an integer array nums, return True if any value appears at least
twice in the array, and return False if every element is distinct 
"""
def solution(nums: list[int]) -> bool:

    hashset = set()
    
    for n in nums:
        if n in hashset:
            print("True")
            return True
        hashset.add(n)
    print("False")
    return False


solution([1, 2, 3, 4, 5, 1, 5])
