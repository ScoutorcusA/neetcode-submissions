class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count will be a dictionary storing the 
        # number of times a number appears

        count = {}

        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in count:
                count[num] = count[num]+1
            else:
                count[num] =1
        
        for number, count in count.items():
            frequency[count].append(number)
        

        result = []

        for i in range(len(frequency) - 1, 0, -1):
            for number in frequency[i]:
                result.append(number)
                if len(result) == k:
                    return result
        
        