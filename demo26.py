# coding=utf-8
"""
有一棵二叉树，请设计一个算法，按照层次打印这棵二叉树。
给定二叉树的根结点root，请返回打印结果，结果按照每一层一个数组进行储存，
所有数组的顺序按照层数从上往下，且每一层的数组内元素按照从左往右排列。保证结点数小于等于500
"""
#class Node:
#    def __init__(self, x):
#          self.val = x
#          self.left = None
#          self.right = None


class TreePrinter:
    def printTree(self, root):
        if not root:
            return []
        queue = [root, '#']
        res = []
        tmp = []
        while queue:
            cur = queue.pop(0)
            if cur == '#':
                res.append(tmp)
                tmp = []
            else:
                tmp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                if queue[0] == '#':
                    queue.append('#')
        return res[:-1]

class TreePrinter:
    def printTree(self, root):
        if not root:
            return []
        queue = [root]
        tmp = []
        res = []
        last = nlast = root
        while queue:
            cur = queue.pop(0)
            tmp.append(cur.val)
            if cur.left:
                queue.append(cur.left)
                nlast = cur.left
            if cur.right:
                queue.append(cur.right)
                nlast = cur.right
            if cur == last:
                res.append(tmp)
                tmp = []
                last = nlast
        return res

if __name__ == "__main__":
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
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)

    head.left = one
    head.right = two
    one.left = three
    one.right = four
    three.left= seven
    three.right = eight
    four.left = nine
    four.right = ten

    two.left = five
    two.right = six
    five.left = eleven
    five.right=twelve
    six.left = thirteen
    six.right = fourteen

    t = TreePrinter()
    print t.printTree(head)
