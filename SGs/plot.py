# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 10:49:08 2021

@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
filename="fc_r_SL_SG"
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
R=np.arange(0,1.05,0.05)
SIGMA=[0.3,0.5,0.7,0.9]
colors=['red','green','blue','black']
markers=['o','s','D','^']
plt.figure(figsize=(8,8))
for sigma in SIGMA:
    plt.plot(R,data["{:.2f}".format(sigma)],lw=2.7,color=colors[SIGMA.index(sigma)],label=(chr(963)+'='+str(sigma)))
plt.xlabel("$r$",fontsize=22)
plt.ylabel("$f_c$",fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.legend(fontsize=20,loc='best')
plt.savefig("{}.pdf".format(filename),dpi=400)
plt.show()