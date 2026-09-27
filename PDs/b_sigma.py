# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 17:04:41 2021
Evolutionary games with stochastic payoff
SG
Square Lattices
@author: 86150
"""
import networkx as nx
import numpy as np
import random
import copy
import json
#参数列
network_type="TL"
B=np.arange(1,1.21,0.01)
#B=np.arange(1,1.42,0.02)#SW
T=5000#最大迭代时间
SIGMA=np.arange(0.05,1.1,0.05)
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
                if strategy[nei]==1:
                    i_payoff+=np.random.normal(0,sigma)
        elif strategy[i]==1:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.normal(b,sigma)
                if strategy[nei]==1:
                    i_payoff+=np.random.normal(0,sigma)
        payoff[i]=i_payoff
    return payoff
#初始化
if network_type=="SL":
    G=square_lattice(50)#正则格子
if network_type=="SW":
    G=nx.watts_strogatz_graph(2500,4)
if network_type=="TL":
    G=nx.generators.lattice.triangular_lattice_graph(70,70,periodic=True)
if network_type=="HL":
    G=nx.generators.lattice.hexagonal_lattice_graph(36,36,periodic=True)
Result={}
for sigma in SIGMA:
    Fc=[]
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
    Result["{:.2f}".format(sigma)]=Fc
json_str=json.dumps(Result)
with open('.\\saves\\b_sigma_{}.json'.format(network_type), 'w') as json_file:
    json_file.write(json_str)