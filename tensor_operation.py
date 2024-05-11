import torch

a = torch.tensor([1,5])
b =torch.tensor([2,7])


#addition
print(a+b)

#scalar multiplication
print(2*a)

#hadmand product
print(a*b)

#dot product
print(torch.dot(a,b))

#adding constant
print(a+2)

#mean
c=torch.tensor([5.0,7.0,3.0,1.0,4.0,5.0])
print(c.mean())

#max
print(a.max())