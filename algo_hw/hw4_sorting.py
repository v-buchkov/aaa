"""Task 1"""
# def check_rotation(arr: list, shift: int = 0) -> int:
#     n = len(arr)
#     if n > 2:
#         mid = int(n / 2)
#         if arr[mid - 1] > arr[mid] and arr[mid] < arr[mid + 1]:
#             return shift + mid
#         elif arr[mid] > arr[mid + 1] and arr[mid - 1] < arr[mid]:
#             return shift + mid + 1
#         elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
#             return check_rotation(arr[:mid], shift) + check_rotation(arr[mid:], shift + mid)
#         else:
#             arr.reverse()
#             return check_rotation(arr)
#     elif n == 2:
#         if arr[0] < arr[1]:
#             return 0
#         else:
#             return 1
#     else:
#         return 0
#
#
# def solution():
#
#     arr = list(map(int, input().split()))
#     i = check_rotation(arr)
#     print(i)
#
#
# solution()

"""Task 2"""
def find_elem_in_arr(arr: list, elem: int, shift: int = 0) -> int:
    rotation = check_rotation(arr)
    original = arr[rotation:] + arr[:rotation]
    original_index = binary_search(original, elem)
    if original_index == -1:
        return -1
    answer = original_index + rotation
    if answer > len(arr) - 1:
        return answer - len(arr) + 1
    else:
        return answer

def binary_search(arr: list, x: int):
	l = 0
	r = len(arr) - 1

	while l <= r:
		mid = l + (r - l) // 2

		if arr[mid] == x:
			return mid
		elif arr[mid] < x:
			l = mid + 1
		else:
			r = mid - 1
	return -1


def check_rotation(arr: list, shift: int = 0) -> int:
    n = len(arr)
    if n > 2:
        mid = int(n / 2)
        if arr[mid - 1] > arr[mid]:
            return shift + mid
        elif arr[mid] > arr[mid + 1]:
            return shift + mid + 1
        else:
            return check_rotation(arr[:mid], shift) + check_rotation(arr[mid:], shift + mid)
    elif n == 2:
        if arr[0] < arr[1]:
            return 0
        else:
            return 1
    else:
        return 0


def solution():
    arr = list(map(int, input().split()))
    elem = int(input().strip())
    index = find_elem_in_arr(arr, elem)
    print(index)


solution()
