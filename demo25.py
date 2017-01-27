# coding=utf-8
"""
给定一棵完全二叉树的根节点root，返回这棵树的节点个数。如果完全二叉树的节点数为N，请实现时间复杂度低于O(N)的解法。
给定树的根结点root，请返回树的大小

"""
class Node():
    def __init__(self,x):
        self.x = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.x)

class CountNodes():
    def count(self,root):
        if not root:
            return 0
        start, left, right = root, root.left, root.right
        i,j = 0,0
        sum = 0
        while left != None:
            i += 1
            left = left.left
        while right != None:
            j += 1
            right = right.left
        if i == j:
            leftcount = 2**i -1
            sum = leftcount + 1 +self.count(start.right)
        else:
            rightcount = 2**j - 1
            sum = rightcount + 1 + self.count(start.left)
        return sum

if __name__ =="__main__":
    head = Node(0)
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)

    head.left = one
    head.right = two
    one.left = three
    one.right = four
    three.left= seven
    three.right = eight
    four.left = nine

    two.left = five
    two.right = six


    c = CountNodes()
    print c.count(head)




