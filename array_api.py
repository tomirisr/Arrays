#!/usr/bin/env python3
import array as arr

class Array(object):
    '''
    An array implementation that holds arbitrary objects.
    '''

    def __init__(self, initial_size=10, chunk_size=5):
        '''Creates an array with an intial size.'''
        self.data = alloc(initial_size)
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire allocated space, including unused spots.'''
        print('{} of {} >>> {}'.format(self.size, len(self.data), ', '.join([ str(item) for item in self.data ])))


    def _check_bounds(self, index):
        '''Ensures the index is within the bounds of the array: 0 <= index <= size.'''
        if 0 <= int(index)+1 <= self.size:
            return True
        else:
            return False

    def _check_increase(self):
        '''
        Checks whether the array is full and needs to increase by chunk size
        in preparation for adding an item to the array.
        '''
        if self.size >= len(self.data):
            dest = alloc(self.size + 5)
            self.data = memcpy(dest, self.data, self.size)


    def _check_decrease(self):
        '''
        Checks whether the array has too many empty spots and can be decreased by chunk size.
        If a decrease is warranted, it should be done by allocating a new array and copying the
        data into it (don't allocate multiple arrays if multiple chunks need decreasing).
        '''
        if len(self.data) - self.size >= 5:
            dest = alloc(len(self.data) - 5)
            self.data = memcpy(dest, self.data, self.size)


    def add(self, item):
        '''Adds an item to the end of the array, allocating a larger array if necessary.'''
        self._check_increase()
        self.data[self.size] = item
        self.size += 1
        return self.data

    def insert(self, index, item):
        '''Inserts an item at the given index, shifting remaining items right and allocating a larger array if necessary.'''
        if self._check_bounds(index):
            self._check_increase()
            for i in range(self.size, int(index), -1): 
                self.data[i] = self.data[i-1]
            self.set(index, item)
            self.size+=1
        else:
           print(f'Error: {index} is not within the bounds of the current array.') 

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            self.data[int(index)] = item
        else:
            print(f'Error: {index} is not within the bounds of the current array.')

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            print(self.data[int(index)])
        else:
            print(f'Error: {index} is not within the bounds of the current array.')

    def delete(self, index):
        '''Deletes the item at the given index, decreasing the allocated memory if needed.  Throws an exception if the index is not within the bounds of the array.'''
        if self._check_bounds(index):
            for i in range(int(index), self.size-1): 
                self.data[i] = self.data[i+1]
            self.data[self.size-1] = None
            self.size-=1
        else:
           print(f'Error: {index} is not within the bounds of the current array.') 
        self._check_decrease()

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if self._check_bounds(index1):
            if self._check_bounds(index2):
                a = self.data[int(index1)]
                b = self.data[int(index2)]
                self.data[int(index1)] = b
                self.data[int(index2)] = a
            else:
               print(f'Error: {index2} is not within the bounds of the current array.') 
        else:
           print(f'Error: {index1} is not within the bounds of the current array.') 


###################################################
###   Utilities

def alloc(size):
    '''
    Allocates array space in memory. This is similar to C's alloc function.
    '''
    data = []
    for i in range(size):
        data.append(None)
    return data


def memcpy(dest, source, size):
    '''
    Copies items from one array to another.  This is similar to C's memcpy function.
    '''
    for i in range(0, size): 
       dest[i] = source[i]
    return dest
