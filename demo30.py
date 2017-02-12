# -*- coding:utf-8 -*-
"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        tmp = []
        res = []
        if not pRoot:
            return res
        stack = [pRoot,'#']
        bool = True
        while stack:
            cur = stack.pop(0)
            if cur == '#':
                if bool:
                    tmp.reverse()
                res.append(tmp)
                tmp = []
            else:
                tmp.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                if stack[0] == '#':
                    stack.append('#')
                    bool = not bool
        return res[:-1]