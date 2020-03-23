# torch imports
import torch.nn.functional as F
import torch.nn as nn


class LinearRegressor(nn.Module):

    def __init__(self, input_features, hidden_dim, output_dim):
        super(LinearRegressor, self).__init__()

        self.fc1 = nn.Linear(input_features, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(p=0.2)
        self.output = nn.Linear(output_dim, 1)
    
    def forward(self, x):        
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.output(x)
        
        return x
    