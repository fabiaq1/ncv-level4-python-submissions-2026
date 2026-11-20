# NCV Level 4 | Day 3 Collections and Records | example: sort_counts_run
# Type it in Thonny, run it, then change one thing.
import random
random.seed(7)
def bubble_counts(values):
    items = values[:]
    comps = 0
    swaps = 0
    n = len(items)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            comps = comps + 1
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swaps = swaps + 1
    return comps, swaps

def selection_counts(values):
    items = values[:]
    comps = 0
    swaps = 0
    for i in range(len(items) - 1):
        smallest = i
        for j in range(i + 1, len(items)):
            comps = comps + 1
            if items[j] < items[smallest]:
                smallest = j
        items[i], items[smallest] = items[smallest], items[i]
        swaps = swaps + 1
    return comps, swaps

for n in (8, 20, 100):
    values = [random.randint(0, 100) for _ in range(n)]
    print(n, "bubble", bubble_counts(values), "selection", selection_counts(values))

# Expected output:
# 8 bubble (28, 15) selection (28, 7)
# 20 bubble (190, 76) selection (190, 19)
# 100 bubble (4950, 2255) selection (4950, 99)
