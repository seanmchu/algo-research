from Algorithm1 import algo1
from Algorithm4 import algo4
from classes import * 
from random import random,randint
import sys, os
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def test(example_name,students,capacity,reserves,priority):
    blockPrint()
    s1 = algo1(students,capacity,reserves,priority)
    s2 = algo4(students,capacity,priority,reserves) 
    enablePrint()
    print (f'S1: {s1}')
    print (f'S2: {s2}')
    
    print(f'For {example_name}:')
    sl = []
    for s in students:
        sl.append((s.index,s.types))
    print(f'Students (index,types)= {sl}')
    print(f'Capacity = {capacity}')
    print(f'Priority = {priority}')
    rl = []
    for r in reserves: 
        rl.append((r.t,r.rank,r.cap))
    print(f'Reserves (type,rank,capacity)= {rl}')
    s1.sort()
    s2.sort()
    print(f'Algorithm1 selected students {s1}')
    print(f'Algorithm4 selected students {s2}')
    assert(s1 == s2)

def example_1():
    s1 = Student(1,[1,3,4,5])
    s2 = Student(2,[1,3,4,5])
    s3 = Student(3,[1,2,3])
    plist = [1,2,3]
    r1 = Reserve(2,1,1)
    r2 = Reserve(3,2,3)
    r3 = Reserve(5,2,3)
    cap = 2
    all_students = [s1,s2,s3]
    all_reserves = [r1,r2,r3]
    test("example 1",all_students,cap,all_reserves,plist)

def example_2():
    s1 = Student(1,[2,3,4]) 
    s2 = Student(2,[1,2,3,4,5])
    s3 = Student(3,[1,2,4])
    s4 = Student(4,[2,3])
    plist = [1,2,3,4]
    r1 = Reserve(1,1,0)
    r2 = Reserve(2,2,3)
    r3 = Reserve(3,2,0)
    r4 = Reserve(4,3,3)
    r5 = Reserve(5,1,1)
    cap = 2
    all_students = [s1,s2,s3,s4]
    all_reserves = [r1,r2,r3,r4,r5]
    test("example 2",all_students,cap,all_reserves,plist)

def example_3():
    s1 = Student(1,[1,2]) 
    s2 = Student(2,[1,2,3])
    s3 = Student(3,[3,4])
    s4 = Student(4,[4,3])
    plist = [1,2,3,4]
    r1 = Reserve(1,1,1)
    r2 = Reserve(2,2,1)
    r3 = Reserve(3,2,2)
    r4 = Reserve(4,1,1)
    capacity = 3
    all_students = [s1,s2,s3,s4]
    all_reserves = [r1,r2,r3,r4] 
    test("example 3",all_students,capacity,all_reserves,plist)

def test_make_example():
    n_example = 0 
    n_students = 4 
    s_types = [[1,2],[1,2,3],[3,4],[4,3]]
    n_reserves = 4 
    r_types = [[1,1,1],[2,2,1],[3,2,2],[4,1,1]]
    cap = 3 
    make_example(n_example,n_students,s_types,n_reserves,r_types,cap)

def make_example(n_example,n_students,s_types,n_reserves,r_types,cap):
    all_students = []
    for i in range(n_students):
        all_students.append(Student(i+1,s_types[i]))
    all_reserves = [] 
    for i in range(n_reserves):
        res_profile = r_types[i]
        all_reserves.append(Reserve(res_profile[0],res_profile[1],res_profile[2]))
    plist = [] 
    for i in range(n_students):
        plist.append(i+1)
    test(f'example {n_example}',all_students,cap,all_reserves,plist)

def gen_students(n_students,n_types_max):
    s_types = [] 
    for i in range(n_students):
        s = [] 
        for j in range(n_types_max):
            if (random() < .5):
                s.append(j + 1)
        s_types.append(s)
    return s_types

def gen_reserves(n_types_max,n_students,max_ranks):
    r_types = [] 
    for i in range(1,n_types_max + 1):
        r = [] 
        #Type
        r.append(i)
        #Rank
        r.append(randint(1,max_ranks)) 
        #Capacity
        r.append(randint(0,n_students)) 
        r_types.append(r)
    return r_types

def generate_examples(n_students_max,n_types_max,max_ranks):
    ind = 0
    for i in range(1,n_students_max + 1):
        sl = gen_students(i,n_types_max)
        rl = gen_reserves(n_types_max,i,max_ranks)
        make_example(ind,i,sl,n_types_max,rl,randint(1,i))
        ind += 1


if __name__ == "__main__":
    #example_1()
    #example_2()
    #example_3()
    #test_make_example()
    for i in range(1000):
        generate_examples(5,5,3)