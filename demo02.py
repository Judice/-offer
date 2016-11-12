# coding=utf-8
class TestRange():            #使用迭代器实现range函数功能
    def __init__(self, r):
        self.value = 0
        self.r = r

    def next(self):
        fir = self.value
        self.value += 1
        if self.value > self.r:
            raise StopIteration
        return fir

    def __iter__(self):
        return self


class RangeIterator():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def next(self):
        fir = self.a
        self.a += 1
        if self.a > self.b:
            raise StopIteration
        return fir

    def __iter__(self):
        return self


class RangeStep():
    def __init__(self,a,b,step):
        self.a = a
        self.b = b
        self.step = step

    def next(self):
        fir = self.a
        self.a = self.a + self.step
        if self.a > self.b:
            raise StopIteration
        return fir

    def __iter__(self):
        return self

if __name__ == "__main__":
    r1 = TestRange(8)
    print list(r1)
    print range(8)
    r2 =RangeIterator(2,8)
    print list(r2)
    print range(2,8)
    r3 = RangeStep(2,8,2)
    print list(r3)
    print range(2,8,2)