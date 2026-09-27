# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:15:35 2022

@author: 86150
"""
import json
import matplotlib.pyplot as plt
import pandas as pd
color=dict(boxes='black',whiskers='black',medians='red',caps='black')
NT=['HL','SL','SW','TL']
#labels=["{} = 0.10".format(chr(963)),"{} = 0.30".format(chr(963)),"{} = 0.50".format(chr(963)),"{} = 0.70".format(chr(963)),"{} = 0.90".format(chr(963))]
labels=["0.10","0.30","0.50","0.70","0.90"]
for network_type in NT:
    filename="PD_"+network_type
    f=open(".\\saves\\{}.json".format(filename))
    data=json.load(f)
    df=pd.DataFrame(data)
    plt.figure(figsize=(8,8),dpi=400)
    #boxdata=df.plot.box(color=color,positions=[1,2,3,4,5],grid=True)
    plt.boxplot(df,labels=labels,positions=[1,2,3,4,5],medianprops=dict(color='red'),showmeans=True)
    plt.grid(linestyle='--')
    plt.ylabel('Payoffs',fontsize=20)
    plt.xticks(fontsize=20)
    plt.yticks(fontsize=20)
    plt.xlabel('$\sigma$',fontsize=20)
    if network_type=='HL':
        plt.ylim([-0.5,3.5])
    if network_type=='SL':
        plt.ylim([-0.5,4.5])
    #if network_type=='SW':
        #plt.ylim([2.0,15.0])
    if network_type=='TL':
        plt.ylim([0,6.5])
    plt.savefig(".\\saves\\PD_PayoffDistribution_{}.pdf".format(network_type),dpi=500,bbox_inches='tight')
    plt.show()