# LIFO - last in first out
class Stack:
    def __init__(self):
        self.data = []

    # Always
    def push(self, item):
        print(f"Pushing: {item}")
        self.data.append(item)

    # Always
    def pop(self):
        popped = self.data.pop(-1)
        print(f"Popping: {popped}")
        return popped

    # Optional
    def peek(self):
        print("Peeking: ")
        return self.data[-1]

    def getLength(self):
        return len(self.data)

    # Don't worry about this line
    def __str__(self):
        display = ",".join(str(data) for data in self.data)
        return f"[{display}]"


# Given a code file as a long string,
# check to see if the provided string
# has balanced brackets
# should return True or False
def balancedBrackets(code):
    pass


print(balancedBrackets("{age(cz{gge(gea[aa]gadz)}gea)}"))  # True
print(balancedBrackets("{age(cz{gge(gea[aa]gadz)gea)}"))  # True
print(balancedBrackets("{age(cz{gge(gea[aa]gadz)}gea)}}"))  # False
