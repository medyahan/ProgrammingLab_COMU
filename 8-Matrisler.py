# Matrislerde İşlemler

def my_matris_addition(matris1,matris2):
  result=[]
  for row in range(len(matris1)):
    result.append([])
    for column in range(len(matris1[0])):
      result[row].append(matris1[row][column]+matris2[row][column])
      #print(column,end=" ")
      #print(matris1[row][column],end=" ")    
    print()
  return result

def my_matris_substraction(matris1,matris2):
  result=[]
  for row in range(len(matris1)):
    result.append([])
    for column in range(len(matris1[0])):
      result[row].append(matris1[row][column]-matris2[row][column])
      #print(column,end=" ")
      #print(matris1[row][column],end=" ")    
    print()
  return result

# Skaler Çarpım

def my_matris_scalar(matris1,alpha):
  result=[]
  for row in range(len(matris1)):
    result.append([])
    for column in range(len(matris1[0])):
      result[row].append(matris1[row][column]*alpha)
      #print(column,end=" ")
      #print(matris1[row][column],end=" ")    
    print()
  return result

# Satır * Sütun

def my_matris_scalar(matris1,alpha):
  result=[]
  for row in range(len(matris1)):
    result.append([])
    for column in range(len(matris1[0])):
      result[row].append(matris1[row][column]*alpha)
      #print(column,end=" ")
      #print(matris1[row][column],end=" ")    
    print()
  return result

def f_1(matris_1,i):
  return matris_1[i]

def f_2(matris_1,j):
  my_j_th_col=[]
  for row in matris_1:
     for indis in range(len(row)):
       if(indis==j):
          my_j_th_col.append(row[indis])
  return  my_j_th_col

def my_Vectors_Inner_Product(v,w):
  size=len(v)
  my_result=[]
  for i in range (size):
    my_result.append(0)
  for i in range(size):
    my_result[i]=v[i]*w[i]
  t=0
  for i in range(size):
    t=t+my_result[i]
  return t

def my_matris_multiply(m_1,m_2):
  result=[]
  for row in range(len(m_1)):
    result.append([])
    for column in range(len(m_2[0])):
      a=f_1(m_1,row)
      b=f_2(m_2,column)
      c=my_Vectors_Inner_Product(a,b)
      result[row].append(c)
      #print(column,end=" ")
      #print(matris1[row][column],end=" ")    
    print()
  return result

matris1=[[1,2,3],[4,5,6]]
matris2=[[3,5,9],[1,2,3]]
matris3=[[1,2],[3,4]]
matris4=[[5,6,7],[8,9,10]]
alpha=10
print(my_matris_addition(matris1,matris2))
print(my_matris_substraction(matris1,matris2))
print(my_matris_scalar(matris1,alpha))
print(my_matris_multiply(matris3,matris4))
