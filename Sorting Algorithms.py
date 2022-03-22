# -*- coding: utf-8 -*-
#INSERTION SORT 
f = open('PS4_test_dataset.txt', 'r')
data = f.readline()
unsorted = data.split(',')
unsorted = [int(x) for x in unsorted]
#reading in the data as a list

def insertion_sort(unsorted):
  sorted = []
  sorted.append(unsorted[0])
  unsorted.pop(0)
  #creating a second list to sort values in. inserting the first data value
  #and then popping that from the unsorted list
  for i in range(0, len(unsorted)):
      
      if unsorted[i] > sorted[i]:
        sorted.insert(i+1, unsorted[i])
     #if the unsorted values are greater than the sorted values, then
     #they are put in above the sorted value 

      elif unsorted[i] < sorted[i]:
        if len(sorted) == 1:
          sorted.insert(i, unsorted[i])
      #if the len of the sorted list is 1, and the unsorted value is less 
      #than what is in the sorted, then it is just put behind it 

        elif all (x > unsorted[i] for x in sorted):
          sorted.insert(0, unsorted[i])
      #on the other hand, if all the values in the list are greater than
      #the unsorted value, then it is put in the very back
      #this is to create anchor points, where there is a greatest and smallest
      #value so that the next nested loop can work
        
        else:
          for a in range(0, len(sorted)):
            if sorted[i-a] <= unsorted[i]:
              sorted.insert(i-a+1, unsorted[i])
              #this iterates over the sorted list until it finds 
              #where the unsorted value is less than another while still greater
              #than another
              break
          
            else: 
              pass

  return sorted 

insertion_sort(unsorted)
import csv 
with open('insertion.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(insertion_sort(unsorted))

#QUICKSORT
f = open('PS4_test_dataset.txt', 'r')
data = f.readline()
seq = data.split(',')
seq = [int(x) for x in seq]

def partition (seq):
  pivot = seq[0]
  seq.pop(0)
  low = []
  high = []
  for a in range(0, len(seq)): 
    if seq[a] < pivot:
      low.append(seq[a])
    elif seq[a] > pivot: 
      high.append(seq[a])
  return low, pivot, high

def quicksort(seq):
  if len(seq) <=1: return seq
  low, pivot, high = partition(seq)
  return quicksort(low) + [pivot] + quicksort(high)

quicksort(seq)
import csv 
with open('quicksort.csv', 'w') as f: 
    write = csv.writer(f) 
    write.writerow(insertion_sort(quicksort(seq)))

#------------------------------------------------------------------#

#MERGE SORT
f = open('PS4_test_dataset.txt', 'r')
data = f.readline()
unsorted_list = data.split(',')
unsorted_list = [int(x) for x in seq]

def merge_sort(unsorted_list):
    if len(unsorted_list) > 1:
        mid = len(unsorted_list) // 2
        left = unsorted_list[:mid]
        right = unsorted_list[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              unsorted_list[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                unsorted_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            unsorted_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_list[k]=right[j]
            j += 1
            k += 1
merge_sort (unsorted_list)
print(unsorted_list)


#------------------------------------------------------------------#


# SELECTION SORT
f = open('PS4_test_dataset.txt', 'r')
data = f.readline()
A = data.split(',')
A = [int(x) for x in A]

def selection_sort(A):
  #I need to find the minimum element
  for i in range(len(A)):
    #i'll set the default to i
    min_index = i

    #now, is i really the minimum
    for j in range(i + 1, len(A)):
      if A[min_index] > A[j]:
        min_index = j #A[j] is the new min

    #i now know the min value between
    #index i and the last index
    #swap values
    A[i], A[min_index] = A[min_index], A[i]
  return A

selection_sort(A)

#------------------------------------------------------------------#
f = open('PS4_test_dataset.txt', 'r')
data = f.readline()
B = data.split(',')
B = [int(x) for x in B]

#BUBBLE SORT
def bubble_sort(B):
  #input list of values to be sorted
  #output number of comparisonsand sorted list
  #sorts ascending values

  #variables to count the number of comparisons
  comparisons = 0
  num_swaps = 0

  #at most i'll have to make len(A) passS though the list and 
  for i in range(len(B)):
  
    #don't have to swap.  No swaps means I can end early
    swap = False

    #look at each adjacent pair to determine is A[j] and A[j+1]
    #need to swap positions in the sorted list
    for j in range(len(B) - i - 1):
      #i need to compare two values in the list A[j] and A[j+1]
      comparisons += 1
      if B[j] > B[j+1]:
        num_swaps += 1
        B[j], B[j+1] = B[j+1], B[j]
        swap = True
  
  #if I just went through the list and no elements swapped
    if swap == False: 
      return comparisons, num_swaps, B
  return comparisons, num_swaps,B

comparisons, swaps, a = bubble_sort(B)
print(str(comparisons) + ' comparisons have been made')
print(str(swaps) + ' swaps have been made')
print(a)
