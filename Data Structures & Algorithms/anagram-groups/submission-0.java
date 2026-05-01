class Solution {
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        HashMap<String, List<String>> GroupsOfAnagrams = new HashMap<>();

        for(int i = 0; i < strs.length; i++)
        {
            int[] letters = new int[26];
            for(int j = 0; j < strs[i].length(); j++)
            {
                letters[strs[i].charAt(j) - (char) 'a']+=1;
            }
            String key =  Arrays.toString(letters);
            if(!GroupsOfAnagrams.containsKey(key))
            {
                GroupsOfAnagrams.put(key, new ArrayList<>());
            }


            GroupsOfAnagrams.get(key).add(strs[i]);
            
        }
        return new ArrayList<>(GroupsOfAnagrams.values());


        
    }
}
