#https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    for i in range(0, n):
        row = ''
        for j in range(0, n):
            row += '#' if j>=n-i-1 else ' '  
        
        print(row)




if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
