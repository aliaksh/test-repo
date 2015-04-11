def IMPORT_TEXTFILE_INTO_GRAPH1(textfile):
  count = [int(i) for i in textfile.readline().split()]
  print ('count\t=', count)
  G = {}
  for i in range(0, count[1]):
    arr = [int(j) for j in textfile.readline().split()]
    if arr[0] not in G:
      G[arr[0]] = [[arr[1], arr[2]]]
    else:
      G[arr[0]].append([arr[1], arr[2]])
    
  return G
#-----------------------------------------------------------------------------------
def MST_PRIM(G,r):
  for i in G:
    key.append(float('inf'))
    #pi.append(None)
  key[r-1] = 0
  #print ('key\t\t=', key)
  #print ('pi\t\t=', pi)
  Q = []
  for i in G:
    Q.append(i)

  dMin = []
  DMin = []
  dMin.append([r,0])
  
  #for k in range(1,7):
  while len(Q) > 0:
    #print ('Q\t\t=', Q)    
    u, dMin, DMin = EXTRACT_MIN(Q,dMin,DMin)
    #print ('dMin\t=', dMin)
    if dMin[0][0] not in pi:
      pi.append(dMin[0][0])
    for i in DMin:#G[dMin[0][0]]:
      #print ('i\t\t=', i)
      if i[0] in Q and i[1] < key[i[0]-1]:# and i[0] == DMin[0][0]:
        #print ('i\t\t', i[0])
        #pi[i[0]-1] = u
        
        key[i[0]-1] = i[1]
    #print ('u\t\t=', u)
    dMin.append(DMin.pop(0))
    dMin.pop(0)
    #print ('dMin\t=', dMin)
    #print ('DMin\t=', DMin)
    #print ('Q\t\t=', Q)
  print ('key\t\t=', key)
  print ('pi\t\t=', pi)
  return key
   
#-----------------------------------------------------------------------------------
def EXTRACT_MIN(Q,dMin,DMin):  
  #if len(dMin) == 1:
    #print ('dMin\t=', dMin[0])
  for i in G[dMin[0][0]]:
    if i[0] in Q:
      #print ('i\t\t', i)
      DMin.append(i)
  '''
  if len(dMin) > 1:
    dMin = sorted(dMin, key=lambda x: x[1])
    for i in G[dMin[0][0]]:
      if i[0] in Q:
        DMin.append(i)
  '''
  
  DMin = sorted(DMin, key=lambda x: x[1])
  #print ('dMin\t=', dMin)
  #print ('DMin\t=', DMin)
  #G[r].remove(arr[0])
  u = DMin[0][0]
  #print ('u\t\t=', u)
  #dMin.append(DMin.pop(0))
  #if dMin[0][0] in Q:
  #print ('Q\t\t=', Q)
  if dMin[0][0] in Q:
    Q.remove(dMin[0][0])
  #else:
    #print ('Skip')
  #  DMin.pop(0)
  #print ('-----------------')
  #print ('dMin\t=', dMin)
  #print ('DMin\t=', DMin)
  #print ('Q\t\t=', Q)
  return u, dMin, DMin
#---------------------------------------------------------------------------------
def IMPORT_TEXTFILE_INTO_GRAPH2(textfile):
  count = int(textfile.readline())
  #print ('count\t=', count)
  G = []
  for i in range(0, count):
    G.append([float(j) for j in textfile.readline().split()])
  #print ('G\t\t=', G)
  nG = CONVERT(G)

  return nG
#---------------------------------------------------------------------------------
def CONVERT(G):
  nG = {}
  for i in range(0, len(G)):
    nG[i+1] = []
 
  for i in range(0, len(G)):
    for j in range(i+1, len(G)):
      nG[i+1].append([j+1, round(m.sqrt(pow(G[i][0] - G[j][0],2)+pow(G[i][1] - G[j][1],2)), 5)])
      nG[j+1].append([i+1, round(m.sqrt(pow(G[i][0] - G[j][0],2)+pow(G[i][1] - G[j][1],2)), 5)])
 
  print ('len(nG)\t=', len(nG))
  return nG
#---------------------------------------------------------------------------------
def PRINT_G(G):
  for i in G:
    print (str(i)+'\t'+str(G[i]))

import math as m
'''
textfile = open('testP.txt', 'r')
G = IMPORT_TEXTFILE_INTO_GRAPH1(textfile)
print ('G\t\t=', G)
key = []
pi = []
r = 9
arr = MST_PRIM(G,r)
print ('sum(key)\t=', sum(arr))
'''
textfile = open('tsp.txt', 'r')
G = IMPORT_TEXTFILE_INTO_GRAPH2(textfile)
print ('G\t\t=', G)
key = []
pi = []
r = 1
arr = MST_PRIM(G,r)
print ('sum(key)\t=', sum(arr))
#PRINT_G(G)
#help(dict)