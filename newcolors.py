#!/usr/bin/env python
# coding=utf-8
#######################################################
#
# Author: Dr. Xudong Zhou
# Mail: x.zhou@rainbow.iis.u-tokyo.ac.jp
# 
# ---------------------------------------------------
#
# 程序介绍及使用方法：
# 本程序依据IPCC的可视化指南，将不同颜色以及色带电子化，以供使用。指南原文请见
# https://www.ipcc.ch/site/assets/uploads/2019/04/IPCC-visual-style-guide.pdf
# 包括的颜色为
# 单色：l1~l6(线), and l1s~l6s(阴影)
# 表示不同情景的单色：r85l, r60l, r45l, r26l (线)，以及 r85s, r60s, r45s, r26s (阴影)
# 用于表示温度的色带：t5~t11 （数字代表颜色分级数量）
# 用于表示降水的色带：p5~p11
# 单色的递进色带：共有4个色系（blue, purple, red, green），分3，4，5级，例如 blue3s~blue5s，代表绿色系3-5级
# 多色的递进色带：分类与上相同，颜色区别度更高
# 如果想用使用相反的色带，可以在色带名称后加"_r"
# 使用方法：
# （0）首先将本文件拷贝到工作文件夹
#  import newcolors   # 加载
#
# （1）使用单个颜色 
#   c = newcolors.newcolor(ColorName) # ColorName即想要的颜色
# 举例：
#   plt.plot( data, c = newcolors.newcolor('l2')) # 画一条淡蓝色的线: rgb(112, 160, 205)
#
# (2) 如果需要使用色带，本程序末有一个示例
#   cmap = newcolors.newcmp(ColormapName) # 加载一个名为 ColormapName的色带
# 举例
#   im = plt.imshow(data, norm = norml, cmap=newcolors.newcmp('green5m'))  # 使用 "greem5m"
# 
# 注意，这些色带是离散的颜色，因此最好提前定义好色带的数量，选择相同数量的色带（如果使用连续性的问题也不大）
# ------------------------------------------------------
#
# ReadMe
# Colors and colormap digitalized from "IPCC Visual Style Guide for Authors"
# Link: https://www.ipcc.ch/site/assets/uploads/2019/04/IPCC-visual-style-guide.pdf
# Including names of color
# single colors, l1~l6(line color), and l1s~l6s(shadow color)
# Single color for RCP, r85l, r60l, r45l, r26l (line color) and r85s, r60s, r45s, r26s (shadow color)
# Sequential colors for Temperature: t5~t11 (number represents the number of color bands)
# Sequential colors for Precipitation: p5~p11
# Single-hue sequential schemes: blue3s~blue5s, purple3s~purple5s, red3s~red5s and green3s~grenn5s
# Multi-hue sequential schemes: blue3m~blue5m, purple3s~5s, red3s~red5s and green3s~green5s
# If users want to reverse the colormap, add "_r" to the name 
# 
# How to use it?
# (0) copy this file to your working folder, then import 
# import newcolors # Load
#
# (1) If you want to use a single color 
#   c = newcolors.newcolor(ColorName) # colorname is the list names 
# e.g., 
#   plt.plot( data, c = newcolors.newcolor('l2')) # plot a line in light blue: rgb(112, 160, 205)
#
# (2) If you want to use a colormap, there is a sample code in the end of this file. 
#   cmap = newcolors.newcmp(ColormapName) # call a new colormap named ColormapName
# e.g., 
#   im = plt.imshow(dc, norm = norml, cmap=newcolors.newcmp('green5m'))  # using the colormap named "greem5m", 5 bands of green color
# 
# Note that the colormap are designed for discrete colors, better to use same number of color bands as the name identifed. 
# 
#######################################################
import matplotlib
matplotlib.use('Agg')
import numpy as np
from matplotlib import colors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#
def rgb(a,b,c):
    out = np.zeros(3, 'f')
    out[0] = a / 255.
    out[1] = b / 255.
    out[2] = c / 255.
    return out 

