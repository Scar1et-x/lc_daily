class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        sl = s.split(" ")
        tmp = -1
        for char in sl:
            if char.isdigit():
                int_char = int(char)
                if int_char > tmp:
                    tmp = int_char
                else:
                    break
        else:
            return True
        return False

    def run(self, test_cases: list[tuple[str, bool]]):
        for case, expected in test_cases:
            try:
                actual = self.areNumbersAscending(case)
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
        ("1 box has 3 blue 4 red 6 green and 12 yellow marbles", True),
        ("hello world 5 x 5", False),
        ("sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s", False),
        ("4 5 11 26", True),
    ]
    solution = Solution()
    solution.run(test_cases)
