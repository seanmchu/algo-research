import networkx as nx 
import numpy as np
import math
import copy
import matplotlib.pyplot as plt
import re
from scipy.sparse.csgraph import maximum_bipartite_matching
from scipy.sparse import csr_matrix
class Student(object):
    def __init__(self,index,types):
        self.index = index
        self.eindex = -1
        self.types = types
        self.sat = 0
    def get_types(self):
        return self.types 
    def get_index (self):
        return self.index  

class Seat(object):
    def __init__(self,index,t,rank):
        self.index = index 
        self.t = t 
        self.rank = rank 
    def get_type(self):
        return self.t 
    def get_rank(self):
        return self.rank
    def get_index(self):
        return self.index

#Will be translated to seats to be put into graph
class Reserve(object):
    #t = type, rank = rank, cap = capacity
    def __init__(self,t,rank,cap):
        self.t = t
        self.rank = rank 
        self.cap = cap 
    def get_type(self):
        return self.t
    def get_rank(self):
        return self.rank 
    def get_cap(self):
        return self.cap

class Graph(object):
    def __init__(self,students,reserves,edges = {}):
        self.students = students 
        self.reserves = reserves
        self.seats = []
        self.edges = []
        self.maxrank = 0
        ind = 0
        for r in self.reserves:
            for i in range(0,r.get_cap()):
                if (r.get_rank() > self.maxrank):
                    
                    self.maxrank = r.get_rank()
                s = Seat(ind,r.get_type(),r.get_rank())
                self.seats.append(s)
                ind += 1 
        self.edges = edges 
    def add_student(self,student):
        self.students.append(student)
    def remove_student(self,student):
        self.students.remove(student)
    def build_rrg(self):
        #reset any existing edges 
        self.edges = np.zeros((len(self.students),len(self.seats)))
        sindex = 0
        for s in self.students:
            vindex = 0
            #So we know which student has which edge index
            s.eindex = sindex
            for v in self.seats:
                if (v.get_type() in s.get_types()):
                    self.edges[sindex][vindex] = v.get_rank()
                else:
                    self.edges[sindex][vindex] = self.maxrank + 1
                vindex += 1
            sindex += 1
    #Convert rank to weight 
    def build_rank_weight_graph(self):
        v = len(self.students) + len(self.seats)
        for i in range(0,len(self.edges)):
            for j in range(0,len(self.edges[i])):
                self.edges[i][j] = pow(2,math.ceil(math.log(v)) * (self.maxrank - self.edges[i][j]))
    #use after having a rank weight graph to add the special weight for already included vertices
    def addspecialweight(self,student):
        i = 0
        for v in self.edges[student.eindex]:
            specweight = pow(2,math.ceil(math.log(abs(len(self.students) + len(self.seats))) * (self.maxrank + 1)))
            self.edges[student.eindex][i] += specweight 
            i += 1
        
    #Find max cost associated with a matching of a given size
    #Done using max flow min cost and negative weights
    def maxcost(self,size):
        G = nx.DiGraph()
        G.add_node("source",demand = - size)
        G.add_edge("source","bridge",weight = 0, capacity = size)
        G.add_edge("xbridge","sink",weight = 0)
        G.add_node("sink", demand = size)
        i = 0
        for e in self.edges:
            G.add_edge("bridge","left" + str(i),weight = 0, capacity = 1)
            i += 1
        j = 0 
        for e in self.edges: 
            k = 0
            for v in e:
                G.add_edge("left" + str(j), "right" + str(k), weight = - v, capacity = 1)
                G.add_edge("right" + str(k), "xbridge", weight = 0, capacity = 1)
                k += 1 
            j += 1
        #print(f'G is {G}')
        return - nx.cost_of_flow(G,nx.max_flow_min_cost(G,"source","sink"))
    #As above, but returns the dict giving the min cost graph
    def maxflow(self,size):
        G = nx.DiGraph()
        G.add_node("source",demand = - size)
        G.add_edge("source","bridge",weight = 0, capacity = size)
        G.add_edge("xbridge","sink",weight = 0)
        G.add_node("sink", demand = size)
        i = 0
        for e in self.edges:
            G.add_edge("bridge","left" + str(i),weight = 0, capacity = 1)
            i += 1
        j = 0 
        for e in self.edges: 
            k = 0
            for v in e:
                G.add_edge("left" + str(j), "right" + str(k), weight = - v, capacity = 1)
                G.add_edge("right" + str(k), "xbridge", weight = 0, capacity = 1)
                k += 1 
            j += 1
        maxx = nx.max_flow_min_cost(G,"source","sink")
        matching_size = 0
        for i in maxx["bridge"]:
            if (maxx["bridge"][i] == 1):
                matching_size += 1
        return maxx, matching_size

    #Takes in a dictionary of edges (from maxflow) and returns the cost of matching if these edges are used
    def truecost (self,seledges):
        cost = 0
        for left in seledges['bridge']:
            if (seledges['bridge'][left] != 0):
                lindex = re.findall("(\d+)",left)[0]
                for edge in seledges[left]:
                    if (seledges[left][edge] != 0):
                        rindex = re.findall("(\d+)",edge)[0]
                        #print(lindex,rindex)
                        cost += self.edges[int(lindex)][int(rindex)]
        return cost
    def adjacent (self,a,b,rank):
        if (self.edges[a][b] <= rank and self.edges[a][b] != 0):
            return True 
        else:
            return False
    #Returns any maximum matching of itself
    def maxmatching(self,rank):
        #Create an adjacency matrix of 1 rank
        translated_matrix = self.edges.copy()
        i = 0
        for e in translated_matrix:
            j = 0
            for v in e:
                if (v > rank):
                    translated_matrix[i][j] = 0
                else:
                    translated_matrix[i][j] = 1
                j += 1
            i += 1
        g = csr_matrix(translated_matrix)
        #print(g)
        #Use Scipy's maximum bipartite matching algorithm, which is O(|E|sqrt(|V|))
        m1 = maximum_bipartite_matching(g,perm_type= "column")
        m2 = maximum_bipartite_matching(g,perm_type= 'row')
        return m1,m2,translated_matrix
    #Dulmage mendelsohn decomposition on self
    def dulmen(self,rank,m1,m2):
        #Get a maximum matching
        #Now we go through alternating paths based on the V0 in order to get our EUO decomposition
        #first we need V0
        unmatched_students = []
        unmatched_seats = []
        i = 0
        for student in m1:
            if (student == -1):
                unmatched_students.append(i)
            i += 1
        i = 0
        for seat in m2:
            if (seat == -1):
                unmatched_seats.append(i)
            i += 1
        #print(unmatched_students,unmatched_seats)
        #print(f'Students in V0: {unmatched_students} , Seats in V0: {unmatched_seats}')
        #Implementation is simpler to split our EUO parititions into students and seats because
        #Our Seats and Students are only indexed within their respective sets
        E_stu = []
        O_stu = []
        U_stu = []
        E_sea = []
        O_sea = []
        U_sea = []
        #Populate E,O of student and seat appropriately 
        for student in unmatched_students:
            E_stu.append(student)
            self.dfs(student,rank,E_stu,O_stu,E_sea,O_sea,m1,m2,True,0)
        for seat in unmatched_seats:
            E_sea.append(seat)
            self.dfs(seat,rank,E_stu,O_stu,E_sea,O_sea,m1,m2,False,0)
        #Populate U of student and seat 
        for i in range(0,len(self.edges)):
            if (i not in E_stu and i not in O_stu):
                U_stu.append(i)
        for i in range(0,len(self.edges[0])):
            if (i not in E_sea and i not in O_sea):
                U_sea.append(i)
        return E_stu,O_stu,U_stu,E_sea,O_sea,U_sea
    #dfs for Dulmage mendelsohn decomposition
    #Naturally, if looking for odd reachable, we are looking for unmatched edges to traverse (since first movement will be along unmatched)
    #and if we are looking for even reachable, we are looking for matched edges to traverse
    def dfs(self,ind,rank,Estu,Ostu,Esea,Osea,stumatch,seamatch,student,length):
        if (length == len(self.edges) + len(self.edges[0])):
            return
        if (length%2 == 0):
            if (student):
                #Students can only be adjacent to seats in the matching
                for i in range(0,len(self.edges[ind])):
                    #Since odd length, we are looking for adjacent but not matched
                    if (self.adjacent(ind,i,rank) and (stumatch[ind] != i) and i not in Osea):
                        Osea.append(i)
                        self.dfs(i,rank,Estu,Ostu,Esea,Osea,stumatch,seamatch,False,length + 1)
            else:
                for i in range(0,len(self.edges)):
                    if (self.adjacent(i,ind,rank) and (seamatch[ind] != i) and i not in Ostu):
                        Ostu.append(i)
                        self.dfs(i,rank,Estu,Ostu,Esea,Osea,stumatch,seamatch,True,length + 1)
        else:
            if (student):
                for i in range(0,len(self.edges[ind])):
                    if (self.adjacent(ind,i,rank) and (stumatch[ind] == i) and i not in Esea):
                        Esea.append(i)
                        self.dfs(i,rank,Estu,Ostu,Esea,Osea,stumatch,seamatch,False,length + 1)
            else:
                for i in range(0,len(self.edges)):
                    if (self.adjacent(i,ind,rank) and (seamatch[ind] == i) and i not in Estu):
                        Estu.append(i)
                        self.dfs(i,rank,Estu,Ostu,Esea,Osea,stumatch,seamatch,True,length + 1)
    
    #Determine if there exists an alternating path from s and ends at s′ ∈ S \S ∗, returns path
    #Change to only return paths that are able to satisfy requirements
    def find_special_alt_path(self,s1,sett,match,depth,path_s,path_v,start_s,special_type = False):
        #print (f"s1 is currently {s1}, sett is {sett}, depth is {depth}")
        depth += 1
        #student
        index = int(s1)
        ps = copy.deepcopy(path_s)
        pv = copy.deepcopy(path_v)
        if (depth % 2):
            ps.append(int(s1))
            if ( (s1 + 1) not in sett and start_s != s1):
                return ps,pv
            matches = 0
            for i in range(0,len(self.edges[0])):
                if (self.edges[index][i] <= self.maxrank and i not in pv and match[index][i] == 0):
                    matches += 1 
            if (matches == 0):
                #end of path (use + 1 because sett is not 0 indexed)
                if ( (s1 + 1) not in sett):
                    return ps,pv
                else:
                    return [],[]    
            found = 0
            for i in range(0,len(self.edges[0])):   
                if (self.edges[index][i] <= self.maxrank  and i not in path_v and match[index][i] == 0):
                    pss,pvv = self.find_special_alt_path(int(i),sett,match,depth,ps,pv,start_s,special_type)
                    if (pss != []):
                        found = 1
                if (found): #found type 1 
                    break
        #seat
        else:
            pv.append(int(s1))
            
            matches = 0
            for i in range(0,len(self.edges)):
                if(self.edges[i][index] <= self.maxrank and i not in ps and match[i][index] != 0):
                    matches += 1
            #If there are no matches, it means that the seat is unmatched --> augmenting path
            if (matches == 0):
                if ( special_type ): #Fits our second criterion
                    rank = self.seats[s1].rank 
                    if (self.find_redundant_student(sett,rank,match)[1] != -1):
                        return ps,pv 
                    else:
                        return [],[]
                else:
                    return [],[]
            found = 0
            for i in range(0,len(self.edges)):
                if(self.edges[i][index] <= self.maxrank and i not in ps and match[i][index] != 0):
                    pss,pvv = self.find_special_alt_path(int(i),sett,match,depth,ps,pv,start_s,special_type)
                    if(ps != []):
                        found = 1
                if (found):
                    break
        return pss,pvv
    #
    def find_redundant_student(self,s,rank,matrix):
        for i in range(0,len(self.edges)):
            if ((i+1) not in s):
                for j in range(0,len(self.edges[0])):
                    if(matrix[i][j] and self.edges[i][j] == rank):
                        return i,j
        return -1,-1
    
    def find_augmenting_path(self,matrix,unmatched_students,maxrank):
        for i in unmatched_students:
            path_s,path_v = self.find_aug_path(i,matrix,0,[],[],maxrank) 
            if (path_s != []):
                return path_s, path_v, True
        return [],[],False

    def find_aug_path(self,s1,match,depth,path_s,path_v,maxrank):
        depth += 1
        #print(f"Maxrank is {maxrank}")
        #student
        #print(depth,path_s,path_v)
        ps = copy.deepcopy(path_s)
        pv = copy.deepcopy(path_v)
        index = int(s1)
        if (depth % 2):
            ps.append(int(s1))
            matches = 0
            for i in range(0,len(self.edges[0])):
                if (self.edges[index][i] <= maxrank and i not in pv and match[index][i] == 0):
                    matches += 1
            if (matches == 0):
                #end of path --> not augmenting since we end on a student
                return [], []
            found = 0
            for i in range(0,len(self.edges[0])):   
                if (self.edges[index][i] <= maxrank and i not in pv and match[index][i] == 0):
                    #print(index)
                    #print(i)
                    #print(maxrank)
                    pss,pvv = self.find_aug_path(int(i),match,depth,ps,pv,maxrank)
                    if (pss != []):
                        found = 1
                if (found):
                    break
        #seat
        else:
            pv.append(int(s1))
            matches = 0
            for i in range(0,len(self.edges)):
                if(self.edges[i][index] <= maxrank and i not in ps and match[i][index] != 0):
                    matches += 1
            #If there are no matches, it means that the seat is unmatched, and we end on an unmatched seat
            if (matches == 0):
                return ps,pv
            found = 0
            for i in range(0,len(self.edges)):
                if(self.edges[i][index] <= maxrank and i not in ps and match[i][index] != 0):
                    pss,pvv = self.find_aug_path(int(i),match,depth,ps,pv,maxrank)
                    if(pss != []):
                        found = 1
                if (found):
                    break
        return pss,pvv
