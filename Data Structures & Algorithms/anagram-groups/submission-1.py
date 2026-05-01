class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each word in the array
            # Add each letter to a hashmap? what would be the key?
            #  OHHH sort each word first. 
                # So something like ACT becomes, ACT and cat becomes ACT

        anagrams = {}
        final_result = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        for key in anagrams.keys():
            final_result.append(anagrams[key])
        return final_result

        
        