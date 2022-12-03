def read_calories():

    with open('./inputs.txt') as inputs:
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