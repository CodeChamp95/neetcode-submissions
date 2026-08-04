class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_length = 1
        max_length = 1
        # start_window = 0
        hmap = {}

        for i in range(len(s)):
            hmap[s[i]] = 1
            window_condition_broken_flag = 0
            for j in range(i + 1, len(s)):
                character = s[j]
                hmap[character] = hmap.get(character,0) + 1
                max_value = 0
                for value in hmap.values():
                    if value > max_value:  
                        max_value = value
                window_length += 1
                # print(f"For i: {i} and j: {j} the window length is {window_length}")

                if window_length - max_value > k:
                    window_condition_broken_flag = 1
                    break

            if window_condition_broken_flag == 1:
                window_length -= 1
                if window_length > max_length:
                    max_length = window_length
            else: 
                if window_length > max_length:
                    max_length = window_length

            window_length = 1
            hmap.clear()

        if window_length > max_length:
            max_length = window_length

        return max_length

    