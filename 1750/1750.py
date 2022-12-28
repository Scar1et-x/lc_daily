class Solution:
    def minimumLength(self, s: str) -> int:
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                break
            if s[start] == s[start + 1] and start < end - 1:
                start += 1
                continue
            if s[end] == s[end - 1] and end > start + 1:
                end -= 1
                continue
            start += 1
            end -= 1
        return end - start + 1

    def run(self, test_cases: list[tuple[str, int]]):
        for case, expected in test_cases:
            assert self.minimumLength(case) == expected


if __name__ == "__main__":
    test_cases = [
        ("ca", 2),
        ("abccba", 0),
        ("abcba", 1),
        ("aabbcaccba", 1),
        ("abcaaba", 3),
    ]
    solution = Solution()
    solution.run(test_cases)
