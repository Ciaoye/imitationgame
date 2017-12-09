#-*-coding:utf-8-*-
# @desc Created by Qiaoye Zou

import os
from PIL import Image
root=r"E:\inout"
count=0
time=2
cut=0
ima=64
for f in os.listdir(root):
    im=Image.open(os.path.join(root,f))
    width=im.width-cut*2
    height=im.height-cut*2
    im = im.convert('RGB')
#    width=im.width
#    height=im.height
    count+=1
    rewidth=ima*time
    if width<height:
        rewidth=100
        reheight=int(100*height/width)
    else:
        reheight = 100
        rewidth = int(100 * width / height)
#    reheight=int(height/width*ima*time)
#    im=im.crop((0+cut,0+cut,width-cut,height-cut))
    im=im.resize((rewidth,reheight), Image.ANTIALIAS)
#    for l in range(0,rewidth,ima):
#        for t in range(0,reheight-64,ima):
#            cropImg = im.crop((l,t,l+ima,t+ima))
    cropImg = im.crop((18,18,82,82))
#            cropImg.save(r'E:\output2\%s_%s_%s.jpg' % (count,l,t))
    cropImg.save(r'E:\output3\%s.jpg' % (count))