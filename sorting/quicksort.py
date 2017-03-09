from random import randint

#Complexity
def partition(a):
	pivot = a[len(a)//2]

	lowest = [v for v in a if v < pivot]
	greatest = [v for v in a if v > pivot]

	return lowest, pivot, greatest

def quicksort(a):
	if len(a) <= 1:
		return a

	lowest, pivot, greatest = partition(a)
	return quicksort(lowest) + [pivot] + quicksort(greatest)

def main():
	a = [1, 27, 77, 3, 88, 2, -1]
	print(quicksort(a))
	
	return 0

if __name__ == '__main__':
	main()
	
