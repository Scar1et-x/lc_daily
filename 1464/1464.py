from typing import List, Tuple


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first, second = 0, 1
        if nums[second] > nums[first]:
            first, second = second, first
        for i, v in enumerate(nums[2:], start=2):
            if v >= nums[first]:
                first, second = i, first
            elif v > nums[second]:
                second = i
        return (nums[first] - 1) * (nums[second] - 1)

    def run(self, test_cases: List[Tuple[List[int], int]]):
        for nums, expected in test_cases:
            assert self.maxProduct(nums) == expected


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 5, 6, 7], 30),
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([3, 7], 12),
    ]
    solution = Solution()
    solution.run(test_cases)
