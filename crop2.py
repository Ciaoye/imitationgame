#-*-coding:utf-8-*-
# @desc Created by Qiaoye Zou

import os
from PIL import Image
root=r"D:\用户目录\下载\Documents"
count=0
for f in os.listdir(root):
    im=Image.open(os.path.join(root,f))
    im = im.convert('RGB')
    count += 1
    for l in range(0,7):
        for t in range(0,7):
                cropImg = im.crop((l*64,t*64,l*64+64,t*64+64))
                cropImg.save(r'E:\output3\%s_%s_%s.jpg' % (count, l, t))