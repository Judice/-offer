# coding=utf-8
"""
题目描述
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
分析:除了最后一阶台阶必须跳到,其余所有台阶有跳到或者不跳两种选择,所以有2^(n-1)中组合
    或者 f(n)=2*f(n-1)
"""


class Solution():
    def jumpFloor(self, number):
        if number == 1:            # return 2**(number-1)   2^(number-1)
            return 1
        n = 1
        for i in range(number-1):
            n *= 2
        return n
