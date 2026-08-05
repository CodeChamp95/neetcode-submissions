class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hmap = {}
        for character in s1:
            s1_hmap[character] = s1_hmap.get(character,0) + 1
        s1_size = len(s1)
        for i in range(len(s2)):
            window_flag = 0
            window_hmap = {}
            for j in range(i, i + s1_size):
                window_char = s2[j]
                if j == len(s2):
                    break
                elif s2[j] not in s1_hmap:
                    break
                window_hmap[window_char] = window_hmap.get(window_char,0) + 1
                if j == i + s1_size - 1:
                    for key in window_hmap.keys():
                        window_count = window_hmap.get(key,0)
                        s1_count = s1_hmap.get(key,0)
                        if window_count != s1_count:
                            return False
                    print(f"True returned for i: {i} and j: {j}")
                    return True

        return False