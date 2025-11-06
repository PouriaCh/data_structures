from typing import List


def bubble_sort(input_list: List[int]) -> List[int]:
    for i in range(len(input_list) - 1, 0, -1):
        for j in range(i):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return input_list


def selection_sort(input_list: List[int]) -> List[int]:
    for i in range(len(input_list) - 1):
        min_index = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_index] > input_list[j]:
                min_index = j
        input_list[min_index], input_list[i] = input_list[i], input_list[min_index]
    return input_list


def insertion_sort(input_list: List[int]) -> List[int]:
    for i in range(1, len(input_list)):
        temp = input_list[i]
        j = i - 1
        while j >= 0 and temp < input_list[j]:
            input_list[j + 1], input_list[j] = input_list[j], temp
            j -= 1
    return input_list


input_list = [4, 2, 6, 5, 1, 3]

print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(f"INPUT LIST: {input_list}")
print(f"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
print(f"BUBBLE SORT: {bubble_sort([4, 2, 6, 5, 1, 3])}")
print(f"SELECTION SORT: {selection_sort([4, 2, 6, 5, 1, 3])}")
print(f"INSERTION SORT: {insertion_sort([4, 2, 6, 5, 1, 3])}")
