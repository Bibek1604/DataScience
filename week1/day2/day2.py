import numpy as np
import time

###creatting array from list

arr_1d=np.array([1,2,3,4,5])
print("1d array :",arr_1d)

arr_2d=np.array([[1,2,3],[4,5,6]])
print("2d array :",arr_2d)


##creating list

py_list=[1,2,3]
print("python list multiplication",py_list*4)

np_array=np.array([1,2,3])
print("python array multiplication",np_array*5)

start=time.time()
py_list 

#creting arrays form scratch

zeros=np.zeros((3,5))
print("zeros",zeros)

ones=np.ones((2,3))
print("ones",ones)

#RANDM
random = np.random.random((2,3))
print("random ",random )

sequence =np.arange(0,10,2)
print("sequence",sequence)

#  vector matrix and tensor 

vector=np.array([1,2,3])
print(vector)

matrix=np.array([[1,2,3],
                 [4,5,6]]) 
print(matrix)


tensor=np.array([[
    [1,2],[3,4]
    ], [
        [5,6],[7,8]
        ]])
print(tensor.shape)
print(tensor.ndim)
print(tensor.size)
print(tensor.dtype)


##Indexing and slicing 
a=np.array([10,20,30,40,50])
print(a[0])
print(a[-1])
print(a[1:3])
print(a)

#mathematicaloperatiron on array

b=np.array([1,2,3])
c=np.array([3,4,5])

print(b+c)
print(b-c)
print(b*c)
print(b/c)