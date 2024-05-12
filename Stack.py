import time

class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def read(self):
        return self.data[-1]
    
class Stack2:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)
    
    def pop(self):
        return self.data.pop()    

    def read(self):
        return self.data[-1]

class Queue:
    def __init__(self):
        self.data = []

    
    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        return self.data.pop(0)
    
    def read(self):
        return self.data[0]
        
    

def testQueue():
    myQueue = Queue()

    time.sleep(1)
    myQueue.enqueue(1)
    print("Inserting ", 1)
    time.sleep(1)
    myQueue.enqueue(2)
    print("Inserting ", 2)
    time.sleep(1)
    myQueue.enqueue(3)
    print("Inserting ", 3)

    time.sleep(1)
    print(myQueue.read())
    myQueue.dequeue()
    time.sleep(1)
    print(myQueue.read())
    myQueue.dequeue()
    time.sleep(1)
    print(myQueue.read())
    myQueue.dequeue()
    time.sleep(1)


class Linter:

    def __init__(self):
        self.stack = Stack()
    


    @classmethod
    def is_opening_brace(cls, char):
        try: 
            return {"(": True, "[": True, "{": True}[char]
        except:
            return False
        
    @classmethod
    def is_closing_brace(cls, char):
        try:
            return {"}": True, "]": True, ")": True}[char]
        except: 
            return False

    @classmethod
    def is_not_match(cls, opening_brace, closing_brace):
        if closing_brace != {"(": ")", "{": "}", "[": "]"}[opening_brace]:
            return False 
        else:
            return True 
        

    def lint(self, code):
        for char in code:
            if Linter.is_opening_brace(char):
                self.stack.push(char)

            elif Linter.is_closing_brace(char):
                popped_brace = self.stack.pop()

                if not popped_brace:
                    raise Exception(f"Error: {char} has no matching opening brace")

                if not Linter.is_not_match(popped_brace, char):
                    raise Exception(f"Error: {popped_brace} has no matching closing brace")
            
        if self.stack.read():
            raise Exception(f"Error: {self.stack.read()} has no matching closing brace.")




        
Linter().lint("(var {x=y}")