# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:49:08 2021
cmap=jet
@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
font = {'family' :  'Times New Roman',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 20,
        }
network_type="SL"
filename="b_sigma_"+network_type
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
B=np.arange(1,1.22,0.01)
SIGMA=np.arange(0.05,1.1,0.05)
matrix=[]
SIGMA=SIGMA[::-1]
for sigma in SIGMA:
    matrix.append(data["{:.2f}".format(sigma)])
for k in range(len(SIGMA)):
    SIGMA[k]=round(SIGMA[k],2)
for k in range(len(B)):
    B[k]=round(B[k],2)
xs,ys = np.meshgrid(B,SIGMA)
z=matrix
plt.figure(figsize=(6,8))
#plt.imshow(z,cmap=plt.cm.jet,extent=(1,1.2,0.05,1.05),interpolation='gaussian',vmin=0,vmax=1)
cset = plt.contourf(xs,ys,z,interpolation='gaussian',cmap=plt.cm.jet)
contour = plt.contour(xs,ys,z,4,colors='k')
plt.clabel(contour,fontsize=10,colors='k')
cb=plt.colorbar(cset)
cb.set_label(label="$f_c$",fontdict=font,rotation=0)
cb.ax.tick_params(labelsize=20)
plt.xlabel('$b$',fontdict=font)
plt.ylabel('$\sigma$',fontdict=font)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig(".\\saves\\test"+filename+".pdf",dpi=400)
plt.show()