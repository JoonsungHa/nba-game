#  File: Nim.py

#  Description: Program that allows us to find the winning move in the game nim sum

#  Student's Name: Joonsung Ha

#  Student's UT EID: jh69256
#  Partner's Name: Laurence Wang

#  Partner's UT EID: lnw653

#  Course Name: CS 313E

#  Unique Number: 50305

#  Date Created: 1/26/20

#  Date Last Modified:

#  Input: heaps is a list of integers giving the count in each heap
#  Output: function returns a single integer which is the nim-sum
def nim_sum(heaps):
    # this changes the elements in the list into integers
    for i in range(len(heaps)):
        into_int = int(heaps[i])
        heaps[i] = into_int

    # this lets me compare two heaps at a time and eventually find the nim_sum
    for i in range(len(heaps) - 1):
        value = heaps[i]^heaps[i+1]
        heaps[i + 1] = value

    return value


# placeholder for the actual return statement

#  Input: heaps is a list of integers giving the count in each heap
#         nim_sum is an integer
#  Output: function returns two integers. The first integer is number
#          of counters that has to be removed. The second integer is
#          the number of the heap from which the counters are removed.
#          If the nim_sum is 0, then return 0, 0



def find_heap(heaps, nim_sum):
    if nim_sum==0:
        return 0,0

    indivsums = []
    for i in range(len(heaps)):
        indivsums[i] = nim_sum(heaps[i])

    remove = 0
    spot = 0
    for i in range(len(indivsums)):
        if indivsums[i]<heaps[i]:
            remove = heaps[i]-indivsums[i]
            spot = i


    return remove,spot+1


def main():
    # read input from input file nim.txt
    data = open("nim.txt", "r")

    num_trials = data.readline()

    if num_trials == "":
        print("Lose Game")

    else:
        num_trials = int(num_trials)

        for i in range(num_trials):
            # gets each line of data from the textfile
            line = data.readline()

            # gets rid of the \n and the end
            line = line.strip()

            # makes the string into a list
            # elements in the list are all strings right now
            x = line.split(" ")
            # print(x)
            # print(type(x))
            y = find_heap(x, nim_sum(x))
            if y[1] == 0 and y[0] == 0:
                print("Lose Game")
            else:
                print("Remove "+str(y[0] + " counters from Heap "+str(y[1])))
                
    data.close()


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
