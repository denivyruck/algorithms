def insertion_sort(v):
	for j in range(1, len(v)):
		key = v[j]

		i = j-1
		while i>=0 and v[i] > key:
			v[i+1] = v[i]
			i = i-1
		v[i+1] = key

def main():
	v = [2,1,2,5,6,2,4,7,9,33,2,23,777,23,32,1,233]
	insertion_sort(v)
	print(v)

if __name__ == '__main__':
	main()
