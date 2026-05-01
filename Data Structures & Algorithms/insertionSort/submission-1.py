# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if(pairs == []):
            return []
        list_of_lists = [pairs.copy()]
        for k in range(1, len(pairs)):
            j = k - 1 
            
            while(j >= 0 and pairs[j + 1].key < pairs[j].key):
                temp = pairs[j]
                pairs[j] = pairs[j + 1]
                pairs[j + 1] = temp
                j = j -1
            list_of_lists.append(pairs.copy())

        return list_of_lists
        