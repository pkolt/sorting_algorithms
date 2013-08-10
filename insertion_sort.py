# coding: utf-8

"""
Сортировка вставками (Insertion sort)
"""


def swap(arr, i1, i2):
    """Функция меняет местами элементы массива"""
    temp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = temp


def insertion_sort(arr):
    """Сортировка вставками"""

    # кол-во элементов в последовательности
    n = len(arr)
    for i in xrange(1, n):
        k = i
        while k > 0 and arr[k] < arr[k-1]:
            swap(arr, k, k-1)
            k -= 1
    return arr


import time
import random

arr = list(range(10000))
random.shuffle(arr)

start_cpu = time.clock()
start_real = time.time()

out = insertion_sort(arr)

end_cpu = time.clock()
end_real = time.time()

print 'Тест: %s' % (out[:20] == list(range(20)))
print 'Процессорное время в секундах %f' % (end_cpu - start_cpu)
print 'Действительное время в секундах %f' % (end_real - start_real)