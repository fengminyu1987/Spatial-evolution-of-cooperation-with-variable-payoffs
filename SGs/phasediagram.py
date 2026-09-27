# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 20:28:53 2021
Phase Diagrams
@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
font = {'family' :  'Times New Roman',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 20,
        }
network_type="HL"
filename="r_sigma_"+network_type
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
R=np.arange(0,1.05,0.05)
SIGMA=np.arange(0.05,1.1,0.05)
Xc=[]
Yc=[]
for sigma in SIGMA:
    row=data["{:.2f}".format(sigma)]
    for i in range(len(row)):
        if row[i]!=1 and i!=0:
            Yc.append(R[i-1])
            Xc.append(sigma)
            break
        elif row[i]!=1 and i==0:
            Yc.append(R[i])
            Xc.append(sigma)
            break
f = interpolate.interp1d(Xc, Yc, kind = 'quadratic')
Xcn=np.arange(min(Xc),max(Xc),0.01)
Ycn=f(Xcn)
Xd=[]
Yd=[]
for sigma in SIGMA:
    row=data["{:.2f}".format(sigma)]
    for i in range(len(row)):
        if row[i]==0 and i!=0:
            Yd.append(R[i-1])
            Xd.append(sigma)
            break
        elif row[i]==0 and i==0:
            Yd.append(R[i])
            Xd.append(sigma)
            break
f = interpolate.interp1d(Xd, Yd, kind = 'quadratic')
Xdn=np.arange(min(Xd),max(Xd),0.01)
Ydn=f(Xcn)
plt.figure(figsize=(8,8))
plt.plot(Xcn,Ycn)
plt.plot(Xdn,Ydn)
plt.xlim([0.05,1.05])
plt.ylim([0,1])
plt.xlabel("$r$",fontdict=font)
plt.xlabel("$\sigma$",fontdict=font)
plt.show()