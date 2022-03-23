import numpy as np
import copy
import math
from sklearn.cluster import kmeans_plusplus
#Implementation of Algorithm 1: an algorithm for unconstrained clustering satisfying PRF
def kprf(agents, k):
    #input parameters are- agents: the multiset of $n$ data points that we cluster on (numpy array), k: |clusters|, $\chi$ can be found by doing dim(agents)
    #return value
    W = []
    #w <- 1 \forall N
    weights = []
    for i in agents:
        weights.append(1)  
    #D = {d(i,j)|i,j \in N}
    distances = []
    for i in range(0,len(agents)):
        for j in range(i + 1,len(agents)):
            distances.append(np.linalg.norm(agents[i]-agents[j]))
    distances.sort()
    #M = {c_i^1,\cdots,c_i^1}
    M = copy.deepcopy(agents)
    j = 0
    cstar = []
    distances2 = []
    for i in range(0,M.shape[0]):
        distances2.append([])
        for a in range(0,agents.shape[0]):
            distances2[i].append(np.linalg.norm(M[i]-agents[a]))
    while (len(W) < k and j < len(distances)):
        cstar = np.empty((0,len(agents[0])))
        cstar_weights = []
        cindices = []
        cstar_list = []
        agent_len = len(distances2[0])
        for c in range(0,len(distances2)):
            if (c >= len(distances2)):
                break
            total_weight = 0
            for i in range(0,agent_len):
                if (distances2[c][i] <= distances[j]):
                    total_weight += weights[i] 
            if (total_weight + 0.001 >= (agents.shape[0]/k)):
                cstar_weights.append(total_weight)
                cstar_list.append(M[c])
                cindices.append(c)
        cstar = np.array(cstar_list)
        if (cstar.shape[0] == 0):
            j += 1
        else:
            #Extract candidate with greatest weighting
            maxweight = max(cstar_weights)
            mindex = cstar_weights.index(maxweight)
            W.append(cstar[mindex])
            M = np.delete(M,cindices[mindex],axis = 0)
            del(distances2[cindices[mindex]])
            #agent_len = agent_len - 1 
            #we want to modify the weights such that all voters of distance \leq d_j from the new centroid has their total weight reduced by n/k
            redis = 0
            for i in range(0,agents.shape[0]):
                if (np.linalg.norm(agents[i]-cstar[mindex]) <= distances[j]):
                    redis += 1
            for i in range(0,agents.shape[0]):
                if (np.linalg.norm(agents[i]-cstar[mindex]) <= distances[j]):
                    weights[i] -= (agents.shape[0]/(k * redis))
    return W 

def within(a,b):
    for i in a:
        if (np.all(np.equal(i,b))):
            return True 
    return False

def norm(a,b):
    n = 0
    for i in range(a.shape[0]):
        n = n + (a[i] - b[i])**2 
    n = math.sqrt(n)
    return n


if __name__ == "__main__":
    print('running kprf')
    n = np.array([[0,0],[0,10],[10,0],[10,0],[10,0],[10,0],[5,5],[3,3],[1,1],[-1.4,1.98],[-20,-40]])
    print(kprf(n,3))

