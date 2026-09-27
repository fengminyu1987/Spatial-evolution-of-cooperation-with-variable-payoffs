# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 15:36:03 2022

@author: 86150
"""
import json
import matplotlib.pyplot as plt
import numpy as np
filename="PDexponential"
f=open(".\\saves\\{}.json".format(filename))
data=json.load(f)
B=np.arange(1,1.31,0.01)
NT=["SW","TL","SL","HL"]
colors=['red','green','blue','black']
markers=['o','s','D','^']
plt.figure(figsize=(8,8))
for i in range(4):
    plt.plot(B,data["{}".format(NT[i])][0:32],lw=1,marker='^',markersize=10,color=colors[i],label=(NT[i]))
plt.xlabel("$b$",fontsize=22)
plt.ylabel("$f_c$",fontsize=22)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.ylim([-0.1,1.1])
plt.legend(fontsize=20,loc='best')
plt.savefig(".\\saves\\{}.pdf".format(filename),dpi=400)
plt.show()