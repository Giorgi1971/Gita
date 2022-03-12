class Stack:
    def __init__(self):
        self.__ls = []

    def push(self, val):
        self.__ls.append(val)

    def pop(self):
        val = self.__ls[-1]
        del self.__ls[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        self.__sum = 0
        Stack.__init__(self)
    
    def get_counter(self):
        return self.__sum

    def pop(self):
        vl = Stack.pop(self)
        self.__sum += vl
        return vl


stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
