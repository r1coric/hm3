def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid - 1
        else:
            return mid
    return left

def sort_list(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

input_sequence = input("Введите последовательность чисел через пробел: ")
try:
    input_list = [int(x) for x in input_sequence.split()]
except ValueError:
    print("Ошибка! В последовательности содержатся недопустимые значения")
else:
    number = input("Введите любое число: ")
    try:
        number = int(number)
    except ValueError:
        print("Ошибка! Введено недопустимое число")
    else:
        input_list = sort_list(input_list)
        position = binary_search(input_list, number)
        if position < len(input_list):
            print(f"Позиция числа {number} в отсортированном списке: {position+1}")
        else:
            print(f"Число {number} больше всех чисел в последовательности")