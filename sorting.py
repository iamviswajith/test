import functools
import pprint

from searching import timer
import random


def shuffle(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        random.shuffle(self.ip_list)
        value = func(self, *args, **kwargs)
        return value
    return wrapper


class sorting_hw:
    def __init__(self,ip_list):
        self.ip_list = ip_list
        self.n = len(self.ip_list)
        self.timer_dict = {}

    def __del__(self):
        for t in sorted(self.timer_dict):
            print(f"Finished {self.timer_dict[t]!r} in {t:.3f} µ secs")

    @timer
    @shuffle
    def bubble_sort(self):
        for i in range(self.n):
            for j in range(self.n-i-1):
                if self.ip_list[j+1] < self.ip_list[j]:
                    self.ip_list[j], self.ip_list[j+1] = self.ip_list[j+1], self.ip_list[j]

    @timer
    @shuffle
    def recursive_bubble_sort(self):
        self.recursive_bubble_sort_util(self.n)

    def recursive_bubble_sort_util(self, n):
        if n == 0:
            return
        self.recursive_bubble_sort_util( n-1 )

        for i in range(self.n - n):
            if self.ip_list[i] > self.ip_list[i+1]:
                self.ip_list[i], self.ip_list[i+1] = self.ip_list[i+1], self.ip_list[i]

    @timer
    @shuffle
    def selection_sort(self):
        for i in range(self.n):
            min_indx = i
            for j in range(i,self.n):
                if self.ip_list[j] < self.ip_list[min_indx]:
                    min_indx = j
            self.ip_list[i], self.ip_list[min_indx] = self.ip_list[min_indx], self.ip_list[i]

    @timer
    @shuffle
    def insertion_sort(self):
        for i in range(1, self.n):
            card = self.ip_list[i]
            j = i-1

            while j >= 0 and card < self.ip_list[j]:
                self.ip_list[j+1] = self.ip_list[j]
                j -= 1
            self.ip_list[j+1] = card

    @timer
    @shuffle
    def recursive_insertion_sort(self):
        self.recursive_insertion_sort_util(self.n-1)

    def recursive_insertion_sort_util(self, i):
        if i==0:
            return
        self.recursive_insertion_sort_util(i-1)
        card = self.ip_list[i]
        j = i-1
        while j>=0 and card < self.ip_list[j]:
            self.ip_list[j+1] = self.ip_list[j]
            j-=1
        self.ip_list[j+1] = card

    @timer
    @shuffle
    def merge_sort(self):
        self.merge_sort_util(self.ip_list)

    def merge_sort_util(self, arr):
        if len(arr) > 1:
            m = len(arr) // 2
            l = arr[:m]
            r = arr[m:]
            self.merge_sort_util(l)
            self.merge_sort_util(r)
            i = j = k = 0
            while i < len(l) and j < len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i+=1
                elif l[i] > r[j]:
                    arr[k] = r[j]
                    j+=1
                k+=1
            while i < len(l):
                arr[k] = l[i]
                k+=1
                i+=1
            while j < len(r):
                arr[k] = r[j]
                k+=1
                j+=1

    # @timer
    # @shuffle
    # def iterative_merge_sort(self):

    # Iterative Merge sort (Bottom Up)

    # Iterative mergesort function to
    # sort arr[0...n-1]
    @timer
    @shuffle
    def iterative_merge_sort(self):
        a = self.ip_list
        current_size = 1

        # Outer loop for traversing Each
        # sub array of current_size
        while current_size < len(a) - 1:

            left = 0
            # Inner loop for merge call
            # in a sub array
            # Each complete Iteration sorts
            # the iterating sub array
            while left < len(a) - 1:
                # mid index = left index of
                # sub array + current sub
                # array size - 1
                mid = left + current_size - 1

                # (False result,True result)
                # [Condition] Can use current_size
                # if 2 * current_size < len(a)-1
                # else len(a)-1
                right = ((2 * current_size + left - 1,
                          len(a) - 1)[2 * current_size
                                      + left - 1 > len(a) - 1])

                # Merge call for each sub array
                self.merge(a, left, mid, right)
                left = left + current_size * 2

            # Increasing sub array size by
            # multiple of 2
            current_size = 2 * current_size

            # Merge Function

    def merge(self,a, l, m, r):
        n1 = m - l + 1
        n2 = r - m
        L = [0] * n1
        R = [0] * n2
        for i in range(0, n1):
            L[i] = a[l + i]
        for i in range(0, n2):
            R[i] = a[m + i + 1]

        i, j, k = 0, 0, l
        while i < n1 and j < n2:
            if L[i] > R[j]:
                a[k] = R[j]
                j += 1
            else:
                a[k] = L[i]
                i += 1
            k += 1

        while i < n1:
            a[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            a[k] = R[j]
            j += 1
            k += 1

    @timer
    @shuffle
    def quick_sort(self):
        self.quick_sort_util( 0, self.n-1)

    def quick_sort_util(self, low, high):
        if low < high:
            pi = self.partition(low, high)

            self.quick_sort_util( low, pi-1)
            self.quick_sort_util( pi+1,high)

    def partition(self, low, high):
        pivot = self.ip_list[high]
        i = low-1
        for j in range(low, high):
            if self.ip_list[j] < pivot:
                i += 1
                self.ip_list[i], self.ip_list[j] = self.ip_list[j], self.ip_list[i]
        self.ip_list[i+1], self.ip_list[high] = self.ip_list[high], self.ip_list[i+1]
        return i+1

    @timer
    @shuffle
    def heap_sort(self):
        for i in range(self.n, -1, -1):
            self.heapify(self.n, i)
        for i in range(self.n-1, -1, -1):
            self.ip_list[i], self.ip_list[0] = self.ip_list[0], self.ip_list[i]
            self.heapify(i, 0)

    def heapify(self, n, i):
        l = 2*i + 1
        r = 2*i + 2
        largest = i
        if l < n and self.ip_list[l] > self.ip_list[i]:
            largest = l
        if r < n and self.ip_list[r] > self.ip_list[largest]:
            largest = r

        if largest != i:
            self.ip_list[i], self.ip_list[largest] = self.ip_list[largest], self.ip_list[i]
            self.heapify(n, largest)


shw = sorting_hw([i for i in range(10)])
shw.bubble_sort()
# shw.recursive_bubble_sort()
shw.selection_sort()
shw.insertion_sort()
# shw.recursive_insertion_sort()
shw.merge_sort()
# this is wrong in geeks for geeks
# shw.iterative_merge_sort()
shw.quick_sort()
shw.heap_sort()










#
#
#
# class sorting:
#     def __init__(self, ip_list):
#         self.ip_list = ip_list
#         self.n = len(self.ip_list)
#         self.timer_dict = {}
#
#     def __del__(self):
#         for t in sorted(self.timer_dict):
#             print(f"Finished {self.timer_dict[t]!r} in {t:.3f} µ secs")
#
#     @shuffle
#     @timer
#     def selection_sort(self):
#         # print(self.ip_list)
#         for i in range(self.n):
#             min_indx = i
#             for j in range(i+1, self.n):
#                 if self.ip_list[j] < self.ip_list[min_indx]:
#                     min_indx = j
#
#             self.ip_list[i], self.ip_list[min_indx] = self.ip_list[min_indx], self.ip_list[i]
#
#         # print(self.ip_list)
#
#     @shuffle
#     @timer
#     def bubble_sort(self):
#         # print(self.ip_list)
#         for i in range(self.n):
#             for j in range(self.n - i - 1):
#                 if self.ip_list[j] > self.ip_list[j+1]:
#                     self.ip_list[j], self.ip_list[j+1] = self.ip_list[j+1], self.ip_list[j]
#         # print(self.ip_list)
#
#     @shuffle
#     @timer
#     def recursive_bubble_sort(self):
#         self.recursive_bubble_sort_util(self.n)
#
#     def recursive_bubble_sort_util(self, i):
#         if i==0:
#             return
#         self.recursive_bubble_sort_util(i-1)
#         j = self.n - i - 1
#
#         while j < self.n - 1:
#             if self.ip_list[j] > self.ip_list[j+1]:
#                 self.ip_list[j], self.ip_list[j+1] = self.ip_list[j+1], self.ip_list[j]
#             j+=1
#
#     @shuffle
#     @timer
#     def insertion_sort(self):
#         for i in range(1, self.n):
#             card = self.ip_list[i]
#             j = i-1
#             while j >= 0 and card < self.ip_list[j]:
#                 self.ip_list[j+1] = self.ip_list[j]
#                 j-=1
#             self.ip_list[j+1] = card
#
#     def insertion_sort_recursive_util(self, arr, n):
#         # base case
#         if n <= 1:
#             return
#
#         # Sort first n-1 elements
#         self.insertion_sort_recursive_util(arr, n - 1)
#         '''Insert last element at its correct position
#             in sorted array.'''
#         last = arr[n - 1]
#         j = n - 2
#
#         # Move elements of arr[0..i-1], that are
#         # greater than key, to one position ahead
#         # of their current position
#         while (j >= 0 and arr[j] > last):
#             arr[j + 1] = arr[j]
#             j = j - 1
#
#         arr[j + 1] = last
#
#     @shuffle
#     @timer
#     def insertion_sort_recursive(self):
#         self.insertion_sort_recursive_util(self.ip_list, self.n)
#
#     def merge_sort_util(self,arr):
#         """
#
#         :type arr: object
#         """
#         if len(arr)>1:
#             m = len(arr)//2
#             llist = arr[:m]
#             rlist = arr[m:]
#             self.merge_sort_util(llist)
#             self.merge_sort_util(rlist)
#
#             i = j = k = 0
#             while i<len(llist) and j<len(rlist):
#                 if llist[i] <= rlist[j]:
#                     arr[k] = llist[i]
#                     i+=1
#                 else:
#                     arr[k] = rlist[j]
#                     j+=1
#                 k+=1
#
#             while i< len(llist):
#                 arr[k] = llist[i]
#                 k+=1
#                 i+=1
#
#             while j< len(rlist):
#                 arr[k] = rlist[j]
#                 k+=1
#                 j+=1
#             self.ip_list = arr
#
#     @shuffle
#     @timer
#     def merge_sort(self):
#         # print(self.ip_list)
#         self.merge_sort_util(self.ip_list)
#         # print(self.ip_list)
#
#     # @shuffle
#     # @timer
#     # def merge_sort_iterative(self):
#     #     i = j = k = 0
#     #     while k< self.n:
#     #         if
#
#     # @shuffle
#     # @timer
#     def heap_sort(self):
#         print(self.ip_list)
#         for i in range((self.n//2)-1, -1, -1):
#             self.heapify(i)
#         print(self.ip_list)
#
#         for i in range(self.n-1, -1, -1):
#             temp = self.ip_list[0]
#             self.ip_list[0] = self.ip_list[i]
#             self.ip_list[i] = temp
#             heapify
#
#         print(self.ip_list)
#
#
#     def heapify(self, i):
#         left = (i*2)+1
#         right = (i*2) + 2
#         small = i
#         if left < self.n and self.ip_list[left] <= self.ip_list[small]:
#             small = left
#         if right < self.n and self.ip_list[right] <= self.ip_list[small]:
#             small = right
#         if i != small:
#             temp = self.ip_list[small]
#             self.ip_list[small] = self.ip_list[i]
#             self.ip_list[i] = temp
#             # self.ip_list[i], self.ip_list[small] = self.ip_list[small], self.ip_list[i]
#             # self.heapify(small)
#
#
#     def extract(self):
#         min = self.ip_list[0]
#         self.ip_list[0] = self.ip_list[self.n-1]
#         self.n -= 1
#         self.heapify(0)
#         return min
#
#
#
#
# x = [i for i in range(0,10)]
# random.shuffle(x)
# s = sorting(x)
#
#
# # s.selection_sort()
# # s.bubble_sort()
# # s.recursive_bubble_sort()
# # s.insertion_sort()
# # s.insertion_sort_recursive()
# # s.merge_sort()
# # s.merge_sort_iterative()
# # s.heap_sort()
# # pprint.pprint(s.timer_dict)