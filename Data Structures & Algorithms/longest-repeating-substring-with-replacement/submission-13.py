class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_length = 1
        max_length = 1
        start_window = 0
        hmap = {}
        hmap[s[0]] = 1
        # window_condition_broken_flag = 0

        for i in range(1,len(s)):
            start_window_char = s[start_window]
            window_length = i - start_window + 1
            character = s[i]
            hmap[character] = hmap.get(character,0) + 1
            max_value = 0
            for value in hmap.values():
                if value > max_value:  
                    max_value = value

            if i == len(s) - 1 and window_length - max_value <= k:
                max_length = max(max_length, window_length)

            # print(f"For start_window: {start_window} and i: {i} the window length is {window_length} and max_value is {max_value}")
            if window_length - max_value > k:
                # window_condition_broken_flag = 1
                max_length = max(max_length,(window_length - 1))
                hmap[start_window_char] = hmap.get(start_window_char,0) - 1
                start_window += 1

        # if not window_condition_broken_flag:
        #     max_length = max(max_length, window_length)
        
        return max_length

    