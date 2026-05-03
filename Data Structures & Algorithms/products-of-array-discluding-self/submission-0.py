class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_prefix_sum = [0] *n
        right_prefix_sum = [0]*n
        left_prefix_sum[0] = 1
        right_prefix_sum[n-1] = 1
        result = [0] * n
        for i in range(1, n):
            left_prefix_sum[i]=nums[i-1] * left_prefix_sum[i-1]
        for i in range(n- 2, -1, -1):
            right_prefix_sum[i] = nums[i+1] * right_prefix_sum[i+1]

        for i in range(n):
            result[i] = left_prefix_sum[i] * right_prefix_sum[i]

        return result

    
            
            

        