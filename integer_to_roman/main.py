class Solution(object):
    def intToRoman(self, num):
        symbol_map = dict(
            [
                ("I", 1),
                ("IV", 4),
                ("V", 5),
                ("IX", 9),
                ("X", 10),
                ("XL", 40),
                ("L", 50),
                ("XC", 90),
                ("C", 100),
                ("CD", 400),
                ("D", 500),
                ("CM", 900),
                ("M", 1000),
            ]
        )
        # sort desc by value to choose the closest candiadate
        symbol_map = dict(
            sorted(symbol_map.items(), key=lambda item: item[1], reverse=True)
        )
        output_roman = ""
        while num > 0:
            for key in symbol_map:
                if num >= symbol_map[key]:
                    num = num - symbol_map[key]
                    output_roman = output_roman + key
                    break
        return output_roman


def main():
    sol = Solution()
    print(sol.intToRoman(58))


if __name__ == "__main__":
    main()
