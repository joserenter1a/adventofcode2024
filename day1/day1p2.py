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

    # lambda function to calculate absolute distance between two points
    dist = lambda a, b: abs(a - b)
    total_distance = 0
    # go through list and calculate total distance
    for i in range(len(leftlist)): #O(n)
        total_distance += dist(leftlist[i], rightlist[i])
    
    return total_distance

if __name__ == '__main__':
    main()
    print(main())
