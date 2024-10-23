import torch 
from torch.utils.data import Dataset

# blueprint --> creating multiple datasets
class dataset(Dataset): 
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
    return self.len
  
# dataset 1
df1 = dataset()
print(df1[0])
print(df1.len)

# iterate the number of samples with size 10
n_samples = 10
for i in range(n_samples):
  x, y = df1[i]
  print(f"{i}: x={x}, y={y}")