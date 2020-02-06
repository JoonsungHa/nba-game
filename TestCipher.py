#  File: TestCipher.py

#  Description:

#  Student's Name: Joonsung Ha

#  Student's UT EID: jh69256
 
#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E 

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode ( strng, key ):


    lst = []
    for row in range(3):
        re = []
        for col in range(len(strng)):
            re.append("-")
        lst.append(re)
        

    row_index = 0
    col_index = 0
    length = len(strng)
    
    while strng != "":
        for i in range(key):
            if col_index < length:
                lst[row_index][col_index] = strng[0]
                strng = strng[1:]
                row_index += 1
                col_index += 1
            else:
                break

        if col_index < length:
            row_index -= 1
            col_index -= 1
        else:
            break

        for b in range(key-2):
            if col_index < length:
                row_index -= 1
                col_index += 1
                lst[row_index][col_index] = strng[0]
                strng = strng[1:]
            else:
                break
        if col_index < length:
            row_index = 0
            col_index += 1
        else:
            break

    return lst



#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode ( strng, key ):

  #I have to recreate the list




  return ""	

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string ( strng ):
  return ""	# placeholder for the actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def encode_character (p, s):
  return ""	# placeholder for actual return statement

#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character decoded using the 
#          Vigenere algorithm. You may not use a 2-D list 
def decode_character (p, s):
  return ""	# placeholder for actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode ( strng, phrase ):
  return ""	# placeholder for the actual return statement

#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode ( strng, phrase ):
  return ""	# placeholder for the actual return statement

def main():
  # prompt the user to enter plain text
  plain_text = input("Enter Plain Text to be Encoded: ")

  # prompt the user to enter the key
  key = input("Enter Key: ")

  # encrypt and print the plain text using rail fence cipher


  # prompt the user to enter encoded text
   
  # prompt the user to enter the key

  # decrypt and print the encoded text using rail fence cipher

  # prompt the user to enter plain text

  # prompt the user to enter pass phrase

  # encrypt and print the plain text using Vigenere cipher

  # prompt the user to enter encoded text

  # prompt the user to enter pass phrase

  # decrypt and print the encoded text using Vigenere cipher

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()

