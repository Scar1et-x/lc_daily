from typing import List, Tuple


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        record = {v: idx for idx, v in enumerate(pushed)}
        min_idx, max_idx = record[popped[0]], record[popped[0]]
        for i in popped[1:]:
            cur = record[i]
            if not (abs(cur - min_idx) == 1 or abs(cur - max_idx) == 1):
                return False
            if cur < min_idx:
                min_idx = cur
            elif cur > max_idx:
                max_idx = cur
        return True

    def run(self, test_cases: List[Tuple[List[int], List[int], bool]]):
        for pushed, popped, expected in test_cases:
            assert self.validateStackSequences(pushed, popped) == expected


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),
        ([0, 2, 1], [0, 1, 2], True),
    ]
    solution = Solution()
    solution.run(test_cases)
