class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        max_length = 1
        window_length = 1
        visited_window = [s[0]]
        for i in range(1,len(s)):
            character = s[i]
            print(f"character is {character}")
            if character in visited_window:
                if window_length > max_length:
                    max_length = window_length

                j = 0
                while j < len(visited_window):
                    print(f"Length of window is {len(visited_window)} and j is {j}")
                    print("Next line")
                    if visited_window[j] == character:
                        print(f"Inside if block, character is {character}")
                        visited_window.remove(character)
                        window_length = window_length - 1
                        break

                    else:
                        print(f"Entered else block with j as {j} and removing {visited_window[j]}")
                        visited_window.remove(visited_window[j])
                        window_length = window_length - 1
                        j = 0
            
            visited_window.append(character)
            window_length = window_length + 1

        return max_length