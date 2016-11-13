# coding=utf-8
"""
   反转列表 方法二:递归
"""
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


def reverse_recursion(head):
    if not head or not head.next:
        return head

    newhead = reverse_recursion(head.next)

    head.next.next = head
    head.next = None

    return newhead

if __name__ == "__main__":
    three = Node(3)

    two= Node(2)
    two.next = three

    one = Node(1)
    one.next = two

    head = Node(0)
    head.next = one

    new_head = reverse_recursion(head)
    while new_head:
        print new_head
        new_head = new_head.next
