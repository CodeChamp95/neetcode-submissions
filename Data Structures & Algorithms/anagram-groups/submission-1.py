class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        else:

            hash_map = {}

            for element in s:
                hash_map[element] = hash_map.get(element,0) + 1

            for element in t:
                hash_map[element] = hash_map.get(element,0) - 1

            for value in hash_map.values():
                if value != 0:
                    return False

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_list = []
        unchecked_strs_map = {}
        for string in strs:
            unchecked_strs_map[string] = len(string)

        for i in range(0,len(strs)):
            word = strs[i]
            if(unchecked_strs_map[word] == 0):
                continue

            sub_list = []
            sub_list.append(word)
            if(i == len(strs)-1):
                ans_list.append(sub_list)
                break

            for key,value in unchecked_strs_map.items():
                if value == len(word) and key != word:
                    if self.isAnagram(word,key):
                        sub_list.append(key)
                        unchecked_strs_map[key] = 0


            # for j in range(i+1,len(strs)):
            #     if self.isAnagram(strs[i],strs[j]):
            #         sub_list.append(strs[j])
            #         unchecked_strs.remove(strs[j])

            ans_list.append(sub_list)
            unchecked_strs_map[word] = 0

        return ans_list




        