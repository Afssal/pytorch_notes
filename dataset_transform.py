import torch
from torch.utils.data import Dataset
from torchvision import transforms
class toy_set(Dataset):


    #initialise variables
    def __init__(self,transform=None,length=None):

        self.x = 2*torch.ones(length,2)
        self.y = torch.ones(length,1)
        self.transform = transform
        self.length =length

    #get length
    def __len__(self):
        return self.length
    
    #get each item
    def __getitem__(self,index):
        sample = self.x[index],self.y[index]
        if self.transform:
            sample = self.transform(sample)
        
        return sample

#another class for transform    
class addition(object):

    #initialise
    def __init__(self,addx=None,addy=None):
        self.addx = addx
        self.addy = addy

    #perform operation
    def __call__(self,sample):
        x = sample[0]
        y = sample[1]
        x = x+self.addx
        y = y+self.addy
        sample = x,y
        return sample
    
class multiplication(object):


    def __init__(self,mulx=None,muly=None):
        self.mulx = mulx
        self.muly = muly

    
    def __call__(self,sample):
        x = sample[0]
        y = sample[1]
        x = x*self.mulx
        y = y*self.muly
        sample = x,y
        return sample


data_trans = transforms.Compose([addition(2,4),multiplication(7,4)])
    
#trans = addition(2,4)
dataset = toy_set(transform=data_trans,length=200)

print(len(dataset))

for i in range(len(dataset)):
    x,y = dataset[i]
    print(i,x,y)

