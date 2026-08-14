class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed_map = {}
        for index, car in enumerate(position):
            speed_map[car] = speed[index]
        fleets = len(position)
        time = []
        position.sort()
        # speed.sort()

        matched_fleet = set()
        for i in range(len(position)):
            car = position[i]
            t = (target - position[i]) / speed_map[car]
            time.append(t)
        
        for i in range(len(time) - 1):
            for j in range(i + 1, len(time)):
                if i in matched_fleet and j in matched_fleet:
                    continue
                elif time[j] >= time[i]:
                    matched_fleet.add(j)
                    time[i] = time[j]
                    fleets -= 1

        # while True:
        #     to_be_continued = 0
        #     for i in range(len(position)):
        #         if position[i] < target:
        #             to_be_continued = 1
        #     if to_be_continued == 0:
        #         break
        #     for i in range(len(position)):
        #         if position[i] < target:
        #             position[i] += speed[i]
        #         else:
        #             reached_fleet.add(i)
        #     for i in range(len(position) - 1):
        #         if i in reached_fleet:
        #             continue
        #         for j in range(i + 1, len(position)):
        #             if i in matched_fleet and j in matched_fleet:
        #                 continue
        #             elif j in reached_fleet:
        #                 continue
        #             else:
        #                 if position[j] == position[i]:
        #                     print(f"Matched for i: {i} and j: {j} at positions: {position[i]} and {position[j]}")
        #                     fleets -= 1
        #                     matched_fleet.add(i)
        #                     matched_fleet.add(j)
        return fleets

            