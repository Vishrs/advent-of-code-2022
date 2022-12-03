def read_calories():

    with open('/Users/tjw815/projects/adventOfCode2022/advent-of-code-2022/day1/inputs.txt') as inputs:
        total = 0
        for line in inputs:
            if line.strip().isnumeric():
                total += int(line.strip())
            else:
                yield total
                total = 0
        

if __name__ == '__main__':
    max_calories = 0
    for total in read_calories():
        max_calories = max(total, max_calories)
    
    print(max_calories)