'''
This is a quick sort program with last element as pivot
'''
import random
import time

def partition(arr,start_index, end_index):
  pivot=arr[end_index] #setting last element as pivot
  i=start_index-1 #index of lowest element
  for j in range(start_index,end_index+1):
    if(arr[j]<pivot):
      i+=1
      arr[j],arr[i]=arr[i],arr[j]   #swapping if the element is less than the pivot element
  arr.insert(i+1,pivot) #shifting the pivot to its proper position
  arr.pop(j+1)
  return arr.index(pivot)

def quicksort(arr, start_index, end_index):
  if start_index< end_index:
    p=partition(arr,start_index,end_index)

    quicksort(arr,start_index,p-1)
    quicksort(arr,p+1,end_index)
 

for i in range(10):
  array = []
  rand= random.randrange(10000)
  for number in range(rand):
      array.append(random.randrange(0, 10000000))
  print(rand)
  n=len(array)
  start_time = time.time() 
  quicksort(array,0,n-1)    
  print((time.time() - start_time))


 
 

