class Solution {
    public boolean isAnagram(String s, String t) 
    {
        HashMap<Character, Integer> s_map = new HashMap<Character, Integer>();
        HashMap<Character, Integer> t_map = new HashMap<Character, Integer>();


        if(s.length() != t.length())
        {
            return false;
        }

        for(int i = 0; i<s.length();i++)
        {
            if(s_map.containsKey(s.charAt(i)) != true)
            {
                s_map.put(s.charAt(i), 1);
            }
            else
            {
                s_map.put(s.charAt(i), s_map.get(s.charAt(i))+1);
            }

             if(t_map.containsKey(t.charAt(i)) != true)
            {
                t_map.put(t.charAt(i), 1);
            }
            else
            {
                t_map.put(t.charAt(i), t_map.get(t.charAt(i))+1);
            }

        }

    for (char i : s_map.keySet()) 
    {
        if(s_map.get(i) != t_map.get(i))
        {
            return false;
        }
  
    }   
return true;
        
    }
}
