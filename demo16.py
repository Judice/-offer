# coding=utf-8
"""
题目描述:
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        elif number <= 2 :
            return number
        else:
            return self.rectCover(number-1)+self.rectCover(number-2)   #递归生成菲波那切数列


class Solution():
    def rectCover(self,number):
        a = 1
        b = 1
        if number == 1:
            return 1
        else:
            for i in range(number):
                a, b = b, a+b         #迭代生成菲波那切数列
            return a