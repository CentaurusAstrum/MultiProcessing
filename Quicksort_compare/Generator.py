import numpy as np
import os

numbers = []
def numbers_generater(N):
    generated = [_ for _ in range(1, N+ 1)]
    np.random.shuffle(generated)
    numbers.extend(generated)
    file_path = './numbers.txt'
    with open(file_path, 'w') as file:
        file.write(str(numbers))
numbers_generater(10_000_000)

#Multi   1_000_000 elemente 21.442058324813843 seconds

