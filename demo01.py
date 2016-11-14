"""
题目描述：
        在一个二维数组中，每一行都从左到右递增的顺序排序，每一列都从上到下递增的
        顺序排序。请完成一个函数， 输入这样的一个二维数组和一个整数，判断数组中
        是否含有该整数
"""


class Solution():
    def search(self):
        row = len(array)
        for i in xrange(row):
            col = len(array[i])
            for j in xrange(col):
                if target == array[i][j]:
                    return True
        return False


if __name__ == "__main__":
    array = [[1, 2, 3,  4,  5],
            [2, 3, 4,  5,   6],
            [3, 6, 9,  12, 15],
            [5, 7, 10, 13, 16],
            [6, 9, 11, 14, 18],
            [7, 10, 12,15, 19]]
    s = Solution()
    print s.find(array,8)