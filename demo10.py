# coding:utf-8
"""
题目描述:
       请实现一个函数，将一个字符串中的空格替换成“%20”。例如，当字符串为We Are Happy.
       则经过替换之后的字符串为We%20Are%20Happy。
"""
class Solution:
    def replace(self, str):
        s = list(str)
        for i in range(len(s)):
            if s[i] == ' ':
                 s[i] = '%20'
        return ''.join(s)       #使用join生成新的字符串

# 或者直接使用replace
class Solution:
    def replace(self, str):
        return str.replace(' ', '%20')