def newcolor(name):
    if name == 'l1':
        return l1()
    if name == 'l2':
        return l2() 
    if name == 'l3':
        return l3() 
    if name == 'l4':
        return l4() 
    if name == 'l5':
        return l5() 
    if name == 'l6':
        return l6() 

    if name == 'l1s':
        return l1s()
    if name == 'l2s':
        return l2s() 
    if name == 'l3s':
        return l3s() 
    if name == 'l4s':
        return l4s() 
    if name == 'l5s':
        return l5s() 
    if name == 'l6s':
        return l6s() 

    if name == 'r85l':
        return r85l() 
    if name == 'r60l':
        return r60l() 
    if name == 'r45l':
        return r45l() 
    if name == 'r26l':
        return r26l() 

    if name == 'r85s':
        return r85s() 
    if name == 'r60s':
        return r60s() 
    if name == 'r45s':
        return r45s() 
    if name == 'r26s':
        return r26s() 

## ----------------------------------------------------
def newcmp(name):
    # Temperature
    if name.find('t5') == 0:
        cdict = t5_c()
    if name.find('t6') == 0:
        cdict = t6_c()
    if name.find('t7') == 0:
        cdict = t7_c()
    if name.find('t8') == 0:
        cdict = t8_c()
    if name.find('t9') == 0:
        cdict = t9_c()
    if name.find('t10') == 0:
        cdict = t10_c()
    if name.find('t11') == 0:
        cdict = t11_c()
    
    # Precipitation
    if name.find('p5') == 0:
        cdict = p5_c()
    if name.find('p6') == 0:
        cdict = p6_c()
    if name.find('p7') == 0:
        cdict = p7_c()
    if name.find('p8') == 0:
        cdict = p8_c()
    if name.find('p9') == 0:
        cdict = p9_c()
    if name.find('p10') == 0:
        cdict = p10_c()
    if name.find('p11') == 0:
        cdict = p11_c()   
    
    # single-hue sequential schemes
    # Blue
    if name.find('blue3s') == 0:
        cdict = blue3s_c()  
    if name.find('blue4s') == 0:
        cdict = blue4s_c()  
    if name.find('blue5s') == 0:
        cdict = blue5s_c()  

    # purple
    if name.find('purple3s') == 0:
        cdict = purple3s_c()  
    if name.find('purple4s') == 0:
        cdict = purple4s_c()  
    if name.find('purple5s') == 0:
        cdict = purple5s_c()  

    # red
    if name.find('red3s') == 0:
        cdict = red3s_c()  
    if name.find('red4s') == 0:
        cdict = red4s_c()  
    if name.find('red5s') == 0:
        cdict = red5s_c()  

    # green
    if name.find('green3s') == 0:
        cdict = green3s_c()  
    if name.find('green4s') == 0:
        cdict = green4s_c()  
    if name.find('green5s') == 0:
        cdict = green5s_c()  

    # Multi-hue sequential schemes
    # Blue
    if name.find('blue3m') == 0:
        cdict = blue3m_c()  
    if name.find('blue4m') == 0:
        cdict = blue4m_c()  
    if name.find('blue5m') == 0:
        cdict = blue5m_c()  

    # purple
    if name.find('purple3m') == 0:
        cdict = purple3m_c()  
    if name.find('purple4m') == 0:
        cdict = purple4m_c()  
    if name.find('purple5m') == 0:
        cdict = purple5m_c()  

    # red
    if name.find('red3m') == 0:
        cdict = red3m_c()  
    if name.find('red4m') == 0:
        cdict = red4m_c()  
    if name.find('red5m') == 0:
        cdict = red5m_c()  

    # green
    if name.find('green3m') == 0:
        cdict = green3m_c()  
    if name.find('green4m') == 0:
        cdict = green4m_c()  
    if name.find('green5m') == 0:
        cdict = green5m_c()  

    # Reverse colormap
    if name.find('_r') > 0:
        cdict = np.flipud(cdict)

    newcmp = LinearSegmentedColormap.from_list(name, cdict)
    return newcmp  




