# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 17:04:41 2021
Evolutionary games with stochastic payoff
On Snow-drift Games With The Parameter r
fc_t_SL_SG
@author: 86150
"""
import networkx as nx
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
#参数列
r=0.5#博弈参数
T=10000#最大迭代时间
N=1000#网络规模，对随机网络
L=50#正则格子宽度
sigma=0.3#正态分布方差
SIGMA=[0.3,0.5,0.7,0.9]
colors=['red','green','blue','black']
#产生Square Lattice，L为方格宽度
def square_lattice(L):
    G=nx.generators.lattice.grid_graph(dim=(1, L, L))
    #构造周期性边界
    for i in range(L):
        G.add_edge((0,i,0),(L-1,i,0))
        G.add_edge((i,0,0),(i,L-1,0))
    return G
def get_all_payoff(G,strategy,r,sigma):
    payoff={}
    for i in G.nodes:
        i_payoff=0
        if strategy[i]==0:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.normal(1,sigma)
                elif strategy[nei]==1:
                    i_payoff+=np.random.normal(1-r,sigma)
        elif strategy[i]==1:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.normal(1+r,sigma)
                elif strategy[nei]==1:
                    i_payoff+=0
        payoff[i]=i_payoff
    return payoff
#初始化
#G=square_lattice(L)#正则格子
#G=nx.barabasi_albert_graph(N,5)
G=nx.generators.lattice.triangular_lattice_graph(L,L,periodic=True)
print(len(G.nodes))
X=np.arange(1,T+2,1)
plt.figure(figsize=(10,6))
for sigma in SIGMA:
    Y=[]
    strategy={}
    for i in G.nodes:
        strategy[i]=int(0<=random.uniform(0,1)<=0.5)
    fc=(len(G.nodes)-sum(strategy.values()))/len(G.nodes)
    Y.append(fc)
    for t in range(T):
        if (0<fc<1):
            payoff=get_all_payoff(G,strategy,r,sigma)
            old_strategy=copy.deepcopy(strategy)
            for x in G.nodes:
                y=random.choice(list(G.neighbors(x)))
                if payoff[y]>payoff[x]:
                    proba=(payoff[y]-payoff[x])/((1+r)*max(G.degree(x),G.degree(y)))
                    if (0<=random.uniform(0,1)<=proba):
                        strategy[x]=old_strategy[y]
            fc=(len(G.nodes)-sum(strategy.values()))/len(G.nodes)
        Y.append(fc)
        print("\r {}: {:.2f}, t: {:d}/{:d}, fc: {:.4f}".format(chr(963),sigma,t,T,fc),end="     ")
    plt.plot(X,Y,lw=2.4,color=colors[SIGMA.index(sigma)],label=(chr(963)+"="+str(sigma)))
plt.legend(fontsize=17,loc='best')
plt.xlabel("$t$",fontsize=22)
plt.ylabel("$f_c$",fontsize=22)
plt.xticks(fontsize=22)
plt.yticks(fontsize=22)
plt.ylim([-0.1,1.1])
plt.xlim([1,T+1])
plt.xscale("log")
plt.savefig(".\\saves\\fc_t_SL_SG.pdf",dpi=350)
plt.show()