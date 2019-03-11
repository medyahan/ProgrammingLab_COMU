# Diziye random şekilde değer atama...

import random
def generate_an_array(n):
    my_array=[]
    for  i in range(n):
        s = random.randint(0,100)
        my_array.append(s)
    return my_array
my_arr_1 = generate_an_array(10)
print(my_arr_1)

# Dizide arama yapma...

def my_search_c(array_2, item):
  found = False
  indis = -1
  step = 0
  for i in range(len(array_2)):
    step += 1
    #if(i == item):
      #found = True
    if (array_2[i] == item):
      found = True
      indis = i
      break
  return found,indis,step
  
# Bubble Sort

for i in range (len(my_arr_1)-1, 0, -1):
  for j in range(i):
    if(my_arr_1[j] > my_arr_1[j+1]):
      t=my_arr_1[j]
      my_arr_1[j] = my_arr_1[j+1]
      my_arr_1[j+1] = t

print(my_arr_1)
print(my_search_c(my_arr_1,68))
