def binarySearch(x, value):
	return binarySearchAux(x, 0, len(x), value)

def binarySearchAux(x, left, right, value):
	
	if left == right:
		return None

	split = (left+right)//2 #integer divide (avoids floats)

	if value < x[split]:
		return binarySearchAux(x, left, split, value) 
	elif value > x[split]:
		return binarySearchAux(x, split + 1, right, value)
	elif value == x[split]:
		return split

if __name__ == '__main__':

	l = [1,2,3,4,5,6]
	index = binarySearch(l, 4)
	print(index)

