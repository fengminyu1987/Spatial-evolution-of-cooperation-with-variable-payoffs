# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:49:08 2021

@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
filename="fc_b_SL_PD"
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
B=np.arange(1,1.2,0.02)
SIGMA=[0.3,0.5,0.7,0.9]
colors=['red','green','blue','black']
markers=['o','s','D','^']
plt.figure(figsize=(8,8))
for sigma in SIGMA:
    plt.plot(B,data["{:.2f}".format(sigma)],lw=2.7,marker=markers[SIGMA.index(sigma)],markersize=12,color=colors[SIGMA.index(sigma)],label=(chr(963)+'='+str(sigma)))
plt.xlabel("$b$",fontsize=22)
plt.ylabel("$f_c$",fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.ylim([-0.1,1.1])
plt.legend(fontsize=20,loc='best')
plt.savefig("{}.pdf".format(filename),dpi=400)
plt.show()