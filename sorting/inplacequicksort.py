
#a[:i] stores the lowest of the items
def partition(a, p, r):
	pivot = a[r]
	i = p

	for j in range(p, r):
		if a[j] < pivot:
			a[i], a[j] = a[j], a[i]
			i += 1
	a[i], a[r] = a[r], a[i]
	
	return i

def quicksort(a, p, r):
	if p < r:
		q = partition(a, p, r)
		quicksort(a, p, q-1)
		quicksort(a, q+1, r)

def main():
	a = [1, 77, 2, -1, -2, -4, 666, 1, 42]
	quicksort(a, 0, len(a)-1)
	print(a)

	return 0

if __name__ == '__main__':
	main()
