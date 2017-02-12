# -*- coding:utf-8 -*-
"""
请用递归方式实现二叉树的先序、中序和后序的遍历打印。
给定一个二叉树的根结点root，请依次返回二叉树的先序，中序和后续遍历(二维数组的形式)
"""
class Node:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class TreeToSequence:
     def convert(self, root):
         res = [[],[],[]]
         self.preorder(root, res[0])
         self.inorder(root, res[1])
         self.postorder(root, res[2])
         return res

     def preorder(self, root, res):
         if not root:
             return None
         res.append(root.val)
         self.preorder(root.left, res)
         self.preorder(root.right, res)
         return res

     def inorder(self,root, res):
         if not root:
             return None
         self.inorder(root.left, res)
         res.append(root.val)
         self.inorder(root.right, res)
         return res

     def postorder(self, root, res):
         if not root:
             return None
         self.postorder(root.left, res)
         self.postorder(root.right, res)
         res.append(root.val)
         return res

