import math


class Solution(object):
    def countingValleys(steps, path):
        curr_level = 0
        valley = 0
        for x in path:
            if (
                x == "D" and curr_level == 0
            ):  ##requirement for valley is it should start from sea level, say 0
                valley = (
                    valley + 1
                )  ##if Down start from level 0, just increment the valley
                curr_level = curr_level - 1
            elif x == "U":
                curr_level = curr_level + 1
            elif x == "D":
                curr_level = curr_level - 1
        return valley


def main():
    sol = Solution()
    # expcted output 2
    print(sol.countingValleys("DDUUDDUDUUUD"))


if __name__ == "__main__":
    main()
