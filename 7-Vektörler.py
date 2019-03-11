# Vektörlerde İşlemler

def my_Vector_Addition(v,w):
  my_result = []
  for i in range (len(v)):
    my_result.append(0)
  for i in range(len(v)):
    my_result[i] = v[i]+w[i]
  return my_result

def my_Vector_Substraction(v,w):
  size = len(v)
  my_result = []
  for i in range (size):
    my_result.append(0)
  for i in range(size):
    my_result[i] = v[i]-w[i]
  return my_result

def my_Vector_Scalar_Product(v,alpha):
  size = len(v)
  my_result = []
  for i in range (size):
    my_result.append(0)
  for i in range(size):
    my_result[i] = v[i]*alpha
  return my_result

def my_Vectors_Inner_Product(v,w):
  size = len(v)
  my_result = []
  for i in range (size):
    my_result.append(0)
  for i in range(size):
    my_result[i] = v[i]*w[i]
  t=0
  for i in range(size):
    t = t + my_result[i]
  return t

a = [1,2,3]
b = [1,2,3]
alpha = 5
beta = 10
print(my_Vector_Scalar_Product(a,alpha))
print(my_Vector_Scalar_Product(b,beta))
x = my_Vector_Scalar_Product(a,alpha)
y = my_Vector_Scalar_Product(b,beta)
print(my_Vector_Addition(x,y))
print(my_Vector_Substraction(a,b))
print(x,y)
print(my_Vectors_Inner_Product(x,y))
