class Solution(object):
    def minimumAbsoluteDifference(self, arr):
    ##sort the array 
        arr.sort()
        min_diff = abs(arr[0] - arr[1])
        for i in range(1, len(arr) - 1):
            if abs(arr[i] - arr[i+1]) < min_diff:
                min_diff = abs(arr[i] - arr[i+1])
        return min_diff

def main():
    sol = Solution()
    print(sol.minimumAbsoluteDifference([3, -7, 0]))


if __name__ == "__main__":
    main()        


