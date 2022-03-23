from Algorithm3 import algo3 
from classes import *
from matching_helpers import *

def algo4(students,capacity,priority,reserves):
    g = Graph(students,reserves)
    g.build_rrg()
    g_matching, match_student, match_seat,k = algo3(g,capacity) #pruned reservation graph and matchings
    matrix = build_matrix(match_student,match_seat,g.maxrank)
    matching_size = 0
    for i in range(0,len(match_student)):
        if (match_student[i] != -1):
            matching_size += 1 
    n_remove = matching_size - capacity 
    print(matrix)
    print(f'n_remove is {n_remove}, k is {k}')
    #Remove first |M| - q edges in graph
    if (n_remove > 0):
        if(remove_k_edges(matrix,n_remove,match_student,k+1,g.edges) == 0):
            remove_k_edges(matrix,n_remove,match_student,k,g.edges)
    print(g.edges)
    #S* <- {} 
    s = []
    for i in priority: 
        print(i,matrix)
        p_student,p_seat = g_matching.find_special_alt_path(i - 1,s,matrix,0,[],[],i-1)
        p_student_2,p_seat_2 = g_matching.find_special_alt_path(i-1,s,matrix,0,[],[],i-1,True)
        print("p_student,p_seat")
        print(p_student,p_seat)
        print(p_student_2,p_seat_2)
        cond_1 = False 
        cond_2 = False 
        if (len(p_student) > 1 and len(p_student) > len(p_seat) and (p_student[-1] + 1) not in s):
            print("condition one true")
            cond_1 = True
        #TODO: Have to search through every augmenting path because first one won't always have a swappable seat even though it may exist 
        elif ( (len(p_student_2) > 0 and len(p_student_2) == len(p_seat_2) and aug_path(matrix,p_seat_2[-1]))):
            print("condition 2 true")
            cond_2 = True
            rank = g.edges[p_student_2[len(p_student_2) - 1]][p_seat_2[len(p_seat_2) - 1]]
            student,seat = g_matching.find_redundant_student(s,int(rank),matrix)
        done = 0
        #If s is matched in m
        for j in range(0,len(matrix[i-1])):
            if (matrix[i-1][j] == 1):
                s.append(i)
                done = 1
                break
        if (done):
            continue
        elif (cond_1):
            s.append(i)
            symmdiff(matrix,p_student,p_seat)
        elif (cond_2 and student != -1):
            print("Condition 2 actually true")
            print(student)
            s.append(i)
            symmdiff(matrix,p_student_2,p_seat_2)
            student,seat = g_matching.find_redundant_student(s,int(rank),matrix)
            if (student != -1):    
                remove_pair(matrix,student,seat)
            else:
                symmdiff(matrix,p_student,p_seat) 
                s.remove(i)   
    for i in priority:
        if (len(s) < capacity and i not in s):
            print(f"appending {i}")
            s.append(i)

    #Get rank 1 and rank 2 seat metrics
    r1 = 0 
    r2 = 0
    r1,r2 = get_metrics(matrix,g.edges)

    return s,r1,r2

def example_1():
    s1 = Student(1,[1,5])
    s2 = Student(2,[])
    s3 = Student(3,[1,4,5])
    s4 = Student(4,[2,5])
    plist = [1,2,3,4]
    r1 = Reserve(1,1,1)
    r2 = Reserve(1,2,3) 
    r3 = Reserve(2,1,1)
    cap = 3
    all_students = [s1,s2,s3,s4]
    all_reserves = [r1,r2,r3]
    sel,r1_seats,r2_seats = algo4(all_students,cap,plist,all_reserves,)
    sel.sort()
    print(f"Algorithm 4 selected students: {sel}")
    print(f"Rank 1 seats filled: {r1_seats}")
    print(f"Rank 2 seats filled: {r2_seats}")
    print(f"Unreserved entries: {cap - r1_seats - r2_seats}")

if __name__ == "__main__":
    example_1()