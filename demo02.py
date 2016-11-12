# coding=utf-8
"""
    问题描述:
        斐波那契数列
        实现一个类， 可通过键值访问， 第n个斐波那契数, 也可通过切片方式
        访问, 例如
        ```
            fib = Fib()
            fib[3] # 2
            fib[0:5] #[0, 1, 1, 2, 3]
        ```
"""
class Solution():
    def __init__(self):
        self.fib = [0, 1]
        self.len = 2

    def __getitem__(self,n):
        if isinstance(n, int):
            if n < self.len:
                return self.fib[n]

            for i in xrange(self.len-1, n):
                self.fib.append(self.fib[i-1]+self.fib[i])
                self.len += 1
            return self.fib[n]

        if isinstance(n, slice):
            start = n.start
            stop = n.stop

            if not isinstance(start,int):
                raise ValueError('start value must be int')
            if not isinstance(stop, int):
                raise ValueError('stop value must be int')

            for i in xrange(self.len-1, stop-1):
                self.fib.append(self.fib[i-1]+self.fib[i])
                self.len += 1
            return self.fib[start:stop]

