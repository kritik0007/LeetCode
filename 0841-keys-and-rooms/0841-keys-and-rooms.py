from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # Initialize a hash-set to keep track of unique visited nodes (rooms)
        visited = {0}
        # Initialize a queue for Breadth-First Search (BFS)
        queue = deque([0])

        while queue:
            # Extract the current node (room) to explore its keys
            current_key = queue.popleft()

            # Iterate through all neighbors (keys) available in the current room
            for key in rooms[current_key]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        # If the number of uniquely visited rooms equals the total number of rooms, return True
        return len(visited) == len(rooms)