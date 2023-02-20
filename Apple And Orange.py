#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
   
    count_Apples = 0
    count_Oranges= 0

    for i in range(len(apples)):
        if a+apples[i] >= s and a+apples[i] <= t:
            count_Apples +=1
            
    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <=t:
            count_Oranges +=1
            
    print(count_Apples)
    print(count_Oranges)
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)