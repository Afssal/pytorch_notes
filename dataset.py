import torch
from torch.utils.data import Dataset


class toy_set(Dataset):

    #initialse variables
    def __init__(self,length=100,transform=None):
        self.x = 2*torch.ones(length,2)
        self.y = torch.ones(length,1)

        self.len = length
        self.transform = transform
    
    #get length
    def __len__(self):
        return self.len
    
    #extract each value from dataset
    def __getitem__(self,index):
        sample = self.x[index],self.y[index]
        if self.transform:
            sample = self.transform(sample)
        return sample
    

dataset = toy_set()
len(dataset)
print(len(dataset))
for i in range(len(dataset)):
    x,y = dataset[i]
    print(i,x,y)