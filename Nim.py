#  File: Nim.py

#  Description: Program that allows us to find the winning move in the game nim sum

#  Student's Name: Joonsung Ha

#  Student's UT EID: jh69256
#  Partner's Name: Laurence WAng

#  Partner's UT EID: lnw653

#  Course Name: CS 313E 

#  Unique Number: 50305

#  Date Created: 1/26/20

#  Date Last Modified:

#  Input: heaps is a list of integers giving the count in each heap
#  Output: function returns a single integer which is the nim-sum
def nim_sum (heaps):


    #this changes the elements in the list into integers
    for i in range(len(heaps)):
        into_int = int(heaps[i])
        heaps[i] = into_int

    #this returns binary
    for i in range(len(heaps)):
        into_binary = bin(heaps[i])
        heaps[i] = into_binary


    #this lets me compare two heaps at a time and eventually find the nim_sum

    for i in range(len(heaps)-1):
        print("iii",i)
        xor_operator(heaps[i],heaps[i+1])





    
    return 0
# placeholder for the actual return statement

#  Input: heaps is a list of integers giving the count in each heap
#         nim_sum is an integer 
#  Output: function returns two integers. The first integer is number
#          of counters that has to be removed. The second integer is
#          the number of the heap from which the counters are removed.
#          If the nim_sum is 0, then return 0, 0



def find_heap (heaps, nim_sum):


    
  return 0, 0		# placeholder for the actual return statement



def xor_operator(heap1, heap2):
    print("it hits")
    print(heap1,heap2)





def main():
  # read input from input file nim.txt
    data = open("nim.txt","r")

    num_trials = data.readline()
    num_trials = int(num_trials)

    for i in range(num_trials):
        #gets each line of data from the textfile
        line = data.readline()

        #gets rid of the \n and the end
        line = line.strip()

        #makes the string into a list
        #elements in the list are all strings right now
        x = line.split(" ")
        #print(x)
        #print(type(x))
        nim_sum(x)
        print("DONE WITH ONE")


  # call function nim_sum() with inputs as given

  # call function find_heap() with inputs as given

  # print the results

'''
If the nim-sum of a given line of data is zero your program will output

Lose Game
'''


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
