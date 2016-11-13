# coding=utf-8
"""
   反转链表
        方法一:循环迭代
"""


class Node():
    def __init__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)           #self.value可以输出字符串


    #方法一:循环迭代


    def reverse_loop(self,head):
        if head == None or head.next == None:
            return head
        prv = None
        while head:
            tmp = head.next      #缓存当前节点的向后指针
            head.next = prv      #反转指针方向
            prv = head           #下次迭代时的向前指针
            head = tmp           #下次迭代时的当前节点
        return prv

if __name__ == "__main__":
    three = Node()
    three.value = 3

    two = Node()
    two.value = 2
    two.next = three

    one = Node()
    one.value = 1
    one.next = two

    head = Node()
    head.value = 0
    head.next = one

    s = Node()
    newhead = s.reverse_loop(head)
    while newhead:
        print newhead
        newhead = newhead.next

