# -*- coding:utf-8 -*-
class Node:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class TreeToSequence:
    def convert(self, root):
        # write code here
        res=[[],[],[]]

        self.preorderTrav(root,res[0])
        self.inorderTrav(root,res[1])
        self.postorderTrav_1(root,res[2])
        return res

    def preorderTrav(self,root,res):
        if not root:
            return
        stack=[]
        stack.append(root)  #先把根入栈
        while stack:
            cur=stack.pop()  #弹出的结点设置为新的root
            res.append(cur.val)
            if cur.right :
                stack.append(cur.right)
            if cur.left :
                stack.append(cur.left)

    def inorderTrav(self,root,res):
        if not root:
            return

        stack=[]
        stack.append(root)
        cur=root.left
        while stack or cur:   #栈不为空或者有右孩子 都继续  因为当树根结点出栈后，栈为空，但是树根结点有右孩子需要继续入栈
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right

    def postorderTrav_1(self,root,res): #使用两个栈
        #因为后序是左右根，所以按根右左入栈2，再从栈2弹出即为后序
        if not root:
            return
        stack1=[]
        stack2=[]
        stack1.append(root)
        while stack1:
            cur=stack1.pop()
            stack2.append(cur)
            if cur.left :
                stack1.append(cur.left)
            if cur.right :
                stack1.append(cur.right)
        while stack2:
            res.append(stack2.pop().val)

