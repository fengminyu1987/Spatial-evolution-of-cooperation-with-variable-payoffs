"""
Created on Fri Nov 26 17:04:41 2021
Evolutionary games with stochastic payoff
On Weak Prisoner's Dilemmas With The Parameter b
b=1.03 1.06 1.09
\sigma=0.1 0.3 0.7 0.9
@author: 86150
"""
import networkx as nx
import numpy as np
import random
import copy
import matplotlib.pyplot as plt
import warnings
import json
warnings.filterwarnings("ignore")
#参数列#博弈参数
B=[1.03]
T=5000#最大迭代时间
comm=4500
L=50
NT=['HL','SL','SW','TL']
def get_all_payoff(G,strategy,b):
    payoff={}
    for i in G.nodes:
        i_payoff=0
        if strategy[i]==0:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.exponential(1)
                if strategy[nei]==1:
                    i_payoff+=np.random.exponential(1e-10)
        elif strategy[i]==1:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.exponential(b)
                if strategy[nei]==1:
                    i_payoff+=np.random.exponential(1e-10)
        payoff[i]=i_payoff
    return payoff
def snapshot(strategy,G):
    result=[]
    for i in range(L):
        temp=[]
        for j in range(L):
            temp.append(strategy[(i,j)])
        result.append(temp)
    return result
#初始化
payoffdatas={}
for network_type in NT:
    if network_type=='SL':
        G=nx.generators.lattice.grid_graph((L,L),periodic=True)#正则格子
    if network_type=="SW":
        G=nx.watts_strogatz_graph(2500,8,0.4)
    if network_type=="TL":
        G=nx.generators.lattice.triangular_lattice_graph(70,70,periodic=True)
    if network_type=="HL":
        G=nx.generators.lattice.hexagonal_lattice_graph(36,36,periodic=True)
    for b in B:
        payofflist=np.zeros(len(G.nodes))
        counter=0
        strategy={}
        for i in G.nodes:
            strategy[i]=int(0<=random.uniform(0,1)<=0.5)
        for t in range(T):
            payoff=get_all_payoff(G,strategy,b)
            old_strategy=copy.deepcopy(strategy)
            for x in G.nodes:
                y=random.choice(list(G.neighbors(x)))
                if payoff[y]>payoff[x]:
                    proba=(payoff[y]-payoff[x])/(b*max(G.degree(x),G.degree(y)))
                    if (0<=random.uniform(0,1)<=proba):
                        strategy[x]=old_strategy[y]
            print("\r b: {:.2f}, t: {:d}/{:d}".format(b,t,T),end="     ")
            if (sum(strategy.values())==2500 or sum(strategy.values())==0):
                break
            if (t>comm):
                payofflist+=list(payoff.values())
                counter+=1
        payoffdatas[network_type]=list(payofflist/counter)
json_str=json.dumps(payoffdatas)
with open('.\\saves\\PD_Exponential.json', 'w') as json_file:
    json_file.write(json_str)