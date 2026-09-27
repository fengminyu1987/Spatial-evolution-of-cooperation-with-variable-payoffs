# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:15:35 2022

@author: 86150
"""
import json
import matplotlib.pyplot as plt
color=dict(boxes='black',whiskers='black',medians='red',caps='black')
labels=['HL','SL','SW','TL']
f=open(".\\saves\\SG_Exponential.json")
data=json.load(f)
plt.figure(figsize=(10,5),dpi=400)
plt.boxplot([data['HL'],data['SL'],data['SW'],data['TL']],labels=labels,positions=[1,2,3,4],vert=False,medianprops=dict(color='red'),showmeans=True)
plt.grid(linestyle='--')
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
#plt.ylabel('Network Types',fontsize=20)
plt.xlabel('Payoffs',fontsize=20)
plt.savefig(".\\saves\\SG_PayoffDistributionExponential.pdf",dpi=500,bbox_inches='tight')
plt.show()