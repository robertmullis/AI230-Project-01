import random, time
from mysort import my_sort          # your sort, in mysort.py

def clock(sort_fn, data):
    start = time.perf_counter()
    sort_fn(list(data))                # fresh copy every run
    return time.perf_counter() - start

nums = [random.randint(0, 999_999) for _ in range(20_000)]
shapes = [("shuffled", nums), ("already sorted", sorted(nums)), ("reversed", sorted(nums, reverse=True))]
for name, data in shapes:
    print(f"{name:>14}:  mine {clock(my_sort, data):8.3f} s   sorted() {clock(sorted, data):8.3f} s")