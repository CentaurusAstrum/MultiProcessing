from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [_ for _ in range(1000)]))

if __name__ == '__main__':
    print('_'*50)