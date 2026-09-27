"""
Created on Fri Nov 26 17:04:41 2021
Evolutionary games with stochastic payoff
On Snowdrift Games With The Parameter r
r=0.2 0.5 0.8
\sigma=0.1 0.3 0.7 0.9
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
R=[0.25,0.35,0.45,0.55]
T=5000#最大迭代时间
L=50
def get_all_payoff(G,strategy,r):
    payoff={}
    for i in G.nodes:
        i_payoff=0
        if strategy[i]==0:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.exponential(1)
                if strategy[nei]==1:
                    i_payoff+=np.random.exponential(1-r)
        elif strategy[i]==1:
            for nei in G.neighbors(i):
                if strategy[nei]==0:
                    i_payoff+=np.random.exponential(1+r)
                if strategy[nei]==1:
                    i_payoff+=np.random.exponential(0)
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
G=nx.generators.lattice.grid_graph((L,L),periodic=True)#正则格子
for r in R:
    strategy={}
    for i in G.nodes:
        strategy[i]=int(0<=random.uniform(0,1)<=0.5)
    for t in range(T):
        payoff=get_all_payoff(G,strategy,r)
        old_strategy=copy.deepcopy(strategy)
        for x in G.nodes:
            y=random.choice(list(G.neighbors(x)))
            if payoff[y]>payoff[x]:
                proba=(payoff[y]-payoff[x])/((1+r)*max(G.degree(x),G.degree(y)))
                if (0<=random.uniform(0,1)<=proba):
                    strategy[x]=old_strategy[y]
        print("\r r: {:.2f}, t: {:d}/{:d}".format(r,t,T),end="     ")
        if (sum(strategy.values())==2500 or sum(strategy.values())==0):
            break
    cell=snapshot(strategy,G)
    plt.imshow(cell,cmap=plt.cm.Blues_r)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(".\\saves\\SGexponential{:.2f}.pdf".format(r),dpi=400)
    plt.show()