# -*- coding: utf-8 -*-
"""mindist.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1REIA9PhV8LmJrZz-mjwTtP_LFOV1XA0J
"""

from multiprocessing import Pool
import numpy as np
import os

def med(str1, str2):
  str1 = str1.lower()
  str2 = str2.lower()

  Distance = np.empty((len(str1) + 1, len(str2) + 1))

  for i in range(0, len(str1) + 1):
    for j in range(0, len(str2) + 1):
      if(i == 0):
        Distance[i,j] = j
      elif(j == 0):
        Distance[i,j] = i
      else:
        temp = 2 if str1[i-1]!=str2[j-1] else 0
        Distance[i,j] = min(Distance[i-1,j] + 1, Distance[i, j-1] + 1, Distance[i-1,j-1] + temp)

  filename = str(str1)+str(int(Distance[len(str1), len(str2)])) 
  f = open(filename, "at")
  f.write(str(str2+"\n"))
  f.close()
  # return Distance[len(str1), len(str2)]

def min_dist_k(str1, final_list, k):
  pool = Pool(processes=16) #processes=len(correct_words)
  for i in range(len(final_list)):
    # print("I: ",i)
    pool.apply_async(med, args=(str1, final_list[i]))
  pool.close()
  pool.join()

  k_list = []
  i = 0
  while(len(k_list)<k):
    filename = str1.lower() + str(i)
    try:
      with open(filename, "r") as f:
        temp = [line.rstrip("\n") for line in f.readlines()]
        if(len(k_list) + len(temp) > k):
          temp = temp[0:k-len(k_list)]
        k_list += temp
    except:
      pass
    i += 1


  all_files = os.listdir()
  for filename in all_files:
    if(str1.lower() in filename):
      os.remove(filename)

  return k_list

# print(med_dict)