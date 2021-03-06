class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push(self, val):
        self.__sum+=val
        Stack.push(self, val)

st1 = Stack()
sta = AddingStack()

st1.push(5)
print(st1.pop())
sta.push(5)
print(sta.pop())