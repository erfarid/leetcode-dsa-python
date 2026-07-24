from typing import List


class Solution:
    def maxActiveSectionsAfterTrade(
        self, s: str, queries: List[List[int]]
    ) -> List[int]:

        n = len(s)

        # Split the string into consecutive segments.
        run_start = []
        run_end = []
        run_length = []
        run_char = []
        run_id = [0] * n

        i = 0

        while i < n:
            j = i
            current_id = len(run_start)

            while j < n and s[j] == s[i]:
                run_id[j] = current_id
                j += 1

            run_start.append(i)
            run_end.append(j - 1)
            run_length.append(j - i)
            run_char.append(s[i])

            i = j

        number_of_runs = len(run_start)

        # For every internal 1-segment:
        #
        # 0...0 + 1...1 + 0...0
        #
        # The trade gains the lengths of both zero segments.
        gain = [0] * number_of_runs

        for i in range(1, number_of_runs - 1):
            if run_char[i] == "1":
                gain[i] = run_length[i - 1] + run_length[i + 1]

        # Build an iterative segment tree for range maximum queries.
        size = 1

        while size < number_of_runs:
            size *= 2

        tree = [0] * (2 * size)

        for i in range(number_of_runs):
            tree[size + i] = gain[i]

        for i in range(size - 1, 0, -1):
            tree[i] = max(tree[2 * i], tree[2 * i + 1])

        def range_max(left: int, right: int) -> int:
            """Return maximum gain from run left to run right."""
            if left > right:
                return 0

            left += size
            right += size
            result = 0

            while left <= right:
                if left % 2 == 1:
                    result = max(result, tree[left])
                    left += 1

                if right % 2 == 0:
                    result = max(result, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return result

        def boundary_gain(
            one_run: int,
            query_left: int,
            query_right: int,
            left_run: int,
            right_run: int
        ) -> int:
            """
            Calculate the gain when one of the neighboring zero-runs
            is only partially inside the query.
            """
            if one_run <= left_run or one_run >= right_run:
                return 0

            if one_run <= 0 or one_run >= number_of_runs - 1:
                return 0

            if run_char[one_run] != "1":
                return 0

            left_zero = one_run - 1
            right_zero = one_run + 1

            left_length = (
                min(query_right, run_end[left_zero])
                - max(query_left, run_start[left_zero])
                + 1
            )

            right_length = (
                min(query_right, run_end[right_zero])
                - max(query_left, run_start[right_zero])
                + 1
            )

            if left_length <= 0 or right_length <= 0:
                return 0

            return left_length + right_length

        total_ones = s.count("1")
        answer = []

        for left, right in queries:
            left_run = run_id[left]
            right_run = run_id[right]

            # Runs strictly inside the two boundary runs.
            best_gain = range_max(left_run + 2, right_run - 2)

            # Handle the possible 1-run next to the left boundary.
            best_gain = max(
                best_gain,
                boundary_gain(
                    left_run + 1,
                    left,
                    right,
                    left_run,
                    right_run
                )
            )

            # Handle the possible 1-run next to the right boundary.
            if right_run - 1 != left_run + 1:
                best_gain = max(
                    best_gain,
                    boundary_gain(
                        right_run - 1,
                        left,
                        right,
                        left_run,
                        right_run
                    )
                )

            answer.append(total_ones + best_gain)

        return answer