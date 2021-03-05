class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, value):      # 데이터 입력
        self.data.append(value)
    
    def pop(self):      # 마지막 데이터 삭제
        if self.is_empty():
            return
        else:
            return self.data.pop(-1)
    
    def peek(self):     # 마지막 원소 확인
        if self.is_empty():
            return
        else:
            last_index = len(self.data) -1
            return self.data[last_index]
    
    def is_empty(self):     # 비었는지 확인
        return not self.data

def book():
    stack = Stack()
    k = int(input())
    for _ in range(k):
        a = int(input())
        if a == 0:
            stack.pop()
        else:
            stack.push(a)
    print(sum(stack.data))

if __name__ == "__main__":
    book()
    