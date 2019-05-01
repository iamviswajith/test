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


class sorting:
    def __init__(self, ip_list):
        self.ip_list = ip_list
        self.n = len(self.ip_list)
        self.timer_dict = {}

    def __del__(self):
        for t in sorted(self.timer_dict):
            print(f"Finished {self.timer_dict[t]!r} in {t:.3f} µ secs")

    @shuffle
    @timer
    def selection_sort(self):
        # print(self.ip_list)
        for i in range(self.n):
            min_indx = i
            for j in range(i+1, self.n):
                if self.ip_list[j] < self.ip_list[min_indx]:
                    min_indx = j

            self.ip_list[i], self.ip_list[min_indx] = self.ip_list[min_indx], self.ip_list[i]

        # print(self.ip_list)

    @shuffle
    @timer
    def bubble_sort(self):
        # print(self.ip_list)
        for i in range(self.n):
            for j in range(self.n - i - 1):
                if self.ip_list[j] > self.ip_list[j+1]:
                    self.ip_list[j], self.ip_list[j+1] = self.ip_list[j+1], self.ip_list[j]
        # print(self.ip_list)

    @shuffle
    @timer
    def recursive_bubble_sort(self):
        self.recursive_bubble_sort_util(self.n)

    def recursive_bubble_sort_util(self, i):
        if i==0:
            return
        self.recursive_bubble_sort_util(i-1)
        j = self.n - i - 1

        while j < self.n - 1:
            if self.ip_list[j] > self.ip_list[j+1]:
                self.ip_list[j], self.ip_list[j+1] = self.ip_list[j+1], self.ip_list[j]
            j+=1

    @shuffle
    @timer
    def insertion_sort(self):
        for i in range(1, self.n):
            card = self.ip_list[i]
            j = i-1
            while j >= 0 and card < self.ip_list[j]:
                self.ip_list[j+1] = self.ip_list[j]
                j-=1
            self.ip_list[j+1] = card

    def insertion_sort_recursive_util(self, arr, n):
        # base case
        if n <= 1:
            return

        # Sort first n-1 elements
        self.insertion_sort_recursive_util(arr, n - 1)
        '''Insert last element at its correct position 
            in sorted array.'''
        last = arr[n - 1]
        j = n - 2

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while (j >= 0 and arr[j] > last):
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = last

    @shuffle
    @timer
    def insertion_sort_recursive(self):
        self.insertion_sort_recursive_util(self.ip_list, self.n)

    def merge_sort_util(self,arr):
        """

        :type arr: object
        """
        if len(arr)>1:
            m = len(arr)//2
            llist = arr[:m]
            rlist = arr[m:]
            self.merge_sort_util(llist)
            self.merge_sort_util(rlist)

            i = j = k = 0
            while i<len(llist) and j<len(rlist):
                if llist[i] <= rlist[j]:
                    arr[k] = llist[i]
                    i+=1
                else:
                    arr[k] = rlist[j]
                    j+=1
                k+=1

            while i< len(llist):
                arr[k] = llist[i]
                k+=1
                i+=1

            while j< len(rlist):
                arr[k] = rlist[j]
                k+=1
                j+=1
            self.ip_list = arr
            
    @shuffle
    @timer
    def merge_sort(self):
        # print(self.ip_list)
        self.merge_sort_util(self.ip_list)
        # print(self.ip_list)

    # @shuffle
    # @timer
    # def merge_sort_iterative(self):
    #     i = j = k = 0
    #     while k< self.n:
    #         if

    # @shuffle
    # @timer
    def heap_sort(self):
        print(self.ip_list)
        for i in range((self.n//2)-1, -1, -1):
            self.heapify(i)
        print(self.ip_list)

        for i in range(self.n-1, -1, -1):
            temp = self.ip_list[0]
            self.ip_list[0] = self.ip_list[i]
            self.ip_list[i] = temp
            heapify

        print(self.ip_list)


    def heapify(self, i):
        left = (i*2)+1
        right = (i*2) + 2
        small = i
        if left < self.n and self.ip_list[left] <= self.ip_list[small]:
            small = left
        if right < self.n and self.ip_list[right] <= self.ip_list[small]:
            small = right
        if i != small:
            temp = self.ip_list[small]
            self.ip_list[small] = self.ip_list[i]
            self.ip_list[i] = temp
            # self.ip_list[i], self.ip_list[small] = self.ip_list[small], self.ip_list[i]
            # self.heapify(small)


    def extract(self):
        min = self.ip_list[0]
        self.ip_list[0] = self.ip_list[self.n-1]
        self.n -= 1
        self.heapify(0)
        return min




x = [i for i in range(0,10)]
random.shuffle(x)
s = sorting(x)


# s.selection_sort()
# s.bubble_sort()
# s.recursive_bubble_sort()
# s.insertion_sort()
# s.insertion_sort_recursive()
# s.merge_sort()
# s.merge_sort_iterative()
s.heap_sort()
# pprint.pprint(s.timer_dict)