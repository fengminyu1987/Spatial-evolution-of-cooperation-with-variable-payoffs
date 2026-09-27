# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:49:08 2021

@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
font = {'family' :  'Times New Roman',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 30,
        }
network_type="HL"
filename="r_sigma_"+network_type
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
R=np.arange(0,1.05,0.05)
SIGMA=np.arange(0.05,1.1,0.05)
matrix=[]
#SIGMA=SIGMA[::-1]
for sigma in SIGMA:
    matrix.append(data["{:.2f}".format(sigma)])
for k in range(len(SIGMA)):
    SIGMA[k]=round(SIGMA[k],2)
for k in range(len(R)):
    R[k]=round(R[k],2)
colname=list(SIGMA)
temp=[]
for i in range(len(matrix)):
    temp.append(np.array(matrix[i]))
z=np.array(temp)
z=z.T
z=z[::-1]
#z=matrix
xs,ys = np.meshgrid(SIGMA,R)
plt.figure(figsize=(11,11))
plt.imshow(z,cmap=plt.cm.jet,extent=(0.05,1.05,0,1),interpolation='gaussian',aspect='auto',vmin=0,vmax=1)
cb=plt.colorbar()
cb.set_label(label="$f_c$",fontdict=font,rotation=0)
cb.ax.tick_params(labelsize=25)
plt.xlabel('$\sigma$',fontdict=font)
plt.ylabel('$r$',fontdict=font)
plt.xticks(fontsize=25)
plt.yticks(fontsize=25)
plt.savefig(".\\saves\\"+filename+".pdf",dpi=400)
plt.show()