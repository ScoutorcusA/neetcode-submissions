class Solution {
    public boolean hasDuplicate(int[] nums) {
            HashMap<Integer, Integer> array = new HashMap<Integer, Integer>();



            for(int i = 0; i <nums.length; i++)
            {
                if(array.containsKey(nums[i]))
                {
                    return true;
                }
                else
                {
                    array.put(nums[i],1);
                }
            }


            return false;


 
    }
}
