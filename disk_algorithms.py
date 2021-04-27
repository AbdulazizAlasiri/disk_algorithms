#   This program implements the following disck-scheduling algorithms:
# FCFS, SCAN and C-SCAN
# The program services a disk of 5,000 cylinders numbered 0 to 4999.
# It generates a random series of 1000 cylinder requests and services
# them according to each of he algorithms listed above. The program
# will be passed the initial position of the disk head (as a parameter
# on the command line) and report the total amount of head movement
# required by each algorithm.
# To run:
# ./file_name followed by number from 0-4999 for index (see below for example)
# ./disk_algorithms 423


import sys
from random import randint

CYLINDERS = 5000
REQUESTS = 1000

# First-Come-First-Serve (fcfs) starts from the index after the starting
# index and continually adds the headmovement from the starting index in
# order recieved. If at end of array, start from index zero and continually
# add until starting index


def fcfs(requests: list, start: int):
    prev = start
    sum = 0
    for req in requests:
        sum += abs(req-prev)
        prev = req
    return sum

# SCAN starts from one left of start, and continually goes down to
# smallest element. Then starts at one higher than start and
# continually goes up to highest value (not 5000)


def scan(requests: list, start: int):
    requests.append(start)

    # remove anu repeated element
    list_set = set(requests)
    # convert the set to the list
    requests = (list(list_set))

    requests.sort()
    start_index = requests.index(start)

    prev = start
    sum = 0
    for req in reversed(requests[:start_index]):
        sum += abs(prev-req)
        prev = req

    for req in requests[start_index+1:]:
        sum += abs(prev-req)
        prev = req
    return sum

# Circular Scan (C-SCAN) - start at start index, increase to  the nearest end
# (even if no value at boundary), save boundary value, go to the secend boundary
# increase till last value before start value


def cscan(requests: list, start: int):
    # add the start ,  edge and  center to the requests list
    requests.append(start)
    requests.append(0)
    requests.append(CYLINDERS-1)

    # remove anu repeated element
    list_set = set(requests)
    # convert the set to the list
    requests = (list(list_set))

    requests.sort()
    start_index = requests.index(start)

    prev = start
    sum = 0
#  go from the current postion to the center
    if CYLINDERS-start >= start:
        for req in reversed(requests[:start_index]):
            sum += abs(prev-req)
            prev = req
        # got to the other end
        prev = requests[-1]
        for req in reversed(requests[start_index+1:]):
            sum += abs(prev-req)
            prev = req
        return sum
    else:
        for req in requests[start_index+1:]:
            sum += abs(prev-req)
            prev = req
        # got to the other end
        prev = requests[0]
        for req in requests[:start_index]:
            sum += abs(prev-req)
            prev = req
        return sum


def main():
    if len(sys.argv) != 2:
        print("Please run the program with starting index from 0-4999. Ex. ./Q1 423")
        exit(-1)
    start = int(sys.argv[1])
    requests = [randint(0, CYLINDERS-1) for _ in range(REQUESTS)]
    print("FCFS head movements: ", fcfs(requests, start))
    print("SCAN head movements: ", scan(requests, start))
    print("CSCAN head movements: ", cscan(requests, start))


if __name__ == '__main__':
    main()
