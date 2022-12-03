def read_strategy():
    
    winning_hand = {'A':'Y', 'B':'Z', 'C':'X'}
    draw_hand = {'A':'X', 'B':'Y', 'C':'Z'}

    score = {'Y':2, 'X':1, 'Z':3}
    total = 0
    with open('inputs.txt') as inputs:

        for line in inputs:
            round = line.strip().split(' ')
            
            if winning_hand[round[0]] == round[1]:
                # won
                total += 6
            elif draw_hand[round[0]] == round[1]:
                total += 3

            total += score[round[1]]

    return total

if __name__ == "__main__":
    print(read_strategy())