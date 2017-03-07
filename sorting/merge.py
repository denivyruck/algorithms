
def merge_sort(v):
	if len(v) < 2:
		return v[:]
	else:
		middle = len(v)//2
		left = merge_sort(v[:middle])
		right = merge_sort(v[middle:])
		return merge(left, right)

def merge(left, right):
	result = []
	i, j = 0, 0

	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	
	while i < len(left):
		result.append(left[i])
		i += 1
	while j < len(right):
		result.append(right[j])
		j += 1

	return result

def main():
	v = [2,3,5,1,24,7,3,21,3,65,674,13,4,45,7654,23,0]
	v = merge_sort(v)
	print(v)

if __name__ == '__main__':
	main()
