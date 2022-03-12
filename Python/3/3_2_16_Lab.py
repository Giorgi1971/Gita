class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self.queue = []
    
    def put(self,elem):
        self.queue.insert(0,elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError


class SuperQueue(Queue):
    def ie(self):
        if len(self.queue)>0:
            return False
        else:
            return True


print('-----------------')
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
print(que.queue)
for i in range(4):
    if not que.ie():
        print(que.get())
    else:
        print("Queue empty")
