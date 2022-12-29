import collections
from typing import List


class Solution:
    def twoOutOfThree(
        self, nums1: List[int], nums2: List[int], nums3: List[int]
    ) -> List[int]:
        counter = collections.Counter(
            list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        )
        return [k for k, v in counter.items() if v >= 2]

    def run(self, test_cases: list[tuple[list[int], list[int], list[int], object]]):
        for *case, expected in test_cases:
            try:
                actual = sorted(self.twoOutOfThree(*case))
                assert actual == expected
            except AssertionError:
                print("\nAssertionError:")
                print("actual:", actual)
                print("expected:", expected)
                break
            print(".", end="")
        else:
            print("\nYou can submit.")


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [2, 3], [3], [2, 3]),
        ([2, 3], [1], [4], []),
        ([3, 1], [2, 3], [1, 2], [1, 2, 3]),
        ([1, 1, 2, 3, 4], [2, 3], [3], [2, 3]),
    ]
    solution = Solution()
    solution.run(test_cases)
