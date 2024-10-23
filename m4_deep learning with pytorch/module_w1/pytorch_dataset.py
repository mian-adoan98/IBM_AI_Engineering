from typing import Any
import torch 
from torch.utils.data import Dataset

# blueprint --> creating multiple datasets
class DataSet(Dataset): 
  def __init__(self, length=100, transform=None): 
    self.x = 2*torch.ones(length, 2)
    self.y = torch.ones(length, 1)
    self.len = length
    self.transform = transform 

  def __getitem__(self, index):
    sample = self.x[index], self.y[index]
    if self.transform:
      sample = self.transform(sample)
    return sample 
    
  def __len__(self):
    return self.le

# transform --> creating multiple transformers to modify the samples of the dataset
class AM_Transform(object):
  def __init__(self, addx, muly):
    self.addx = addx 
    self.muly = muly

  def __call__(self, sample):
    x, y = sample[0], sample[1]
    x = self.addx + x
    y = self.muly * y
    sample = x,y
    return sample 


# dataset 1
df1 = DataSet()
sample1 = df1[0]
print(sample1)
print(df1.len)

# iterate the number of samples with size 10
# n_samples = 10
# for i in range(n_samples):
#   x, y = df1[i]
#   print(f"{i}: x={x}, y={y}")

# transformer 1: method 1
# am_transformer = AM_Transform(2, 1)
# x,y = am_transformer(df1[0])
# print(x,y)

# transformer 1: method 2
am_transformer = AM_Transform(4, 2)
df2 = DataSet(transform=am_transformer)
print(df2[0])