#Lines 
def l1():
    return rgb(0,0,0)

def l2():
    return rgb(112,160,205)

def l3():
    return rgb(196,121,0)

def l4():
    return rgb(178,178,178)

def l5():
    return rgb(0,52,102)

def l6():
    return rgb(0,79,0)

def l1s():
    return rgb(128,128,128)

def l2s():
    return rgb(91,174,178)

def l3s():
    return rgb(204,174,113)

def l4s():
    return rgb(191,191,191)

def l5s():
    return rgb(67,147,195)

def l6s():
    return rgb(223,237,195)

# RCPs 

def r85l():
    return rgb(153,0,2)

def r85s():
    return rgb(252,209,197)

def r60l():
    return rgb(196,121,0)

def r60s():
    return rgb(204,174,113)

def r45l():
    return rgb(112,160,205)

def r45s():
    return rgb(146,197,222)

def r26l():
    return rgb(0,52,102)

def r26s():
    return rgb(67,147,195)


# Temperature 
def t5_c():
    col_dict=[  rgb(202,0,32),
                rgb(244,165,130),
                rgb(247,247,247),
                rgb(146,197,222),
                rgb(5,113,176)         
                ]
    
    return col_dict

def t6_c():
    col_dict=[  rgb(178,24,43),
                rgb(239,138,98),
                rgb(253,219,199),
                rgb(209,229,240),
                rgb(103,169,207),
                rgb(33,102,172)         
                ]
    
    return col_dict

def t7_c():
    col_dict=[  rgb(178,24,43),
                rgb(239,138,98),
                rgb(253,219,199),
                rgb(247,247,247),
                rgb(209,229,240),
                rgb(103,169,207),
                rgb(33,102,172)          
                ]
    
    return col_dict

def t8_c():
    col_dict=[  rgb(178,24,43),
                rgb(214,96,77),
                rgb(244,165,130),
                rgb(253,219,199),
                rgb(209,229,240),
                rgb(146,197,222),
                rgb(67,147,195),
                rgb(33,102,172)          
                ]
    
    return col_dict

def t9_c():
    col_dict=[  rgb(178,24,43),
                rgb(214,96,77),
                rgb(244,165,130),
                rgb(253,219,199),
                rgb(247,247,247),
                rgb(209,229,240),
                rgb(146,197,222),
                rgb(67,147,195),
                rgb(33,102,172)          
                ]
    
    return col_dict

def t10_c():
    col_dict=[  rgb(103,0,31),
                rgb(178,24,43),
                rgb(214,96,77),
                rgb(244,165,130),
                rgb(253,219,199),
                rgb(209,229,240),
                rgb(146,197,222),
                rgb(67,147,195),
                rgb(33,102,172),
                rgb(5,48,97)         
                ]
    return col_dict

def t11_c():
    col_dict=[  rgb(103,0,31),
                rgb(178,24,43),
                rgb(214,96,77),
                rgb(244,165,130),
                rgb(253,219,199),
                rgb(247,247,247),
                rgb(209,229,240),
                rgb(146,197,222),
                rgb(67,147,195),
                rgb(33,102,172),
                rgb(5,48,97)         
                ]
    
    return col_dict

# Precipitation 
def p5_c():
    col_dict=[  rgb(166,97,26),
                rgb(223,194,125),
                rgb(245,245,245),
                rgb(128,205,193),
                rgb(1,133,113)         
                ]
    
    return col_dict

def p6_c():
    col_dict=[  rgb(140,81,10),
                rgb(216,179,101),
                rgb(246,232,195),
                rgb(199,234,229),
                rgb(90,180,172),
                rgb(1,102,94)         
                ]
    
    return col_dict

def p7_c():
    col_dict=[  rgb(140,81,10),
                rgb(216,179,101),
                rgb(246,232,195),
                rgb(245,245,245),
                rgb(199,234,229),
                rgb(90,180,172),
                rgb(1,102,94)         
                ]
    
    return col_dict

