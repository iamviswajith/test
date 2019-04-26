import functools

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
        self.recursive_bubble_sort_util()

    def recursive_bubble_sort_util(self):
        for j in range(self.n):
            try:
                if self.ip_list[j] > self.ip_list[j + 1]:
                    self.ip_list[j], self.ip_list[j + 1] = self.ip_list[j + 1], self.ip_list[j]
                    self.recursive_bubble_sort_util()
            except IndexError:
                pass
        return

    @shuffle
    @timer
    def insertion_sort(self):
        for i, num in range(1, self.n):
            j = 0
            while j <= i-1:
                if self.ip_list[i] < self.ip_list[i]:


x = [i for i in range(0,30)]
random.shuffle(x)
s = sorting(x)
s.selection_sort()
s.bubble_sort()
s.recursive_bubble_sort()
s.insertion_sort()