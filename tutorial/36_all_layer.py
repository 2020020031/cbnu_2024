import torch
import torch.nn as nn

def get_num_params(model):
    """
    모델(레이어)의 파라미터 수를 계산하는 함수
    
    Args:
        model : torch.nn.Module
    Returns:
        num_params : int
    """
    return sum([p.numel() for p in model.parameters()])


## model1 : conv -> batchnorm -> relu -> maxpool -> conv -> batchnorm -> relu -> maxpool
## model2 : linear -> relu -> dropout -> linear -> sigmoid

inp1 = torch.randn(128, 3, 32, 32)
model1 = []
model1 += [nn.Conv2d(3, 32, kernel_size=3, padding=1)]
model1 += [nn.BatchNorm2d(32)]
model1 += [nn.ReLU()]
model1 += [nn.MaxPool2d(kernel_size=2, stride=2)]
model1 += [nn.Conv2d(32, 64, kernel_size=3, padding=1)]
model1 += [nn.BatchNorm2d(64)]
model1 += [nn.ReLU()]
model1 += [nn.MaxPool2d(kernel_size=2, stride=2)]
model1 = nn.Sequential(*model1)
print(model1)
print(f"Number of parameters in model1: {get_num_params(model1)}")
out1 = model1(inp1)
print(out1.size())

inp2 = torch.randn(128, 4096)
model2 = []
model2 += [nn.Linear(4096, 4096)]
model2 += [nn.ReLU()]
model2 += [nn.Dropout(p=0.5)]
model2 += [nn.Linear(4096, 10)]
model2 += [nn.Sigmoid()]
model2 = nn.Sequential(*model2)
print(model2)
print(f"Number of parameters in model2: {get_num_params(model2)}")
out2 = model2(inp2)
print(out2.size())
