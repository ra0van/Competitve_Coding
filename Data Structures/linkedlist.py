class Node:
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next
	def __str__(self):
		return "Node[Data= " + str(self.data)+" ]"

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self,data):
		if(self.head == None):
			self.head = Node(data)
		else:
			curr = self.head
			while (curr.next!=None) :
				curr = curr.next
			curr.next = Node(data)

	def delete(self,data):
		curr = self.head

		if curr.data == data:
			self.head = curr.next
		elif curr==None:
			return False
		else:
			while curr!=None and curr.next!=None and curr.next.data!=data:
				curr=curr.next
			if curr!=None and curr.next!=None:
				curr.next = curr.next.next

	def find(self,data):
		curr = self.head
		if curr == None:
			return False

		while curr!=None and curr.data!=data and curr.next!=None:
			curr = curr.next

		if curr.data == data:
			return True
		return False



	def display(self):
		curr = self.head
		while curr!=None:
			print str(curr) + "-->",
			curr = curr.next
		print ""


# Initialize a new linked list
print "Initializing linked list"
ll = LinkedList()

# Insert values in the linked list
print "Inserting values 1,2,3,9 in the Linked List"
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(9)

# Display the linked list
print "Displaying the linked list"
ll.display()

# Delete an element from the linked list. Demonstrate the Delete function
print "Delete an element (data = 3) from the linked list"
ll.delete(3)

print "Display the linked list again. The value 3 is deleted. "
ll.display()

# Try to find the value 2 in the linked list (Demonstrating the Find function)
print "Try to find the value 2 in the linked list"
found = ll.find(2)
if found == True:
	print "The value 2 is present in the Linked List"
else:
	print "The value 2 is not present in the linked list"

# Try to find the value 20 in the linked list
print "Try to find the value 20 in the linked list"
found = ll.find(20)
if found == True:
	print "The value 20 is present in the Linked List"
else:
	print "The value 20 is not present in the linked list"

		