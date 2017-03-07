#Good sorting algorithm, but a good implementation of quicksort usually beats it

#O(lg(n)) or O(h)
def max_heapity(A, i):
	l = i*2+1
	r = i*2+2

	if l < len(A) and A[l] > A[i]:
		largest = l
	else:
		largest = i
	if r < len(A) and A[r] > A[largest]:
		largest = r
	
	#If is greater, swap it and propagate changes
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapity(A, largest)

#O(n)
def build_max_heap(A):
	for i in range(len(A)//2-1, -1, -1):
		max_heapity(A, i)

def heapsort(A):
	sorted_list = []
	i = len(A)-1

	build_max_heap(A)
	while i >= 0:
		A[0], A[i] = A[i], A[0]
		greatest = A.pop()
		sorted_list = [greatest] + sorted_list
		max_heapity(A, 0)
		i -= 1
	return sorted_list

def main():
	a = [12, 6, 2, 3, 666, 42, 2, 1]
	sl = heapsort(a)
	print(sl)

if __name__ == '__main__':
	main()
