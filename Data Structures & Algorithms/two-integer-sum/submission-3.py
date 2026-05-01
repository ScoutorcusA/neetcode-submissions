class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        keys = {}
        for index, num in enumerate(nums):
            if target - num in keys:
                return [keys[target-num], index]
            else:
                keys[num] = index
        return [0,0]
        


        
        