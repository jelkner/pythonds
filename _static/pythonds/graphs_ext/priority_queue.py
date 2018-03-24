# Bradley N. Miller, David L. Ranum, Jeffrey Elkner
# Introduction to Data Structures and Algorithms in Python
# Copyright 2018
#
# This implementation of binary heap takes key value pairs, we will assume
# that the keys are all comparable


class PriorityQueue:
    def __init__(self):
        self.heap = [(0, 0)]
        self.size = 0

    def build_heap(self, alist):
        self.size = len(alist)
        self.heap = [(0, 0)]
        for i in alist:
            self.heap.append(i)
        i = len(alist) // 2
        while (i > 0):
            self.perc_down(i)
            i = i - 1

    def perc_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.heap[i][0] > self.heap[mc][0]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def min_child(self, i):
        if i * 2 > self.size:
            return -1
        else:
            if i * 2 + 1 > self.size:
                return i * 2
            else:
                if self.heap[i*2][0] < self.heap[i*2+1][0]:
                    return i * 2
                else:
                    return i * 2 + 1

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap[i][0] < self.heap[i//2][0]:
                self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i //= 2

    def add(self, k):
        self.heap.append(k)
        self.size = self.size + 1
        self.perc_up(self.size)

    def del_min(self):
        retval = self.heap[1][1]
        self.heap[1] = self.heap[self.size]
        self.size = self.size - 1
        self.heap.pop()
        self.perc_down(1)
        return retval

    def is_empty(self):
        return self.size == 0

    def decrease_key(self, val, amt):
        # this is a little wierd, but we need to find the heap thing to
        # decrease by looking at its value
        done = False
        i = 1
        my_key = 0
        while not done and i <= self.size:
            if self.heap[i][1] == val:
                done = True
                my_key = i
            else:
                i = i + 1
        if my_key > 0:
            self.heap[my_key] = (amt, self.heap[my_key][1])
            self.perc_up(my_key)

    def __contains__(self, vtx):
        for pair in self.heap:
            if pair[1] == vtx:
                return True
        return False
