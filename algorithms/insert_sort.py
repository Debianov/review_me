target = [2, 3, 6, 8, 1, 23423, -1]
for currentElementIndex in range(1, len(target)):
	for shiftedElementIndex in range(currentElementIndex, 0, -1):
		if target[shiftedElementIndex] < target[shiftedElementIndex - 1]:
			target[shiftedElementIndex], target[shiftedElementIndex - 1] = target[shiftedElementIndex - 1], target[shiftedElementIndex]
		else:
			break