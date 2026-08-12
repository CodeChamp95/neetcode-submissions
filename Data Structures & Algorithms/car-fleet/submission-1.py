class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = len(position)
        matched_fleet = set()
        reached_fleet = set()
        while True:
            to_be_continued = 0
            for i in range(len(position)):
                if position[i] < target:
                    to_be_continued = 1
            if to_be_continued == 0:
                break
            for i in range(len(position)):
                if position[i] < target:
                    position[i] += speed[i]
                else:
                    reached_fleet.add(i)
            for i in range(len(position) - 1):
                if i in reached_fleet:
                    continue
                for j in range(i + 1, len(position)):
                    if i in matched_fleet and j in matched_fleet:
                        continue
                    elif j in reached_fleet:
                        continue
                    else:
                        if position[j] == position[i]:
                            # print(f"Matched for i: {i} and j: {j} at positions: {position[i]} and {position[j]}")
                            fleets -= 1
                            matched_fleet.add(i)
                            matched_fleet.add(j)
        return fleets

            