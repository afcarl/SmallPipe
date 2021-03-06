import torch 
import torch.nn as nn 
import torch.nn.functional as F 
import torch.optim as optim


class ControlModel(nn.Module): 

	def __init__(self, code_size, output_size): 

		nn.Module.__init__(self)

		self.l1 = nn.Linear(2*code_size, 64)
		self.l2 = nn.Linear(64,64)
		self.l3 = nn.Linear(64,output_size)

	def forward(self, x): 

		x = F.elu(self.l1(x))
		x = F.elu(self.l2(x))

		return F.tanh(self.l3(x))

	def save(self, path): 

		torch.save(self.state_dict(), path)

	def load(self, path):

		self.load_state_dict(torch.load(path))