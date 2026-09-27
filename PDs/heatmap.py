# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:49:08 2021
cmap=jet
@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator
font = {'family' :  'Times New Roman',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 30,
        }
network_type="HL"
if network_type=="SL" or network_type=="HL":
    bupper=1.2
    x_major_locator=MultipleLocator(0.05)
if network_type=="SW":
    bupper=2
    x_major_locator=MultipleLocator(0.2)
if network_type=="TL":
    bupper=1.4
    x_major_locator=MultipleLocator(0.1)
filename="b_sigma_"+network_type
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
B=np.arange(1,1.21,0.05)
SIGMA=np.arange(0.05,1.1,0.05)
matrix=[]
#SIGMA=SIGMA[::-1]
for sigma in SIGMA:
    matrix.append(data["{:.2f}".format(sigma)])
for k in range(len(SIGMA)):
    SIGMA[k]=round(SIGMA[k],2)
for k in range(len(B)):
    B[k]=round(B[k],2)
colname=list(SIGMA)
temp=[]
for i in range(len(matrix)):
    temp.append(np.array(matrix[i]))
z=np.array(temp)
z=z.T
z=z[::-1]
xs,ys = np.meshgrid(B,SIGMA)
plt.figure(figsize=(11,11))
#SL,HL:1-1.2；SW:1-2；TL：1.4
plt.imshow(z,cmap=plt.cm.jet,extent=(0.05,1.05,1,bupper),interpolation='gaussian',aspect='auto',vmin=0,vmax=1)
cb=plt.colorbar()
cb.set_label(label="$f_c$",fontdict=font,rotation=0)
cb.ax.tick_params(labelsize=25)
plt.ylabel('$b$',fontdict=font)
plt.xlabel('$\sigma$',fontdict=font)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
ax=plt.gca()
ax.yaxis.set_major_locator(x_major_locator)
plt.savefig(".\\saves\\test"+filename+".pdf",dpi=400)
plt.show()