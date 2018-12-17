class Stack_operations :
	
	size = 10
	def __init__(self):
		self.count = 0
		self.list = []
		self.stack_elements = []

	#To check if the stack is empty
	def is_empty(self):
		return self.count == 0

	#To check if the stack is full
	def is_full (self):
		return self.count == Stack_operations.size

	#To insert an elements into the stack
	def push(self,element):
		#element = int(input("enter the elements"))
		if not self.is_full():	
			self.list.append(element)
			print (self.list)
			self.count += 1
		else:
			print ("Stack is full")

	#To remove the element from the stack
	def pop(self):
		if not self.is_empty() :
			ele = self.list.pop()
			self.count -=1 
			self.stack_elements.append(ele)
		else:
			print ("Stack is empty")
		print(self.stack_elements)

	#It returns the element at the top of the stack else NULL, if the stack is empty	
	def peek(self):
		if not self.is_empty(): 
			return self.list[-1]
		else:
			return null

	def length(self):
		return self.count
	
#assertions
o1 = Stack_operations()
assert(o1.length() == 0)
o1.push(10)
o1.push(20)
o1.push(30)
assert(o1.peek() == 30)


		
			
