import time, math, functools

def timer(func):

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.perf_counter()
        value = func(self, *args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time)*(10**6)
        self.timer_dict[run_time] = func.__name__
        return value
    return wrapper


class searching:

    def __init__(self, ip_list):
        self.ip_list = ip_list

    @timer
    def linear_search(self, x):
        t1 = time.time()
        for elem in self.ip_list:
            if elem == x:
                break
        # print("linear_search took \t\t\t\t"+str(round((time.time() - t1)*(10**6), 3))+" micro seconds"
        #                                                             "\t\t\tcomplexity O(n)")

    def binary_search_recursion_util(self, x, l, r, ip_list):

        if r >= l:
            mid = l + (r-l)//2
            if ip_list[mid] == x:
                return mid
            elif ip_list[mid] > x:
                return self.binary_search_recursion_util(x, l, mid-1, ip_list)
            else:
                return self.binary_search_recursion_util(x, mid+1, r, ip_list)

        else:
            return -1

    @timer
    def binary_search_recursion(self, x):
        idx = self.binary_search_recursion_util(x, 0, len(self.ip_list)-1, self.ip_list)
        # print("binary_search_recursion took \t" + str(round((time.time() - t1)*(10**6), 3)) + " micro seconds"
        #                                                                           "\t\t\tcomplexity O(log n)")

    def binary_search_iterative_util(self, x, l, r, ip_list):

        while l<=r:
            mid = l+(r-l) // 2

            if ip_list[mid] == x:
                return mid
            elif ip_list[mid] < x:
                l = mid+1
            else:
                r = mid-1
        return -1

    @timer
    def binary_search_iterative(self,x):
        idx = self.binary_search_iterative_util(x, 0, len(self.ip_list)-1, self.ip_list)
        # print("binary_search_iterative took \t" + str(round((time.time() - t1)*(10**6), 3)) + " micro seconds"
        #                                                                           "\t\t\tcomplexity O(log n)")

    @timer
    def jump_search(self, x):
        n = len(self.ip_list)
        step = math.sqrt(n)

        while self.ip_list[int(min(step, n) - 1)] < x:
            prev = step
            if step >= n:
                return -1
            step += step

        while self.ip_list[int(prev)] < x:
            prev += 1
            if prev == min(step, n):
                return -1
        if self.ip_list[int(prev)] != x:
            return -1

        # print("jump_search took \t\t\t\t"+str(round((time.time() - t1)*(10**6), 3))+ " micro seconds"
        #                                                            "\t\t\tcomplexity O(√n)")

    def interpolation_search_util(self, x, lo, hi):
        pos = lo + int(  ( (x - self.ip_list[lo]) * (hi - lo) ) / (self.ip_list[hi] - self.ip_list[lo])  )

        if self.ip_list[pos] == x:
            return pos
        elif self.ip_list[pos] < x:
            return self.interpolation_search_util( x, pos, hi)
        elif self.ip_list[pos] > x:
            return self.interpolation_search_util( x, lo, pos)
    @timer
    def interpolation_search(self, x):
        # t1 = time.time()
        lo, hi = 0, len(self.ip_list) - 1
        self.interpolation_search_util(x, lo, hi)
        # print("interpolation_search took \t\t" + str(round((time.time() - t1) * (10 ** 6),3)) + " micro seconds"
        #                                                                            "\t\t\tcomplexity O(log log n) ")

    def binary_search_iterative_fewer_comparison(self,x):
        t1 = time.time()
        l, r = 0, len(self.ip_list)
        while (r-l) > 1:
            m = l+int( (r-l)/2 )
            if self.ip_list[m] <= x:
                l = m
            else:
                r= m
        if self.ip_list[l] == x:
            print("b_s_it_fewer_comparison took \t" + str(round((time.time() - t1) * (10 ** 6),3)) + " micro seconds"
                                                                                          "\t\t\tcomplexity O(log n)")
        else:
            return -1

    def find_floor(self, x):
        if x < self.ip_list[0]:
            return -1
        t1 = time.time()
        l, r = 0, len(self.ip_list)
        while (r - l) > 1:
            m = l + int((r - l) / 2)
            if self.ip_list[m] <= x:
                l = m
            else:
                r = m
        if self.ip_list[l] <= x:
            # print("floor value : ",self.ip_list[l])
            return l
        else:
            return -1

    def find_ceil(self, x):
        l, r = 0, len(self.ip_list)
        if self.ip_list[r-1] < x :
            return -1
        while (r-l) > 1:
            m = l + int((r-l) / 2)
            if x <= self.ip_list[m]:
                r = m
            else:
                l = m
        if self.ip_list[r] >= x:
            # print("ciel value : ",self.ip_list[r])
            return r
        else:
            return -1

    def find_num_of_duplicates(self, x):
        l = self.find_floor(x)
        r = self.find_ceil(x)
        print(r - l + 1)

ip = []
for i in range(0,2000,2):
    ip.extend([i]*4)
# s = searching(ip)
# s.linear_search(1998)
# s.binary_search_recursion(1998)
# s.binary_search_iterative(1998)
# s.jump_search(1998)
# s.interpolation_search(1998)
# s.binary_search_iterative_fewer_comparison(1998)
"""
    Problem Statement: Given an array of N distinct integers, find floor value of input ‘key’. 
    Say, A = {-1, 2, 3, 5, 6, 8, 9, 10} and key = 7, we should return 6 as outcome.
"""
# s.find_floor(1999)
# s.find_ceil(17)
# s.find_num_of_duplicates(20)