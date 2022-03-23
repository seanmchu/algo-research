import numpy as np
import copy
import math

#faster than numpy provided integers aren't large enough for overflow
def norm(a,b):
    n = 0
    for i in range(a.shape[0]):
        n = n + (a[i] - b[i])**2 
    #print(n)
    n = math.sqrt(n)
    return n

def approx_prf(agents,k):
    delta_counter = 0
    Y = np.zeros((0,agents.shape[1])) 
    N = copy.deepcopy(agents)
    n = agents.shape[0]
    M = copy.deepcopy(agents)
    #D = {d(i,j)|i,j \in N}
    distances = []
    for i in range(0,len(agents)):
        for j in range(i + 1,len(agents)):
            distances.append(norm(agents[i],agents[j]))
    distances.sort()
    
    #First axis is for M (prospective centroids), second axis is for N (points)
    dd = []
    for i in range(0,len(agents)):
        dd.append([])
    for i in range(0,len(agents)):
        for j in range(0,len(agents)):
            dd[i].append(norm(agents[i],agents[j]))
    #sort D
    distances.sort()
    while N.size != 0 and delta_counter < len(distances) and Y.shape[0] < k:
        #Smoothly increase delta 
        delta = distances[delta_counter]
        #print(f"beginning run, delta is {delta}")
        #Remove all elements of N in a delta ball around every Y (centroids)
        nshape = N.shape[0]
        #First while loop (check all y and x )
        for i in range(Y.shape[0]):
            for j in range(nshape):
                if (j >= nshape):
                    break
                if (norm(Y[i],N[j]) <= delta):
                    N = np.delete(N,j,axis = 0)
                    nshape -= 1
                    for a in range(0,len(dd)):
                        del(dd[a][j])
        for i in range(M.shape[0]):
            ball = []
            if (i >= M.shape[0]):
                break
            #Find indices of elements in ball 
            for j in range(N.shape[0]):
                if (dd[i][j] <= delta):
                    ball.append(j)
            nshape = N.shape[0]
            if (len(ball) >= math.ceil(nshape/k)):
                #Append x to Y
                Y = np.vstack([Y,M[i]])
                if (Y.shape[0] > k):
                    break
                ball.sort(reverse=True)
                for b in ball:
                    if (b < N.shape[0]):
                        N = np.delete(N,b,axis=0)
                M = np.delete(M,i,axis = 0)
                del (dd[i])
                for i in range(0,len(dd)):
                    for b in ball:
                        if (b < len(dd[i])):
                            del(dd[i][b])
                        else:
                            del(dd[i][len(dd[i])-1])
        if (Y.shape[0] > k):
            break
        delta_counter += 1
    for j in range(M.shape[0]):
        if (Y.shape[0] >= k):
            break
        Y = np.vstack([Y,M[j]])
    return Y 

    
if __name__ == "__main__":
    print('running approx prf')
    n = np.array([[10,0],[10,0],[0,10],[0,0]])
    print(f"y is {approx_prf(n,3)}")