class Solution:

    def encode(self, strs: List[str]) -> str:

        final_string=""
        for str_tiny in strs:
            final_string+= str(len(str_tiny)) + "#" + str_tiny
        return final_string



    def decode(self, s: str) -> List[str]:
        index_current = 0
        final_list = []
        while(index_current < len(s)):
            length = ""
            while(True):
                if(s[index_current] == '#'):
                    break
                length += s[index_current]
                index_current+=1
            
            length = int(length)

            word = s[index_current+1:index_current+length+1]
            final_list.append(word)
            index_current+=length+1

        return final_list
            # 3#hello
         # We need to go through the string:
            # Find the length we can do so by iterating until we encounter the 
            # first #
            # Add the string to the array
            # do the same for the rest of the strings

            


        
    
