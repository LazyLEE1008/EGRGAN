import torch
import torchvision
import torch.nn as nn

class Vgg16(nn.Module):
    def __init__(self):
        super(Vgg16, self).__init__()
        feature = torchvision.models.vgg16(pretrained=True).features
        self.to_relu_1_2 = nn.Sequential()
        self.to_relu_2_2 = nn.Sequential()
        self.to_relu_3_3 = nn.Sequential()
        self.to_relu_4_3 = nn.Sequential()

        for x in range(4):
            self.to_relu_1_2.add_module(str(x), feature[x])

        for x in range(4, 9):
            self.to_relu_2_2.add_module(str(x), feature[x])

        for x in range(9, 16):
            self.to_relu_3_3.add_module(str(x), feature[x])

        for x in range(16, 23):
            self.to_relu_4_3.add_module(str(x), feature[x])

        for param in self.parameters():
            param.requires_grad = False

    def forward(self, x):
        h = self.to_relu_1_2(x)
        h_relu_1_2=h

        h = self.to_relu_2_2(h)
        h_relu_2_2=h

        h = self.to_relu_3_3(h)
        h_relu_3_3 = h

        h = self.to_relu_4_3(h)
        h_relu_4_3 = h

        out = (h_relu_1_2, h_relu_2_2, h_relu_3_3, h_relu_4_3)
        return out

