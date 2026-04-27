class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        new_str = s.lower()
        while(start<end):
            print(f"Start: {new_str[start]} and End: {new_str[end]}")
            if new_str[start].isalnum() and new_str[end].isalnum():
                if new_str[start] == new_str[end]:
                    start = start + 1
                    end = end - 1
                else:
                    return False

            elif new_str[start].isalnum() is False:
                start = start + 1

            elif new_str[end].isalnum() is False:
                end = end - 1

        return True

        