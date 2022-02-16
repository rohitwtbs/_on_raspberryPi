class Stack:
    def __init__(self, data ): 
        self.stack = []
        if(data):
            self.stack.append(data)

    def push(self, data ):
        self.stack.append(data)
    def pop(self):
        popped_elemnt = self.stack.pop()
    def show(self):
        for i in self.stack:
            print(i)

s = Stack(45)
s.push(23)
s.push(29)
s.push(695)
s.show()
s.pop()
s.show()

