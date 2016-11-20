# coding=utf-8
"""
    题目描述:
        用两个栈来实现一个队列, 并实现两个函数appendTail, deleteHead, 分别完成
        在队列尾部插入结点和在队列头删除结点的功能
"""


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, n):
        self.stack1.append(n)
        return self.stack1

    def deleteHead(self):
        if self.stack2 == []:
            while self.stack1:
                 self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
