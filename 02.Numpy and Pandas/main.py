import numpy as np 
import pandas as pd

# array = np.array(((3,4,5,3),(6,8,5,6)),dtype=int)
# print(array.shape)
# print(array.ndim)

# n1 = np.array([1,2,3,4])
# n2 = np.array([5,6,7,8])
# addition = np.add(n1,n2)
# print(addition)
# print(len(addition))

df = pd.DataFrame({'Name':['John','Smith','Alice'],'Age':[25,30,22],'City':['New York','Los Angeles','Chicago']})
print(df)
# df2 = pd.DataFrame([[4,2,4],[5,6,7],[8,9,10]],columns=['A','B','C'],index=['X','Y','Z'])
# print(df2)