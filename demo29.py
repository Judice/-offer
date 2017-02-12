# -*- coding:utf-8 -*-
"""
首先我们介绍二叉树先序序列化的方式，假设序列化的结果字符串为str，初始时str等于空字符串。先序遍历二叉树，如果遇到空节点，就在str的末尾加上“#!”，“#”表示这个节点为空，节点值不存在，当然你也可以用其他的特殊字符，“!”表示一个值的结束。如果遇到不为空的节点，假设节点值为3，就在str的末尾加上“3!”。现在请你实现树的先序序列化。
给定树的根结点root，请返回二叉树序列化后的字符串。
"""
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeToString:
    def toString(self, root):
        # write code here
        if not root:
            return
        res = []
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur == '#':
                node = '#'+'!'
                res.append(node)
                continue
            node = str(cur.val)+'!'
            res.append(node)
            if cur.right:
                stack.append(cur.right)
            else:
                stack.append('#')
            if cur.left:
                stack.append(cur.left)
            else:
                stack.append('#')
        return ''.join(res)