import os
import heapq
def read_calories():

    with open('inputs.txt') as inputs:
        total = 0
        for line in inputs:
            if line.strip().isnumeric():
                total += int(line.strip())
            else:
                yield total
                total = 0
        

if __name__ == '__main__':
    
    calories = []
    TOP_K = 3


    for total in read_calories():
        heapq.heappush(calories, -total)
    
    total = 0
    for i in range(TOP_K):
        total += abs(heapq.heappop(calories))
    
    print(total)