from typing import List, Tuple


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in prices[i + 1 :]:
                if j <= prices[i]:
                    prices[i] -= j
                    break
        return prices

    def run(self, test_cases: List[Tuple[List[int], List[int]]]):
        for case, expected in test_cases:
            assert self.finalPrices(case) == expected


if __name__ == "__main__":
    test_cases = [
        ([8, 4, 6, 2, 3], [4, 2, 4, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([10, 1, 1, 6], [9, 0, 1, 6]),
    ]
    solution = Solution()
    solution.run(test_cases)
