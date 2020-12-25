import torch
from torch.autograd import Variable
from torchvision import models, transforms
from io import BytesIO

import json
import numpy as np
from PIL import Image

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
model = models.vgg16(pretrained=True)
model.to(device)
model.eval()
normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225])

preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    normalize
])
class_index = json.load(open('/app/imagenet_class_index.json', 'r'))

def detect_obj(data):
    img = Image.open(BytesIO(data))
    img_tensor = preprocess(img)
    img_tensor = img_tensor.to(device)
    img_tensor.unsqueeze_(0)

    out = model(Variable(img_tensor))
    l_id = np.argmax(out.data.numpy())
    return class_index[str(l_id)][1]
