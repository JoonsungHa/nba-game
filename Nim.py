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
def nim_sum (heaps):


    #this changes the elements in the list into integers
    for i in range(len(heaps)):
        into_int = int(heaps[i])
        heaps[i] = into_int

    #this returns binary
    for i in range(len(heaps)):
        into_binary = bin(heaps[i])
        heaps[i] = into_binary


    copy_heap = heaps


    #this lets me compare two heaps at a time and eventually find the nim_sum
    for i in range(len(heaps)-1):
        
        value = get_nim_sum(heaps[i],heaps[i+1])
        heaps[i+1] = value


        #get_nim_sum(heaps[i],heaps[i+1])
    print("VALUE",value)


    #now this is to get xor for each individual heap
    individual_nim_sum_lst = []
    for i in range(len(copy_heap)):
      individual_nim_sum = get_nim_sum(value,copy_heap[i])
      individual_nim_sum_lst.append(individual_nim_sum)


    print(individual_nim_sum_lst)



    #now we have to compare each heap with nim_sum value and if the individual nim_sum value is less than the heap then thats the one
    




    
    return 0
# placeholder for the actual return statement

#  Input: heaps is a list of integers giving the count in each heap
#         nim_sum is an integer 
#  Output: function returns two integers. The first integer is number
#          of counters that has to be removed. The second integer is
#          the number of the heap from which the counters are removed.
#          If the nim_sum is 0, then return 0, 0


def get_nim_sum(heap1, heap2):

  nim_sum_value_non_binary = int(heap1,2) ^ int(heap2,2)
  nim_sum_value_binary = '{0:b}'.format(nim_sum_value_non_binary)

  
  return nim_sum_value_binary





def find_heap (heaps, nim_sum):


    
  return 0, 0		# placeholder for the actual return statement






def main():
  # read input from input file nim.txt
    data = open("nim.txt","r")

    num_trials = data.readline()

    if num_trials == "":
      print("Lose Game")

    else:
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
          #print("DONE WITH ONE")


    # call function nim_sum() with inputs as given

    # call function find_heap() with inputs as given

    # print the results



# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()
