class Queue:
    def __init__(self):
        self.list = []

    def length(self):
        return len(self.list)

    def isEmpty(self):
        return self.length() == 0
    
    def add(self, item):
        self.list.append(item)
        return

    def remove(self):
        self.list = self.list[1:]
        return

    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.list[0]

    def display(self):
        return self.list

q = Queue()
q.add(10)
q.add(9)
q.add(8)
print(q.display())
q.remove()
print(q.display())

