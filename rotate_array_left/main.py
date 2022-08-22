class Solution(object):
    def rotate_left(self, arr, d):
        if d == 0:
            return arr
        temp_list = []
        for x in range(d, len(arr)):
            temp_list.append(arr[x])
        for x in range(0, d):
            temp_list.append(arr[x])
        return temp_list


def main():
    sol = Solution()
    print(sol.rotate_left([1, 2, 3, 4], 2))


if __name__ == "__main__":
    main()
