class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        matched_fleet = set()
        while True:
            to_be_continued = 0
            for i in range(len(position)):
                if position[i] < target:
                    to_be_continued = 1
            if to_be_continued == 0:
                break
            for i in range(len(position)):
                position[i] += speed[i]
            for i in range(len(position) - 1):
                for j in range(i + 1, len(position)):
                    if i not in matched_fleet and j not in matched_fleet:
                        if position[j] == position[i]:
                            fleets -= 1
                            matched_fleet.add(i)
                            matched_fleet.add(j)
        return fleets

            