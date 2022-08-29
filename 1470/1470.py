from typing import List, Tuple


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n + i])
        return res

    def run(self, test_cases: List[Tuple[List[int], int, List[int]]]):
        for nums, n, expected in test_cases:
            assert self.shffule(nums, n) == expected


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], 2, [1, 3, 2, 4]),
        ([1, 2], 1, [1, 2]),
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
    ]
    solution = Solution()
    solution.run(test_cases)
