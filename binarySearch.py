#
#
####

def binarySearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		midpoint = (first + last)//2
		if alist[midpoint] == item:
			found = True
		else:
			if item < alist[midpoint]:
				last = midpoint - 1
			else:
				first = midpoint + 1
	return found

testList = [0,2,4,5,7,9,12,23,34,45,56,67,78,89,90]
print(binarySearch(testList, 3))
print(binarySearch(testList, 13))