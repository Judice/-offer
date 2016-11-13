# coding=utf-8
"""
    题目描述:
        用两个栈来实现一个队列, 并实现两个函数appendTail, deleteHead, 分别完成
        在队列尾部插入结点和在队列头删除结点的功能
    思路:
        栈1用来存放元素， 栈2用来出栈, 入队列时直接把元素入栈到栈1，
        出队列时，如果栈2为空，遍把栈1全部出栈并入栈到栈2, 栈2再出栈
"""


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, n):
        self.stack1.append(n)

    def deleteHead(self):
        while self.stack1 != []:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
