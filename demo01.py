"""
题目描述：
        在一个二维数组中，每一行都从左到右递增的顺序排序，每一列都从上到下递增的
        顺序排序。请完成一个函数， 输入这样的一个二维数组和一个整数，判断数组中
        是否含有该整数
"""


class Solution():
    def find(self, array, target):
        col = len(array[0])
        row = len(array)
        if target < array[0][0]:
            return False
        if target > array[row-1][col-1]:
            return False

        i = 0
        j = col -1
        while i < row and j >=0 :
            if array[i][j] == target:
                return True
            elif target > array[i][j]:
                 i += 1
            else:
                 j -= 1
        return False


if __name__ == "__main__":
    array = [[1, 2, 3,  4,  5],
            [2, 3, 4,  5,   6],
            [3, 6, 9,  12, 15],
            [5, 7, 10, 13, 16],
            [6, 9, 11, 14, 18],
            [7, 10, 12,15, 19]]
    s = Solution()
    print(s.find(array,8))