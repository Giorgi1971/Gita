class Po:
    def __init__(self, val=0) -> None:
        self.val = val


obj = Po()
obj1 = Po(98)
print(obj.val, ' - ', obj1.val)