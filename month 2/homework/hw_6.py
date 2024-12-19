def selection_sort(unsorted_list):
    list_length = len(unsorted_list)
    for start_number in range(list_length):
        max_number = unsorted_list[0]
        max_index = 0
        for check_number in range(1, list_length - start_number):
            if max_number < unsorted_list[check_number]:
                max_number = unsorted_list[check_number]
                max_index = check_number

        unsorted_list[max_index], unsorted_list[list_length- start_number - 1] = unsorted_list[list_length - start_number - 1], unsorted_list[max_index]

    return unsorted_list

print(selection_sort([895, 945, 852, 560, 126, 164, 305, 471, 379, 952, 102, 5]))


def binary_search(val, A):
    N = len(A) #5000
    result_ok = False
    first = 0
    last = N - 1
    pos = 0
    while first < last:
        middle = round((first + last) / 2)

        if val == A[middle]:
            first = middle
            last = first
            result_ok = True
            pos = middle

        else:
            if val > A[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if result_ok == True:
        print('Элемент найден')
        print(pos)
    else:
        print('Элемент не найден')

binary_search_list = [number for number in range(5000)]
binary_search(3579, binary_search_list)