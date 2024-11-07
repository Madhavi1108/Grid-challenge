#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def gridChallenge(grid):
    correct_list = []
    for row in grid:
        sorted_row = ''.join(sorted(row))  
        correct_list.append(sorted_row)


    for j in range(len(correct_list[0])):  
        for i in range(len(correct_list) - 1):
            if correct_list[i][j] > correct_list[i + 1][j]: 
                return 'NO'

    return 'YES'




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
