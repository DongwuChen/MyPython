# -*- coding: utf-8 -*-

from random import randint

__version__ = '0.1'
__author__ = 'dw'

def quick_sort(lists, left, right):
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists

def check(lists):
	for i in range(len(lists)-1):
		assert lists[i] <= lists[i + 1]
	print("The array is sorted")

if __name__ == '__main__':
	arr = []
	for i in range(1000):
		arr.append(randint(-2147483648, 2147483647))
	quick_sort(arr, 0, len(arr)-1)
	check(arr)
