
def partition(a, p, r):
	pivot = a[r]
	i = p-1

	for i in range(p, r-1):
		if a[i] < pivot:
			a[i], 

def quicksort(a, p, r):
	if p < r:
		q = partition(a, p, r)
