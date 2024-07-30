def binary_search_recursive(list,low, high, target):
	
	while low <= high:
		mid = (low + high)//2

		if list[mid] == target:
			return mid
		elif list[mid] < target:
			low = mid + 1
			return binary_search_recursive(list, low, high, target)
		else:
			high = mid - 1
			return binary_search_recursive(list, low, high, target)
	return None


def verify(index):
	if index is not None:
		print("Target found at", index)
	else:
		print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search_recursive(numbers,0, len(numbers)-1, 12)
verify(result)


result = binary_search_recursive(numbers,0, len(numbers)-1, 2)
verify(result)
