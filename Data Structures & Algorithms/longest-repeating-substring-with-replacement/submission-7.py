class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        window_k = k
        window_length = 1
        max_length = 1
        start_window = 0
        max_window_char = s[0]
        hmap = {}
        hmap[s[0]] = 1

        for i in range(1,len(s)):
            character = s[i]
            hmap[character] = hmap.get(character,0) + 1
            max_value = 0
            for key,value in hmap.items():
                if value > max_value:
                    max_value = value
                    max_window_char = key

            if window_k == 0 and s[i] != s[i-1] and i == start_window + 1:
                if window_length > max_length:
                    max_length = window_length
                for j in range(start_window,i):
                    prev_char = s[j]
                    hmap[prev_char] = hmap.get(prev_char,0) - 1
                start_window = i
                max_window_char = s[start_window]
                window_length = 1
                window_k = k

            elif character == max_window_char:
                window_length += 1

            elif character != max_window_char and window_k != 0:
                window_length += 1
                window_k -= 1

            elif character != max_window_char and window_k == 0:
                if window_length > max_length:
                    max_length = window_length
                for j in range(start_window,i):
                    prev_char = s[j]
                    hmap[prev_char] = hmap.get(prev_char,0) - 1
                start_window = i
                max_window_char = s[start_window]
                window_length = 1
                window_k = k

        if window_length > max_length:
            max_length = window_length

        return max_length

    #    character = s[0]
    #    start_index = 0
    #    window_indices = [] 
    #    max_length = 0
    #    window_length = 1
    #    max_character = s[0]

    #    for i in range(1,len(s)):
    #         if s[i] == character:
    #             window_length = window_length + 1

    #         else:
    #             end_index = i - 1
    #             window_indices.append([start_index,end_index])
    #             if window_length > max_length:
    #                 max_length = window_length
    #             max_character = character
    #             window_length = 1
    #             character = s[i]
    #             start_index = i

    #    if window_length > max_length:
    #             max_length = window_length

    #    end_index = len(s) - 1
    #    window_indices.append([start_index,end_index])

    #    start = 0
    #    end = len(s) - 1
    #    for index in window_indices:
    #         print(index)
    #         diff = index[1] - index[0]
    #         if diff == max_length - 1:
    #             start = index[0] - 1
    #             end = index[1] + 1

    #    count = max_length
    #    if k == 0:
    #         return count
    #    print(count,start,end)
    #    left_count = 0
    #    for i in range(k):
    #         if start < 0:
    #             break

    #         s.replace(s[start],max_character)
    #         count = count + 1
    #         left_count = left_count + 1
    #         start = start - 1

    #    k = k - left_count
    #    while start >= 0:
    #         if s[start] != max_character:
    #             break

    #         else: 
    #             count = count + 1
    #             start = start - 1

    #    for i in range(k):
    #         if end > len(s) - 1:
    #             break

    #         s.replace(s[end],max_character)
    #         count = count + 1
    #         end = end + 1

    #    while end < len(s):
    #         if s[end] != max_character:
    #             break

    #         else: 
    #             count = count + 1
    #             end = end + 1

    #    return count

    