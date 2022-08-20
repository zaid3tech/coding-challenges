class Solution(object):
    def romanToInt(self, s):
        symbol_map = dict(
            [
                ("I", 1),
                ("V", 5),
                ("X", 10),
                ("L", 50),
                ("C", 100),
                ("D", 500),
                ("M", 1000),
            ]
        )
        sum = 0
        i = 0
        while i < len(s):
            if (
                i < (len(s) - 1) and symbol_map[s[i]] < symbol_map[s[i + 1]]
            ):  ##if curr is less than next, next - curr
                sum = sum + (symbol_map[s[i + 1]] - symbol_map[s[i]])
                i = i + 2
            else:
                sum = sum + symbol_map[s[i]]
                i = i + 1
        return sum


def main():
    sol = Solution()
    print(sol.romanToInt("LVIII"))


if __name__ == "__main__":
    main()
