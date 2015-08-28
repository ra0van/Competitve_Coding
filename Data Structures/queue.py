# Using Deques from collections as a queue
# List can also be used, but they are not as efficient as deques

from collections import deque
queue = deque(["London","Paris","New York","Delhi"])
print "This is original queue";
print queue

print "Adding more to the queue"
queue.append("Bangalore");
queue.append("Leh");

print queue

dequedElemnt1 = queue.popleft()
dequedElemnt2 = queue.popleft()

print "Deuquing element 1: ",dequedElemnt1 
print "Deuquing element 2: ",dequedElemnt2 

print "Final state of the queue"
print queue

