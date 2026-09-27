# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 17:04:41 2021
Evolutionary games with stochastic payoff
WPD
Square Lattices
@author: 86150
"""
import networkx as nx
import numpy as np
import random
import copy
import json
#参数列
b=1.03#博弈参数
B=np.arange(1,1.2,0.02)
T=10000#最大迭代时间
N=1000#网络规模，对随机网络
L=50#正则格子宽度
sigma=0.3#正态分布标准差
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
def get_all_payoff(G,strategy,b,sigma):
    payoff={}
    for i in G.nodes:
        i_payoff=0
        if strategy[i]==0:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.normal(1,sigma)
        elif strategy[i]==1:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.normal(b,sigma)
        payoff[i]=i_payoff
    return payoff
#初始化
G=square_lattice(L)#正则格子
#G=nx.barabasi_albert_graph(N,4)
Result={}
Std={}
for sigma in SIGMA:
    Fc=[]
    STD=[]
    for b in B:
        Y=[]
        strategy={}
        for i in G.nodes:
            strategy[i]=int(0<=random.uniform(0,1)<=0.5)
        fc=(len(G.nodes)-sum(strategy.values()))/len(G.nodes)
        Y.append(fc)
        for t in range(T):
            if (0<fc<1):
                payoff=get_all_payoff(G,strategy,b,sigma)
                old_strategy=copy.deepcopy(strategy)
                for x in G.nodes:
                    y=random.choice(list(G.neighbors(x)))
                    if payoff[y]>payoff[x]:
                        proba=(payoff[y]-payoff[x])/((b)*max(G.degree(x),G.degree(y)))
                        if (0<=random.uniform(0,1)<=proba):
                            strategy[x]=old_strategy[y]
                fc=(len(G.nodes)-sum(strategy.values()))/len(G.nodes)
            Y.append(fc)
            print("\r {}: {:.2f}, b: {:.2f}, t: {:d}/{:d}, fc: {:.4f}".format(chr(963),sigma,b,t,T,fc),end="     ")
        Fc.append(np.mean(Y[T-1000:]))
        STD.append(np.std(Y[T-1000:]))
    Result["{:.2f}".format(sigma)]=Fc
    Std["{:.2f}".format(sigma)]=STD
json_str=json.dumps(Result)
with open('.\\saves\\fc_b_SL_PD.json', 'w') as json_file:
    json_file.write(json_str)
json_str2=json.dumps(Std)
with open('.\\saves\\std_b_SL_PD.json', 'w') as json_file:
    json_file.write(json_str2)