import torch
import numpy as np
import pandas as pd

#define tensor
a = torch.tensor([4,6,7,2,1])

#tensor datatype
print(a.dtype)

#type of tensor
print(a.type())


print("-----------------")

#specify datatype 
a = torch.tensor([6,9,1,2],dtype=torch.int32)


print("-----------------")

#specify tensortype
a = torch.FloatTensor([7,8,2,1])

print(a.dtype)

print(a.type())

print("-----------------")

#type convertion
a= torch.tensor([9,8,6,1])
print(a.type())
a = a.type(torch.FloatTensor)
print(a.type())

print("-----------------")


#number of element
print(a.size())

#dimension
print(a.ndimension())

print("------------------")

#1d to 2d dimension
a_col = a.view(4,1)
print(a_col)
print(a_col.ndimension())

a_col_ = a.view(-1,1)
print(a_col_)
print(a_col_.ndimension())


print("---------------------")

#numpy to torch
a = np.array([3,6,8,2,1])
print(type(a))
a_1 = torch.from_numpy(a)
print(a_1)
print(type(a_1))

#torch to numpy
a_2 = a_1.numpy()
print(type(a_2))


print("---------------")

#pandas series to torch

a = pd.Series([8,4,2,1,7])
print(type(a))
b= torch.from_numpy(a.values)
print(type(b))

c = b.tolist()
print(type(c))