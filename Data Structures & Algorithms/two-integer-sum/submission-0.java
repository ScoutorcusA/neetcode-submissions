class Solution {
    public int[] twoSum(int[] nums, int target) 
    {
        HashMap<Integer, Integer> temp = new HashMap<>();
         int [] tempA = {0,0};

        for(int i = 0; i<nums.length; i++)
        {
            if(temp.containsKey(nums[i]) == false)
            {
                temp.put(nums[i], i);
                
            }
            
            if(temp.containsKey(target - nums[i]) && temp.get(target -nums[i]) != i)
                {
             tempA[1] = i;
            tempA[0] =  temp.get(target - nums[i]);
            return tempA;
                }
        

        }



      return tempA;  
    }

}
