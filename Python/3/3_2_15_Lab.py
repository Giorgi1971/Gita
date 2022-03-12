class QueueError(IndexError):
    def __init__(self):
        IndexError.__init(self)
        print('QueError')


class Queue:
    def __init__(self):
        self.__ls = []

    def put(self, elem):
        self.__ls.insert(0, elem)

    def get(self):
        try:
            vl = self.__ls.pop()
            return vl
        except:
            raise QueueError


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("QuEEEEEEEerror")
except:
    print("Queue error")
