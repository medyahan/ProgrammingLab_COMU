# Matrisin determinantını bulma...

matris_1=[[1,2],[3,4]]
matris_2=[[1,2,3],[4,5,67],[7,8,9]]
print(matris_1,matris_2)
#print(matris_1[0]),len(matris)
#print(matris_1[0][0]),len(matris[0])

# 2*2lik matrisin determinantı

def det_from_2_by_2(m_1):
  s_1=m_1[0][0]*m_1[1][1]
  s_2=m_1[0][1]*m_1[1][0]
  s_3=s_1-s_2
  return s_3
print(det_from_2_by_2(matris_1))

def delete_row_from_matris(m1,m,n):
  result=[]
  size_1=(len(m1))
  size_2=(len(m1[0]))
  for i in range(size_1):
    if(i==m):
      continue
    row_1=[]
    for j in range(size_2):
      if(j==n):
        continue
      row_1.append(m1[i][j])
    result.append(row_1)
  return result
matris_1=[[1,2],[3,4]]
print(matris_2,delete_row_from_matris(matris_2,0,0))

# 3*3lük matrisin determinantı

def det_from_3_by_3(m_1):
  a1=m_1[0][0]
  a2=delete_row_from_matris(m_1,0,0)
  a3=det_from_2_by_2(a2)
  a4=a1*a3

  b1=m_1[0][1]
  b2=delete_row_from_matris(m_1,0,1)
  b3=det_from_2_by_2(b2)
  b4=b1*b3

  c1=m_1[0][2]
  c2=delete_row_from_matris(m_1,0,2)
  c3=det_from_2_by_2(c2)
  c4=c1*c3
  return a4-b4+c4
print(det_from_3_by_3(matris_2))

# 4*4lük matrisin determinantı

matris_4=[[13,2,3,4],[5,6,7,8],[9,10,31,42],[13,134,15,16]]
def det_from_4_by_4(m_1):
  a1=m_1[0][0]
  a2=delete_row_from_matris(m_1,0,0)
  a3=det_from_3_by_3(a2)
  a4=a1*a3

  b1=m_1[0][1]
  b2=delete_row_from_matris(m_1,0,1)
  b3=det_from_3_by_3(b2)
  b4=b1*b3

  c1=m_1[0][2]
  c2=delete_row_from_matris(m_1,0,2)
  c3=det_from_3_by_3(c2)
  c4=c1*c3

  d1=m_1[0][3]
  d2=delete_row_from_matris(m_1,0,3)
  d3=det_from_3_by_3(d2)
  d4=d1*d3
  return a4-b4+c4-d4
print(det_from_4_by_4(matris_4))
