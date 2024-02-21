import concurrent.futures
import ast, time

def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = numbers[len(numbers) // 2]
        left = [x for x in numbers if x < pivot]
        middle = [x for x in numbers if x == pivot]
        right = [x for x in numbers if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def split_list(numbers, N):
    """Teilt die Liste in N annähernd gleich große Teile"""
    avg = len(numbers) / float(N)
    splitted = []
    last = 0.0

    while last < len(numbers):
        splitted.append(numbers[int(last):int(last + avg)])
        last += avg

    return splitted

def merge_lists(lists):
    """Verschmilzt mehrere sortierte Listen zu einer einzigen sortierten Liste"""
    while len(lists) > 1:
        merged_lists = []
        for i in range(0, len(lists), 2):
            if i + 1 < len(lists):
                merged_lists.append(merge_sorted_lists(lists[i], lists[i+1]))
            else:
                merged_lists.append(lists[i])
        lists = merged_lists
    return lists[0]

def merge_sorted_lists(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main(N=8):

    start_time = time.time()

    file_path = 'numbers.txt'
    with open(file_path, 'r') as file:
        numbers = ast.literal_eval(file.read())

    splitted_lists = split_list(numbers, N)

    with concurrent.futures.ProcessPoolExecutor() as executor:
        sorted_sublists = list(executor.map(quicksort, splitted_lists))

    sorted_list = merge_lists(sorted_sublists)

    end_time = time.time()

    print(f'Executiontime {end_time - start_time} seconds')

if __name__ == '__main__':
    main(N=8)
