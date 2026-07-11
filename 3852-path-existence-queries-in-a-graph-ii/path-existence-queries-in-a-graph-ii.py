from typing import List


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # Sort the nodes according to their values.
        order = sorted(range(n), key=lambda index: nums[index])
        sorted_nums = [nums[index] for index in order]

        # position[node] = position of the node in sorted order
        position = [0] * n
        for sorted_index, original_index in enumerate(order):
            position[original_index] = sorted_index

        # Identify connected components.
        # A gap greater than maxDiff separates two components.
        component = [0] * n

        for i in range(1, n):
            component[i] = component[i - 1]

            if sorted_nums[i] - sorted_nums[i - 1] > maxDiff:
                component[i] += 1

        # farthest[i] = farthest sorted position reachable from i
        # using exactly one edge.
        farthest = [0] * n
        right = 0

        for left in range(n):
            right = max(right, left)

            while (
                right + 1 < n
                and sorted_nums[right + 1] - sorted_nums[left] <= maxDiff
            ):
                right += 1

            farthest[left] = right

        # Binary lifting:
        # jump[k][i] = farthest position reachable from i
        # using at most 2^k edges.
        log = n.bit_length()
        jump = [farthest]

        for k in range(1, log):
            previous = jump[k - 1]
            current = [0] * n

            for i in range(n):
                current[i] = previous[previous[i]]

            jump.append(current)

        answer = []

        for u, v in queries:
            left = position[u]
            right = position[v]

            # Distance from a node to itself is zero.
            if left == right:
                answer.append(0)
                continue

            if left > right:
                left, right = right, left

            # Nodes in different components cannot reach each other.
            if component[left] != component[right]:
                answer.append(-1)
                continue

            current = left
            distance = 0

            # Take the largest possible jumps while remaining
            # strictly before the target.
            for k in range(log - 1, -1, -1):
                next_position = jump[k][current]

                if next_position < right:
                    current = next_position
                    distance += 1 << k

            # One final edge reaches the target or passes it.
            answer.append(distance + 1)

        return answer