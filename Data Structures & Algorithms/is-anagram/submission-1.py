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