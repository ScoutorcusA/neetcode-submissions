class Solution:
    def climbStairs(self, n: int) -> int:

        if (n <= 1):
            return 1
        else:
           return  self.climbStairs(n-1) + self.climbStairs(n-2)
        # We need to form combinations of 1, or 2. 
        # to reach n = 3 stairs, we can either
        # 1 + 1 + 1 = 3
        # or 1 + 2 = 3
        # or 2 + 1 = 3
        # for n = 4
        # 1 + 1 + 1 + 1 = 4
        # 1 + 2 + 1 = 4
        # 2 + 2 = 4
        # 2 + 1 + 1 = 4
        # 1 + 1 + 2 = 4
        