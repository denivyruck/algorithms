#Implementation of a heap priority queue. all operations perform in lg(n) time

def heap_maximum(a):
	return a[0]

def max_heapify(a, i):
	l = i*2+1
	r = i*2+2

	if l < len(a) and a[l] > a[i]:
		largest = l
	else:
		largest = i
	if r < len(a) and a[r] > a[largest]:
		largest = r
	
	#If is greater, swap it and propagate changes
	if largest != i:
		a[i], a[largest] = a[largest], a[i]
		max_heapify(a, largest)

def extract_max(a):
	if len(a) < 1:
		raise 'Heap underflow'
	if len(a) == 1:
		return a.pop()
	
	top, a[0] = a[0], a.pop()
	max_heapify(a, 0)

	return top

def increase_key(a, i, key):
	if a[i] < key:
		raise 'smaller key'
	a[i] = key
	while i > 0 and a[i>>1] < a[i]:
		a[i], a[i>>1] = a[i>>1], a[i]
		i = i>>1

def main():
	a = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]
	print(extract_max(a))
	print(extract_max(a))
	print(extract_max(a))
	

if __name__ == '__main__':
	main()
