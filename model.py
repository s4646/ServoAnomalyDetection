import torch
from torch import nn

DROP_OUT = 0.2

class Convolutional_Neural_Network(nn.Module):

    def __init__(self):

        super().__init__()
        
        self.conv_1d_1 = nn.Conv1d(1, 16, kernel_size = 9, padding = 1)
        self.drop_1 = nn.Dropout(p=DROP_OUT)
        self.bn_1 = nn.BatchNorm1d(16)
        self.max_pool_1d_1 = nn.MaxPool1d(kernel_size = 3)

        self.conv_1d_2 = nn.Conv1d(16, 64, kernel_size = 7, padding = 1)
        self.drop_2 = nn.Dropout(p=DROP_OUT)
        self.bn_2 = nn.BatchNorm1d(64)
        self.max_pool_1d_2 = nn.MaxPool1d(kernel_size = 3)

        self.conv_1d_3 = nn.Conv1d(64, 128, kernel_size = 5, padding = 1)
        self.drop_3 = nn.Dropout(p=DROP_OUT)
        self.bn_3 = nn.BatchNorm1d(128)
        self.max_pool_1d_3 = nn.MaxPool1d(kernel_size = 3)

        self.conv_1d_4 = nn.Conv1d(128, 256, kernel_size = 3, padding = 1)
        self.drop_4 = nn.Dropout(p=DROP_OUT)
        self.bn_4 = nn.BatchNorm1d(256)
        
        self.global_avg_pooling_1d = nn.AdaptiveAvgPool1d(1)
        self.flatten = nn.Flatten()

        self.dense = nn.Linear(256, 1) # change to 1 for sigmoid

        self.activation = nn.Sigmoid() # if 1 use sigmoid

    def forward(self, X):

        x = nn.ReLU()(self.conv_1d_1(X))
        x = self.drop_1(x)
        x = self.bn_1(x)
        x = self.max_pool_1d_1(x)

        x = nn.ReLU()(self.conv_1d_2(x))
        x = self.drop_2(x)
        x = self.bn_2(x)
        x = self.max_pool_1d_2(x)

        x = nn.ReLU()(self.conv_1d_3(x))
        x = self.drop_3(x)
        x = self.bn_3(x)
        x = self.max_pool_1d_3(x)

        x = nn.ReLU()(self.conv_1d_4(x))
        x = self.drop_4(x)
        x = self.bn_4(x)

        x = self.global_avg_pooling_1d(x)
        x = self.flatten(x) # flatten before entering the dense layer
        x = nn.ReLU()(self.dense(x))

        y = self.activation(x) # if 1 use sigmoid

        return y

    def get_epochs(self):
        return 10

    def get_learning_rate(self):
        return 1e-03

    def get_batch_size(self):
        return 16
