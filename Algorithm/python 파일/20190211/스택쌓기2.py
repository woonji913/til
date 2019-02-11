s = []

def push(item):
    s.append(item)

def pop():
    if len(s) == 0:
        print("stack is Empty!")
        return
    else:
        return s.pop(-1)

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())