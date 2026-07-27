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

            # unchecked_s_chars = []
            # for char in s:
            #     unchecked_s_chars.append(char)
            # for char in t:
            #     if char not in unchecked_s_chars:
            #         return False
            #     else:
            #         unchecked_s_chars.remove(char)

        return True