class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_set = set(s1)
        s1_size = len(s1)
        for i in range(len(s2)):
            window_set = set()
            for j in range(i, i + s1_size):
                if j == len(s2):
                    break
                elif s2[j] not in s1_set:
                    break
                window_set.add(s2[j])
                if j == i + s1_size - 1 and len(s1_set.intersection(window_set)) == len(s1_set):
                    print(f"True returned for i: {i} and j: {j}")
                    return True

        return False