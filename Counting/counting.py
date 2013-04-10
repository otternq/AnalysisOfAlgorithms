def count(size, cardinality):
	x = array(size, 0)
	done = False

	while not done:
		print(x)

		for ii in range(0, size):
			i = (size-1) - ii;
			if x[i] < cardinality - 1:
				x[i] += 1
				break
			else:
				x[i] = 0

				if i == 0:
					done = True

def gray(i):
	return i ^ (i >> 1)

if __name__ == "__main__":

	print("Count")
	count(3, 3);
	count(3, 2);

	print("Grey")
	for i in range(0, 1<<4):
		print(i, gray(i+1), gray(i), gray(i+1) - gray(i))
