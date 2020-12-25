import json
import torch
from torch.autograd import Variable
from torchvision import models, transforms
from io import BytesIO
import numpy as np
from PIL import Image

# GPUが使えれば使う 
device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# vgg16の学習済みモデルを利用
model = models.vgg16(pretrained=True)
# GPUが使えれば使う 
model.to(device)
# modelを推論用にする
model.eval()

# train時と同じ条件にする(前処理)
normalize = transforms.Normalize(
    mean=[0.485, 0.456, 0.406],
    std=[0.229, 0.224, 0.225])
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    normalize
])

# ImageNetのラベル
class_index = json.load(open('/app/imagenet_class_index.json', 'r'))

def detect_obj(data):
    # train時と同じ条件にする(前処理)
    img = Image.open(BytesIO(data))
    # train時と同じ条件にする(前処理)
    img_tensor = preprocess(img)
    # GPUが使えれば使う 
    img_tensor = img_tensor.to(device)
    # 入力の先頭はバッチサイズ
    img_tensor.unsqueeze_(0)
    # 推論
    out = model(Variable(img_tensor))
    # スコアの最大値をとる
    l_id = np.argmax(out.data.numpy())
    return class_index[str(l_id)][1]
