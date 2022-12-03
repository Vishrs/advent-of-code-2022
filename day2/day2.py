def read_strategy():
    
    winning_hand = {'A':'P', 'B':'S', 'C':'R'}
    draw_hand = {'A':'R', 'B':'P', 'C':'S'}
    lose_hand = {'A':'S', 'B':'R', 'C':'P'}
    round_scoring = {'Y':3, 'X':0, 'Z':6}
    play_scoring = {'R':1,'P':2,'S':3}

    total = 0
    with open('inputs.txt') as inputs:

        for line in inputs:
            round = line.strip().split(' ')
            
            if round[1] == 'Z':
                total += play_scoring[winning_hand[round[0]]]
            elif round[1] == 'Y':
                total += play_scoring[draw_hand[round[0]]]
            else:
                total += play_scoring[lose_hand[round[0]]]

            total += round_scoring[round[1]]

    return total

if __name__ == "__main__":
    print(read_strategy())