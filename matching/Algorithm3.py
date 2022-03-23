#Algorithm 3
#TODO: Ask Haris about problems since not sure why stuff isn't working for the current example included here
from classes import *
import copy
from matching_helpers import *
def build_matrix(m_student,m_seat):
    matrix = np.zeros((len(m_student),len(m_seat)))
    for i in range(0,len(m_student)):
        if (m_student[i] != -1):
            matrix[i][m_student[i]] = 1
    return matrix
def algo3(g,capacity):
    g1 = copy.deepcopy(g)
    m1,m2,a = g1.maxmatching(1)    
    matrix = build_matrix(m1,m2)
    print(matrix)
    if (len(g1.edges) == 0):
        return [],[],[],0
    i = 1
    for i in range(1,g1.maxrank):
        E_stu,O_stu,U_stu,E_sea,O_sea,U_sea = g1.dulmen(i,m1,m2)
        #print(E_stu,O_stu,U_stu,E_sea,O_sea,U_sea)
        #Delete all edges incident to nodes in O,U in higher ranks
        #Student side
        for j in range(0,len(m1)):
            if (j in O_stu or j in U_stu):
                for k in range(0,len(g1.edges[j])):
                    if (g1.edges[j][k] > i): #If rank of edge > i
                        g1.edges[j][k] = g1.maxrank + 1
        #Seat side
        for j in range(0,len(m2)):
            if (j in O_sea or j in U_sea):
                for k in range(0,len(g1.edges)):
                    if (g1.edges[k][j] > i):
                        g1.edges[k][j] = g1.maxrank + 1
        #Delete all edges in OO, OU in rank i graph
        #Delete OO edges
        for j in range (0,len(O_stu)):
            odd_student = O_stu[j]
            for k in range(0,len(O_sea)):
                odd_seat = O_sea[k]
                if (g1.edges[odd_student][odd_seat] == i):
                    g1.edges[odd_student][odd_seat] = g1.maxrank + 1 
        #Delete OU edges 
        #O student, U seat
        for j in range (0,len(O_stu)):
            odd_student = O_stu[j]
            for k in range(0,len(U_sea)):
                unmatched_seat = U_sea[k]
                if (g1.edges[odd_student][unmatched_seat] == i):
                    g1.edges[odd_student][unmatched_seat] = g1.maxrank + 1 
        #U student, O seat
        for j in range (0,len(U_stu)):
            unmatched_student = U_stu[j]
            for k in range(0,len(O_sea)):
                odd_seat = O_sea[k]
                if (g1.edges[unmatched_student][odd_seat] == i):
                    g1.edges[unmatched_student][odd_seat] = g1.maxrank + 1 
        size = get_matching_size(m1)
        if (size >= capacity):
            return g1,m1,m2,i
        else:
            #Obtain G_i+1 by adding edges E_i+1 to G_i --> done by for loop
            unmatch_students = find_unmatched_students(matrix)
            s_aug_path,v_aug_path, found = g1.find_augmenting_path(matrix,unmatch_students, i + 1)
            while (found):
                symmdiff(matrix,s_aug_path,v_aug_path)
                unmatch_students = find_unmatched_students(matrix)
                s_aug_path,v_aug_path, found = g1.find_augmenting_path(matrix,unmatch_students, i + 1)
            m1,m2 = matrix_to_matching(matrix)
    print("Reached end")
    return g1,m1,m2,i


def example():
    #Setup example
    s1 = Student(1,[1,3])
    s2 = Student(2,[4])
    s3 = Student(3,[1,3,4])
    s4 = Student(4,[1,3,4])
    plist = [1,2,3,4]
    r1 = Reserve(1,3,0)
    r2 = Reserve(2,2,0) 
    r3 = Reserve(3,2,2)
    r4 = Reserve(4,2,2)
    r5 = Reserve(5,3,0)
    capacity = 3
    all_students = [s1,s2,s3,s4]
    all_reserves = [r1,r2,r3,r4,r5]
    g = Graph(all_students,all_reserves)
    #Build rrg and get maximal matching prior to DMD
    g.build_rrg()
    #print(f'Initial graph: \n{g.edges}')
    final_graph, m1,m2,i = algo3(g,capacity)
    print(f"Max rank reached is {i}")
    print(f'Final Graph (After removing required edges): \n{final_graph.edges}')
    print(f'Final matching |\n {build_matrix(m1,m2)}')
    #print(f'Matching (student side): {matching_student} | Matching (seat side): {matching_seat}')
if __name__ == "__main__":
    example()
