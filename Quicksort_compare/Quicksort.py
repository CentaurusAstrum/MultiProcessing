"""
    The program expects a python list in a textfile as input.
    Avg. runtime of Quickssort: O(n*log(n))
"""

import ast, time

start_time = time.time()
file_path = './numbers.txt'

with open(file_path, 'r') as file:
     numbers = ast.literal_eval(file.read())

def quicksort(numbers, l, r):
    if l < r:
        pivotIndex = divide(numbers, l, r)
        quicksort(numbers, l, pivotIndex)
        quicksort(numbers, pivotIndex + 1, r)

def divide(numbers, l, r):
    pivot = numbers[l + (r - l) // 2]
    while True:
        while numbers[l] < pivot:
            l += 1
        while numbers[r] > pivot:
            r -= 1
        if l >= r:
            return r
        numbers[l], numbers[r] = numbers[r], numbers[l]
        l += 1
        r -= 1
        
quicksort(numbers, 0, len(numbers) -1)

end_time = time.time()
print(f'Executiontime {end_time - start_time} seconds')
