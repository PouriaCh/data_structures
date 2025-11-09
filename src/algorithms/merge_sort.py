def merge(list1, list2):
    sorted_list = []
    i = 0
    j = 0
    while len(list1) > i and len(list2) > j:
        if list1[i] > list2[j]:
            sorted_list.append(list2[j])
            j += 1
        else:
            sorted_list.append(list1[i])
            i += 1
    while len(list1) > i:
        sorted_list.append(list1[i])
        i += 1
    while len(list2) > j:
        sorted_list.append(list2[j])
        j += 1
    return sorted_list


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list

    mid_index = int(len(my_list) / 2)
    left_list  = merge_sort(my_list[:mid_index])
    right_list = merge_sort(my_list[mid_index:])

    return(merge(left_list, right_list))


list1 = [1, 3, 7, 8]
list2 = [2, 4, 5, 6]

print(merge(list1, list2))
print(merge_sort([4, 1, 7, 3, 9]))