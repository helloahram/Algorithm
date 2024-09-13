class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from Empty Stack")
        
    def peep(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from Empty Stack")
        
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)