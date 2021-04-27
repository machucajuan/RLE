# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 16:38:44 2021

@author: Juan
"""


def run_lenght_encoding(input):
    encoded_input = ""
    i = 0
   
    while (i <= len(input)-1):
        count = 1
        ch = input[i]
        j = i
        while (j < len(input)-1):
            if (input[j] == input[j+1]):
                count = count+1
                j = j+1
            else:
                break
        encoded_input=encoded_input+str(count)+ch
        i = j+1
    return encoded_input
  
#Provide different values for input and test your program
encoded_input=run_lenght_encoding("ABBBBCCCCCCCCAB")
print(encoded_input)

def encoding(input):
  result = ''
  i = 0
  length = len(input)
  while (i <= length - 1):
    count = 1
    char = input[i]
    j = i
    while (j < length - 1):
      if (input[j] == input[j+1]):
        count += 1
        j += 1
      else:
        break
    if (count == 1):
      result += char
    else:
      result += str(count) + char
    i = j + 1
  return result

