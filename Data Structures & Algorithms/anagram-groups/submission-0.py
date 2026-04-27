class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False

        else:
            unchecked_s_chars = []
            for char in s:
                unchecked_s_chars.append(char)
            for char in t:
                if char not in unchecked_s_chars:
                    return False
                else:
                    unchecked_s_chars.remove(char)

        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_list = []
        unchecked_strs = []
        for string in strs:
            unchecked_strs.append(string)

        for i in range(0,len(strs)):
            if(strs[i] not in unchecked_strs):
                continue

            sub_list = []
            sub_list.append(strs[i])
            if(i == len(strs)-1):
                ans_list.append(sub_list)
                break

            for j in range(i+1,len(strs)):
                if self.isAnagram(strs[i],strs[j]):
                    sub_list.append(strs[j])
                    unchecked_strs.remove(strs[j])

            ans_list.append(sub_list)
            unchecked_strs.remove(strs[i])

        return ans_list




        