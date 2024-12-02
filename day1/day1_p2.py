# Advent of code day 1 part 2
# similarity score

def open_and_init():
    # initialize lists
    leftlist = []
    rightlist = []

    with open('input.txt', 'r') as file: #O(N)
        for line in file:
            right, left = map(int, line.strip().split())
            leftlist.append(left)
            rightlist.append(right)

    leftlist.sort()
    rightlist.sort()

    def freq_map_init(list: [int]):
        # returns a frequency map given a list of ints
        freq = {}
        for i in list:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq

    freq = freq_map_init(rightlist)

    similarity = 0
    for el in leftlist:
        if el in freq:
            similarity +=  el * freq[el] 
    return similarity

if __name__ == '__main__':
    open_and_init()

