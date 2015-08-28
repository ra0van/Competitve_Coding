class Node:
	def __init__(self,data=None,prev=None,next=None):
		self.data = data
		self.prev = prev
		self.next = next

	def __str__(self):
		return "Node[Data: "+str(self.data)+" ]"

class DoubleLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self,data):
		if (self.head==None):
			self.head = Node(data)
			self.tail = self.head
		else:
			curr = self.head
			while  curr.next!=None:
				curr = curr.next

			if curr!=None:
				tmpNode = Node(data)
				curr.next = tmpNode	
				tmpNode.prev = curr
				self.tail = tmpNode

	def delete(self,data):
		curr = self.head
		if curr.data == data:
			self.head = curr.next
			self.head.prev = None
			return True
		if curr == None:
			return False
		elif self.tail.data == data:
			self.tail = self.tail.prev
			self.tail.next = None
			return True
		while curr!=None and curr.data!=data :
			curr = curr.next

		if curr.data == data:
			curr.prev.next = curr.next
			curr.next.prev = curr.prev
			return True

		return False

	def find(self,data):
		curr = self.head
		if curr == None:
			return False
		if self.head.data == data:
			return True
		if self.tail.data == data:
			return True

		while curr!=None:
			if curr.data==data:
				return True
			curr = curr.next

		return False

	def fwd_print(self):
		if self.head == None:
			print "No Elements"
			return False
		curr = self.head
		while curr!=None:
			print str(curr) + "-->",
			curr = curr.next
		print ""
		return True

	def rev_print(self):
		if self.head == None:
			print "No Elements"
			return False

		curr = self.tail

		while curr!=None:
			print "<--"+str(curr),
			curr = curr.prev
		print ""
		return True

# Initializing list
l = DoubleLinkedList()

# Inserting Values
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)

# Forward Print
l.fwd_print()

# Reverse Print
l.rev_print()

# Try to find 3 in the list
if (l.find(3)):
    print("Found")
else :
    print("Not found")

# Delete 3 from the list
l.delete(3)

# Forward Print
l.fwd_print()

# Reverse Print
l.rev_print()

# Now if we find 3, we will not get it in the list
if (l.find(3)):
    print("Found")
else :
    print("Not found")
