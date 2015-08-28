# Using Lists as a stack 
# it has both append(push) and pop  operations


stack = [1,2,3,4,5,6]

print "Original Contents of the stack"
print stack

print "pushing on to the stack"
stack.append(10)
stack.append(7)

print stack

print "pop contents from the stack"

tmp = stack.pop()
print "popped value from stack",tmp

print "stack after popping."
print stack


