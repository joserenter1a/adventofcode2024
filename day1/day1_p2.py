# Advent of code day 1 part 2
# similarity score

def main():
    # initialize lists
    leftlist = []
    rightlist = []
    # open file
    with open('input.txt', 'r') as file: #O(N)
        # split line into two separate lists
        for line in file:
            right, left = map(int, line.strip().split())
            leftlist.append(left)
            rightlist.append(right)
    # sort lists into left and right
    leftlist.sort()
    rightlist.sort()

    # helper function to create a frequency map
    def freq_map_init(list: [int]):
        # returns a frequency map given a list of ints
        freq = {}
        for i in list:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq
    # initialize our map with the right list
    freq = freq_map_init(rightlist)

    similarity = 0
    # calculate similarity score based on formula given
    for el in leftlist:
        if el in freq:
            similarity +=  el * freq[el] 

    return similarity

if __name__ == '__main__':
    main()
    # print(main())
