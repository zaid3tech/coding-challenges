import math 
class Solution(object):
    def sockMerchant(n, arr):
        pair = 0
        digit_count = {}
        for i in range(0, len(arr)):
            if arr[i] in digit_count:
                digit_count[arr[i]] = digit_count[arr[i]] + 1
            else:
                digit_count[arr[i]] = 1
    
        for x in digit_count.values():
            if x % 2 == 0:
                pair = pair + math.floor(x/2)
            elif x > 1: 
                pair = pair + math.floor(x/2)
        return pair


def main():
    sol = Solution()
    #expcted output 2
    print(sol.sockMerchant([1, 1, 1, 2, 2]))


if __name__ == "__main__":
    main()