def p8_c():
    col_dict=[  rgb(140,81,10),
                rgb(191,129,45),
                rgb(223,194,125),
                rgb(246,232,195),            
                rgb(199,234,229),
                rgb(128,205,193),
                rgb(53,151,143),
                rgb(1,102,94)       
                ]
    
    return col_dict

def p9_c():
    col_dict=[  rgb(140,81,10),
                rgb(191,129,45),
                rgb(223,194,125),
                rgb(246,232,195),   
                rgb(245,245,245),         
                rgb(199,234,229),
                rgb(128,205,193),
                rgb(53,151,143),
                rgb(1,102,94)       
                ]
    
    return col_dict

def p10_c():
    col_dict=[  rgb(84,48,5),
                rgb(140,81,10),
                rgb(191,129,45),
                rgb(223,194,125),
                rgb(246,232,195),            
                rgb(199,234,229),
                rgb(128,205,193),
                rgb(53,151,143),
                rgb(1,102,94), 
                rgb(0,60,48)    
                ]

    return col_dict

def p11_c():
    col_dict=[  rgb(84,48,5),
                rgb(140,81,10),
                rgb(191,129,45),
                rgb(223,194,125),
                rgb(246,232,195),  
                rgb(245,245,245),           
                rgb(199,234,229),
                rgb(128,205,193),
                rgb(53,151,143),
                rgb(1,102,94),   
                rgb(0,60,48)    
                ]
    
    return col_dict

# single-hue sequential schemes
# blue
def blue3s_c():
    col_dict=[  rgb(222,235,147),
                rgb(158,202,225),
                rgb(49,130,189),        
                ]
    
    return col_dict

def blue4s_c():
    col_dict=[  rgb(239,243,255),
                rgb(189,215,231),
                rgb(107,174,214),
                rgb(33,113,181)         
                ]
    
    return col_dict

def blue5s_c():
    col_dict=[  rgb(239,243,255),
                rgb(189,215,231),
                rgb(107,174,214),
                rgb(49,130,189),
                rgb(8,81,156)         
                ]
    
    return col_dict

# purple
def purple3s_c():
    col_dict=[  rgb(239,237,245),
                rgb(188,189,220),
                rgb(117,107,177),        
                ]
    
    return col_dict

def purple4s_c():
    col_dict=[  rgb(242,240,247),
                rgb(203,201,226),
                rgb(158,154,200),
                rgb(106,81,163)         
                ]
    
    return col_dict

def purple5s_c():
    col_dict=[  rgb(242,240,247),
                rgb(203,201,226),
                rgb(158,154,200),
                rgb(117,107,177),
                rgb(84,39,143)         
                ]
    
    return col_dict

# Red
def red3s_c():
    col_dict=[  rgb(254,224,210),
                rgb(252,146,116),
                rgb(222,45,38),        
                ]
    
    return col_dict

def red4s_c():
    col_dict=[  rgb(254,229,217),
                rgb(252,174,145),
                rgb(251,106,74),
                rgb(203,24,29)         
                ]
    
    return col_dict

def red5s_c():
    col_dict=[  rgb(254,229,217),
                rgb(252,174,145),
                rgb(251,106,74),
                rgb(222,45,38),
                rgb(165,15,21)         
                ]
    
    return col_dict

# Red
def green3s_c():
    col_dict=[  rgb(229,245,224),
                rgb(161,217,155),
                rgb(49,163,84),        
                ]
    
    return col_dict

def green4s_c():
    col_dict=[  rgb(237,248,233),
                rgb(186,228,179),
                rgb(116,196,118),
                rgb(35,139,69)         
                ]
    
    return col_dict

def green5s_c():
    col_dict=[  rgb(237,248,233),
                rgb(186,228,179),
                rgb(116,196,118),
                rgb(49,163,84),
                rgb(0,109,44)         
                ]
    
    return col_dict

