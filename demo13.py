# coding=utf-8
"""
   一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
   设函数f(x),n个台阶有f(n)种跳法,且f(n)=f(n-1)+f(n-2),转化为求菲波那切数列
"""
class Solution():
    def jumpFloor(self,n):
        a = 1
        b = 1
        if n == 1:
            return a
        else:
            for i in range(n):
                a, b = b, a+b
            return a

