class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        max_length = 1
        window_length = 1
        hmap = {}
        hmap[s[0]] = 0
        start_window = 0
        # visited_window = [s[0]]

        for i in range(1,len(s)):
            character = s[i]
            matching_index = hmap.get(character,-1)
            if matching_index == -1:
                window_length += 1
                hmap[character] = i

            else:
                if window_length > max_length:
                    max_length = window_length
                for j in range(start_window,matching_index + 1):
                    prev_window_char = s[j]
                    hmap.pop(prev_window_char)
                start_window = matching_index + 1
                window_length = i - start_window + 1
                hmap[character] = i


        return max_length