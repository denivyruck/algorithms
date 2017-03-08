
class Node(object): 
	def __init__(self, v):
		self.l = None
		self.r = None
		self.v = v
		
class Tree(object):
	def __init__(self):
		self.root = None

	def add(self, v):
		if self.root == None:
			self.root = Node(v)
		else:
			self._add(v, self.root)
	
	def _add(self, v, node):
		if v < node.v:
			if node.l != None:
				return self._add(v, node.l)
			else:
				node.l = Node(v)
		else:
			if node.r != None:
				return self._add(v, node.r)
			else:
				node.r = Node(v)

	def search(self, v, node=None):
		if node == None or node.v == v:
			return node
		if v < node.v:
			return self.search(v, node.l)
		return self.search(v, node.r)
	
	def iteractive_search(self, v, node=None):
		while node != None and v != node.v:
			if v < node.v:
				node = node.l
			else:
				node = node.r
		return node

	def inorder(self, node):
		if node != None:
			self.inorder(node.l)
			print(node.v)
			self.inorder(node.r)

	def printTree(self):
		if self.root != None:
			self._print_tree(self.root)

	def _print_tree(self, node):
		if node != None:
			self._print_tree(node.l)
			print(str(node.v) + '  ')
			self._print_tree(node.r)

if __name__ == '__main__':
	t = Tree()
	t.add(1)
	t.add(5)
	t.add(12893)
	t.add(7)
	t.add(222)
	t.printTree()

