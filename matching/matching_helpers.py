import numpy as np
import math 
import copy 
import networkx as nx 
import re
from classes import *

#student matching, seat matching, max rank --> matrix
def build_matrix(m_student,m_seat,maxrank):
    matrix = np.zeros((len(m_student),len(m_seat)))
    for i in range(0,len(m_student)):
        if (m_student[i] != -1):
            matrix[i][m_student[i]] = 1
    return matrix

#matrix,edges --> int,int 
def get_metrics(matrix,edges):
    r1 = 0
    r2 = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] == 1):
                if (edges[i][j] == 1):
                    r1 += 1
                elif (edges[i][j] == 2):
                    r2 += 1
    return r1,r2

#matrix --> void 
def remove_k_edges(matrix,n_remove,m_student,k,gedges):
    n_removed = 0
    for i in range(len(matrix)):
        if (n_removed == n_remove):
            return 1
        for j in range(len(matrix[i])):
            if (matrix[i][j] and gedges[i][j] == k):
                matrix[i][j] = 0 
                n_removed += 1
                break 
    return 0


#M <- M ⊕ P
#matrix --> matrix
def symmdiff(matrix,path_s,path_v):
    #First, build a list of edges based on path_s, path_v 
    edges = []
    for i in range(0,len(path_s)):
        for j in range(i - 1,i + 1):
            if (j >= 0 and j < len(path_v)):
                edges.append((path_s[i],path_v[j]))
    for i,j in edges:
        if (matrix[i][j] == 0):
            matrix[i][j] = 1
        else:
            matrix[i][j] = 0


#Checks whether or not the seat is unmatched or not in the matrix
#matrix,seat --> Bool
def aug_path(matrix,seat):
    for i in range(0,len(matrix)):
        if(matrix[i][seat]):
            return False 
    return True


#matrix,student,seat --> void 
def remove_pair(matrix,student,seat):
    matrix[student][seat] = 0


#matrix --> int 
def get_matching_size(m):
    size = 0
    for i in m:
        if (i != -1):
            size += 1
    return size 

# matrix --> list 
def find_unmatched_students(matrix):
    m1, _ = matrix_to_matching(matrix)
    l = []
    for i in range(0,len(m1)):
        if (m1[i] == -1):
            l.append(i)
    return l

#Converts matrix to matching in numpy syntax
def matrix_to_matching(matrix):
    m1 = [-1] * len(matrix)
    m2 = [-1] * len(matrix[0])
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            if (matrix[i][j] == 1):
                m1[i] = j 
                m2[j] = i 
    return m1,m2


#Gets number of rank 1 and rank 2 seats filled in the matching
#Specifc for A-S algorithm, because uses networkx matching
def get_seat_metrics(edges,matching):
    r1 = 0
    r2 = 0
    for left in matching["bridge"]:
        if (matching['bridge'][left] != 0):
            lindex = re.findall("(\d+)",left)[0]
            for edge in matching[left]:
                if(matching[left][edge] != 0):
                    rindex = re.findall("(\d+)",edge)[0]
                    if (edges[int(lindex)][int(rindex)] == 1):
                        r1 += 1
                    elif (edges[int(lindex)][int(rindex)] == 2):
                        r2 += 1
    return r1, r2