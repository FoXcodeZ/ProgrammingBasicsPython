import random

numbersList = []

def GetListOfRandomNumbers(range_min, range_max):
    return random.sample(range(range_min, range_max + 1), (range_max + 1) - range_min)


numbersList = GetListOfRandomNumbers(1, 15)
print(f"Numbers before sorting: {numbersList}")
numbersList.sort();
print(f"Numbers after sorting: {numbersList}")
