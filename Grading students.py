import math
import os
import random
import re
import sys

def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            difference = 5 - grade % 5
            if difference < 3:
                grade += difference
        rounded_grades.append(grade)
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()