#!/usr/bin/python3
# -*- coding: utf-8 -*


def max_heapify(A, node_index):
    l = (node_index+1) * 2 - 1
    r = (node_index+1) * 2

    largest = 0

    if (l<len(A)) and (A[l]>A[node_index]):
        largest = l
    else:
        largest = node_index
    
    if (r<len(A)) and (A[r]>A[largest]):
        largest = r
    
    if largest != node_index:
        t = A[node_index]
        A[node_index] = A[largest]
        A[largest] = t

        max_heapify(A, largest)
    else:
        return


def build_max_heap(A):
    mid_index = int((len(A)-1)/2)

    for i in range(mid_index, -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    original_len = len(A)-1
    temp_list = []
    build_max_heap(A)
    for total_len in range(original_len, -1, -1):
        max_heapify(A,0)
        t = A[0]
        A[0] = A[len(A)-1]
        temp_list.append(t)
        A.pop()
    
    return temp_list
 
    


A = [16,4,10,14,7,9,3,2,8,1]

print("original list is " + str(A))
max_heapify(A,1)
print("changes list is " + str(A))
print("--------------------------")
A = [4,1,3,2,16,9,10,14,8,7]
print("original list is " + str(A))
build_max_heap(A)
print("changes list is " + str(A))
print("--------------------------")
A = [4,1,3,2,16,9,10,14,8,7]
print("original list is " + str(A))
A = heap_sort(A)
print("changes list is " + str(A))