# Multi-hue sequential schemes
# blue
def blue3m_c():
    col_dict=[  rgb(237,248,177),
                rgb(127,205,187),
                rgb(44,127,184),        
                ]
    
    return col_dict

def blue4m_c():
    col_dict=[  rgb(255,255,204),
                rgb(161,218,180),
                rgb(65,182,196),
                rgb(34,94,168)         
                ]
    
    return col_dict

def blue5m_c():
    col_dict=[  rgb(255,255,204),
                rgb(161,218,180),
                rgb(65,182,196),
                rgb(44,127,184),
                rgb(37,52,148)         
                ]
    
    return col_dict

# purple
def purple3m_c():
    col_dict=[  rgb(224,236,244),
                rgb(158,188,218),
                rgb(136,86,167),        
                ]
    
    return col_dict

def purple4m_c():
    col_dict=[  rgb(237,248,251),
                rgb(179,205,227),
                rgb(140,150,198),
                rgb(136,65,157)         
                ]
    
    return col_dict

def purple5m_c():
    col_dict=[  rgb(237,248,251),
                rgb(179,205,227),
                rgb(140,150,198),
                rgb(136,86,167),
                rgb(129,15,124)         
                ]
    
    return col_dict

# red
def red3m_c():
    col_dict=[  rgb(254,237,160),
                rgb(254,178,76),
                rgb(240,59,32),        
                ]
    
    return col_dict

def red4m_c():
    col_dict=[  rgb(255,255,178),
                rgb(254,204,92),
                rgb(253,141,60),
                rgb(227,26,28)         
                ]
    
    return col_dict

def red5m_c():
    col_dict=[  rgb(255,255,178),
                rgb(254,204,92),
                rgb(253,141,60),
                rgb(240,59,32),
                rgb(189,0,38)         
                ]
    
    return col_dict

# green
def green3m_c():
    col_dict=[  rgb(247,252,185),
                rgb(173,221,142),
                rgb(49,163,84),        
                ]
    
    return col_dict

def green4m_c():
    col_dict=[  rgb(255,255,204),
                rgb(194,230,153),
                rgb(120,198,121),
                rgb(35,132,67)         
                ]
    
    return col_dict

def green5m_c():
    col_dict=[  rgb(255,255,204),
                rgb(194,230,153),
                rgb(120,198,121),
                rgb(49,163,84),
                rgb(0,104,55)         
                ]
    
    return col_dict


## ----------------------------------------------------

if __name__=='__main__':
    C=np.random.rand(500).reshape((20,25))
    S=np.random.rand(500).reshape((20,25))

    # range (0,2)
    dc = S**2+C
    vmin = 0
    vmax = 2
    inter = 0.2

    # JET, RAINBOW
    fig=plt.figure(figsize=(4,3),dpi=300)
    fig.subplots_adjust(left=0.1,right=0.85,top=0.90,bottom=0.1)
    ax = fig.add_subplot(1,1,1)

    interval = np.array(np.arange(vmin,vmax+inter/2.,inter))
    norml = colors.BoundaryNorm(interval, 256)

    im = plt.imshow(dc, norm = norml, cmap='rainbow')

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="2%", pad=0.15)
    cbar = plt.colorbar(im, cax=cax)
    cbar.ax.tick_params()

    plt.savefig('colors-old.jpg')

    ###
    # newcolors
    fig=plt.figure(figsize=(4,3),dpi=300)
    fig.subplots_adjust(left=0.1,right=0.85,top=0.90,bottom=0.1)
    ax = fig.add_subplot(1,1,1)

    interval = np.array(np.arange(vmin,vmax+inter/2.,inter))
    norml = colors.BoundaryNorm(interval, 256)

    im = plt.imshow(dc, norm = norml, cmap=newcmp('p10'))

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="2%", pad=0.15)
    cbar = plt.colorbar(im, cax=cax)
    cbar.ax.tick_params()

    plt.savefig('colors-new.jpg')
