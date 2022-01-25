import random
import numpy as np

def checkSquare(sq):
    if(len(np.unique(sq)) != 9):
        return False
    # All numbers unique
    # Now Need to check if everything sums

    rowSum = np.sum(sq, axis=1)
    colSum = np.sum(sq, axis=0)
    if(not all(el == rowSum[0] for el in rowSum)):
        return False
    if(not all(el == colSum[0] for el in colSum)):
        return False
    if(rowSum[0] != colSum[0]):
        return False

    #Sum of diagonals
    sumMain = sum(np.diagonal(sq))
    sumOff  = sum(np.fliplr(sq).diagonal())

    if(sumMain != sumOff):
        return False
    if(sumMain != rowSum[0]):
        return False

    return True

nums=  []

for i in range(2147395600):
    if(i % 100 == 0):
        print(i/2147395600 * 100)
    nums.append(i*i)

for _ in range(len(nums)):
    print("Checking")
    row1 = random.sample(nums, 3)
    row2 = random.sample(nums, 3)
    row3 = random.sample(nums, 3)
    if(checkSquare([row1, row2, row3])):
        print("Success!\nSquare was:")
        print([row1, row2, row3])
        exit(0)

print("None Found")