"""

    Rotate an array of n elements to the right by k steps.

    For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

    3 solutions:

    sol 1:
        create a new array
            range(0:k):
                copy new_arr[i] = arr[len(arr)-k+i]
            j=0
            range(k:):
                copy new_arr[i] = arr[j]
                j+=1
        complexity = O(n) for time and space
    sol 2:
        bubble rotate
    sol 3:
        reverse(0:k)
        revers(k:)
        reverse(0:)

"""
import random

class RotateArray:
    def __init__(self,k):
        self.arr = [random.randint(1,101) for _ in range(10)]
        self.k = k
        self.n = len(self.arr)

    def sol_w_new_arr(self):
        new_arr = []

        for i in range(self.k,self.n):
            new_arr.append(self.arr[i])

        for i in range(self.k):
            new_arr.append(self.arr[i])

        print("["+",".join((self.arr[0:self.k]))+"]["+",".join(self.arr[self.k:]))
        print(self.arr)
        print(new_arr)


ra = RotateArray(4)
ra.sol_w_new_arr()