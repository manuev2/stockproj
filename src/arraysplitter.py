import math
import numpy as np

def arraysplitter(array: list, subarrays: int):
    splitarray = []
    # Ceiling for index of where to split
    splitval = math.ceil(len(array) / subarrays)
    # Split array
    splitarray = [array[x:x + splitval] for x in range(0, len(array), splitval)]
    # Print arrays
    # for x in range(len(splitarray)):
    #     print(splitarray[x])
    return splitarray