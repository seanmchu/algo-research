import networkx as nx 
import numpy as np
import math
import copy
from classes import Student, Seat, Reserve, Graph
import re
from matching_helpers import *

def algo1(students,capacity,reserves,priority):
    # print("Students | types: ")
    # for s in students:
    #     print(f'{s.get_index()} | {s.get_types()}')
    # print(f"Capacity : {capacity}")
    # print("Reserves : Type | Rank | quota limit")
    # for r in reserves:
    #     print(f'{r.get_type()}|{r.get_rank()}|{r.get_cap()}')
    # print("Priority ordering of students (index)")
    # print(priority)
    g = Graph(students,reserves)
    g.build_rrg()
    edge_copy = copy.deepcopy(g.edges)
    # print("ranked_reservation_graph (non adj edges denoted as rank maxrank+1 edges)")
    # print(g.edges)
    selected = []
    #order by priority
    p_students = [] 
    for p in priority:
        for s in students:
            if (s.get_index() == p):
                p_students.append(s)
    if (g.edges.size == 0):
        for s in p_students:
            if (len(selected) == capacity):
                break
            if (s not in selected):
                selected.append(s)
    
    selected = []
    n_sel = 0
    g.build_rank_weight_graph()
    #We find the max cost possible for the graph with the capacity constraints
    #print(g.edges)
    maxcost = g.maxcost(capacity)
    #print(f'Maximal capacity matching signature cost: {maxcost}')
    #Check if we can add the student each time 
    #We create a copy version of the graph so we can add our special weights
    r1_seats = 0
    r2_seats = 0
    for s in p_students:
        if (len(selected) >= capacity):
            break
        g_copy = copy.deepcopy(g)
        #Add special weights to all v in S*
        for v in selected:
            g_copy.addspecialweight(v)
        #add the special weight to s  
        g_copy.addspecialweight(s)
        #print(g_copy.edges)
        tempmatching, matching_size = g_copy.maxflow(capacity)
        #print(tempmatching,matching_size)
        if (matching_size < len(selected) + 1):
            continue
        #Now we have to match the capacity to the flow cost 
        truecost = g.truecost(tempmatching)
        #print(f'Matching signature cost if student {s.index} is added: {truecost}')
        if (truecost == maxcost):
            selected.append(s)
            r1_seats, r2_seats = get_seat_metrics(edge_copy,tempmatching)
    for s in p_students:
        if (len(selected) == capacity):
            break
        if (s not in selected):
            selected.append(s)
    sl = []
    for s in selected:
        sl.append(s.index)
    
    #We simply check which seats are matched in the rrg
    return sl, r1_seats,r2_seats

        
    
def example_1():
    s1 = Student(1,[])
    s2 = Student(2,[4])
    s3 = Student(3,[3])
    s4 = Student(4,[1,2,3])
    s5 = Student(5,[1])
    s6 = Student(6,[2,3])

    plist = [1,2,3,4,5,6]
    r1 = Reserve(1,1,1) 
    r2 = Reserve(2,1,1)
    r3 = Reserve(3,2,1)
    r4 = Reserve(4,2,1)
    cap = 3
    all_students = [s1,s2,s3,s4,s5,s6]
    all_reserves = [r1,r2,r3,r4]
    sel,r1_seats,r2_seats = algo1(all_students,cap,all_reserves,plist)
    sel.sort()
    print(f"Algo 1 selected students: {sel}")
    print(f"Rank 1 seats filled: {r1_seats}")
    print(f"Rank 2 seats filled: {r2_seats}")
    print(f"Unreserved entries: {cap - r1_seats - r2_seats}")
if __name__ == "__main__":
    example_1()


    