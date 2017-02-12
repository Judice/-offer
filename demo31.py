# coding=utf-8
"""
有一棵二叉树，请设计一个算法判断这棵二叉树是否为平衡二叉树。
给定二叉树的根结点root，请返回一个bool值，代表这棵树是否为平衡二叉树。

"""
class Node:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class CheckBalance:
    def check(self, root):
        if self.getHeight(root) >=0:
            return True
        else:
            return False

    def getHeight(self,root):  #后序遍历 得到层数
        if not root:  #空树，层数为0
            return 0
        left=self.getHeight(root.left)  #左子树 深度
        right=self.getHeight(root.right)  #右子树 深度

        if (abs(left-right) >1):  #不是平衡二叉树
            return -1

        return max(left,right)+1


if __name__ == "__main__":
    head = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)

    head.left = one
    head.right = two
    one.left = three
    one.right = four
    c = CheckBalance()
    print c.check(head)