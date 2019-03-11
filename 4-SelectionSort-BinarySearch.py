# Selection Sort

def selection_sort(array):
  min_index = 0
  print(array)
  for i in range(len(array)):
    min_index = i
    for j in range(i,len(array)-1):
      if(array[min_index] > array[j+1]):
        min_index = j+1
    temp = array[min_index]
    array[min_index] = array[i]
    array[i] = temp
  return array

# Binary Search

def binary_search(array,search):
  first = 0
  last = len(array)-1
  found = False
  s = 0
  while(first <= last and not found):
    mid = (first + last)//2
    print("first - last : ",first,last)
    s += 1
    if(array[mid] == search):
      found = True
    else:
      if(array[mid] > search):
        last = mid-1
      else:
        first = mid+1
  return found,mid,s
array = [21,12,13,44,25,2,7,16,14]
print(selection_sort(array))
print(binary_search(array,25))
