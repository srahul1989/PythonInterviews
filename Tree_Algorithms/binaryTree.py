#
#
###

class BinaryTree:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self):
		self.key = obj

	def getRootVal(self):
		return self.key

r = BinaryTree('a')
print r.getRootVal()
#print r.getLeftChild()
#print r.getRightChild()
r.insertLeft('b')
r.insertRight('c')
print (r.getLeftChild())
print (r.getRightChild())



