# coding=utf-8
"""
   大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
"""
class Solution():
    def Fibonacci(self, n):
        fibs = [0, 1, 1]
        if n < 2:
            return fibs[n]
        else:
            for i in range(2, n+1):
                fibs.append(fibs[i-1] + fibs[i-2])
            return fibs[n]

if __name__ == "__main__":
    s = Solution()
    print s.Fibonacci(7)