def partition(x, left, right):
	#pick the pivot element
	s = left
	
	pivot = x[s]

	for i in range(left+1, right):
		#invariant: i > s
		if x[i] < pivot:
			s += 1
			(x[s], x[i]) = (x[i], x[s])

	#insert pivot
	(x[s], x[left]) = (x[left], x[s])

	return s

def kth(x, k):
	return kthaux(x, k, 0, len(x))

def kthaux(x, k, left, right):
	"""

		Keywork arguments
		x -- the list
		k -- the kth element of sort(x)

	"""
	s = partition(x, left, right)

	if s > k: return kthaux(x, k, left, s)
	if s < k: return kthaux(x, k, s+1, right)
	if s == k: return x[s]