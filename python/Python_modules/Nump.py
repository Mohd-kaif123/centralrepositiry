# NumPy is used for fast numerical computations in Python. 
# It provides support for large multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays.   
# It is widely used in scientific computing, data analysis,Automation and machine learning.
# To Install: sudo apt install python3-numpy
import numpy as np

arr= np.array([1,2,3,4,5])
print(arr*2)

# create 1d Array
arr1= np.array([10,20,30,40,50])
print("\n1D Array:", arr1)

# create 2d Array
arr2= np.array([[1,2,3],[4,5,6]])
print("\n2D Array:", arr2)

# reshape array used to change the shape of an array without changing its data.
reshapped=arr2.reshape(3,2)
print("\nReshaped Array:", reshapped)

print("\n SUM:",arr1.sum())
print("\n MEAN:",arr1.mean())
print("\n MAX:",arr1.max())
print("\n MIN:",arr1.min())
# WAP to write MIN.MAX,SUM,MEAN of 2D Array