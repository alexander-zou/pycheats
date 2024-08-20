#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

@File   : use_imageio.py   
@Author : alexander.here@gmail.com
@Date   : 2024-08-20 15:00    (+0800)   
@Brief  :  

'''

# 最好使用FFMpeg作为视频编码后端:
# better to use FFMpeg as backend:
#   pip install imageio[ffmpeg]

import imageio.v2 as imageio # or use v3 for newer apis

# 截屏 Take Screenshot:
image = imageio.imread( '<screen>') # or '<clipboard>' to paste

# 保存RGB图像 Save Image:
imageio.imwrite( 'screen.png', image)

# 读取图像 Load/Decode Image:
image = imageio.imread( 'screen.png')
h, w, ch = image.shape

# 视频编码 Save/Encode Video:
VIDEO_H, VIDEO_W = 480, 640; assert( VIDEO_W < w and VIDEO_H < h)
FRAMES = 360

with imageio.get_writer( "screen.mp4", fps=30, quality=10, codec='libx264') as writer:
    sx = sy = 0
    for fno in range( FRAMES):
        print( f'generating video frame {fno+1:03d}/{FRAMES} ...')
        frame = image[ sy:sy+VIDEO_H, sx:sx+VIDEO_W].copy()
        sx = ( sx + 3) % ( w - VIDEO_W)
        sy = ( sy + 7) % ( h - VIDEO_H)
        # add one frame:
        writer.append_data( frame)

# End of 'use_imageio.py' 

