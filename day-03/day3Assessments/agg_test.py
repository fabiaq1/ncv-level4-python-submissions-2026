# NCV Level 4 | Day 3 Collections and Records | example: agg_test
# Type it in Thonny, run it, then change one thing.
data = [65,72,48,90,55,72,48,72]
def mode_of(values):
    counts = {}
    for v in values:
        if v in counts:
            counts[v] = counts[v] + 1
        else:
            counts[v] = 1
    best = 0
    for v in counts:
        if counts[v] > best:
            best = counts[v]
    modes = []
    for v in counts:
        if counts[v] == best:
            modes.append(v)
    return modes


def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def find_all(values, target):
    positions = []
    for i in range(len(values)):
        if values[i] == target:
            positions.append(i)
    return positions

def count_of(values, target):
    count = 0
    for v in values:
        if v == target:
            count = count + 1
    return count

def total_of(values):
    total = 0
    for v in values:
        total = total + v
    return total

def mean_of(values):
    return total_of(values)/len(values)

def max_of(values):
    best = values[0]
    for v in values:
        if v > best:
            best = v
    return best

def min_of(values):
    lowest = values[0]
    for v in values:
        if v < lowest:
            lowest = v
    return lowest


print("Total  :", total_of(data))
print("Mean   :", mean_of(data))
print("Highest:", max_of(data))
print("Lowest :", min_of(data))
print("First 72 at:", find_first(data, 72))
print("All 72 at  :", find_all(data, 72))
print("Count of 72:", count_of(data, 72))
print("Mode   :", mode_of(data))
print("Mode (tie):", mode_of([1, 2, 2, 3, 3]))

# Expected output:
# Total  : 522
# Mean   : 65.25
# Highest: 90
# Lowest : 48
# First 72 at: 1
# All 72 at  : [1, 5, 7]
# Count of 72: 3
# Mode   : [72]
# Mode (tie): [2, 3]
