from Algorithm2 import algo2 
from Algorithm1 import algo1 
from Algorithm5 import algo5 
from Algorithm6 import algo6
from Algorithm7 import algo7
from Algorithm8 import algo8
from pog import pog 
from pos import pos
from classes import * 
from random import random,randint
from matplotlib import pyplot as plt 
import sys, os
import operator
import numpy.random as ran
from scipy.stats import truncnorm 
#Assumptions:
#   everything is up to 2 ranks 
#   types are distributed among students in a uniformly random fashion (using python.random)
#   The capacity of each reserve (seats assigned to each rank/type) is uniformly random
#   we say that the number of types is always 3 (number of seats per rank is between 0-2), and the number of students is always 6


#Default parameters
MAX_RANK = 2
MAX_SEATS = 2 
N_STUDENTS = 10
N_TYPES = 4 
TYPE_CHANCE = 0.5
RESERVE_PERCENTAGE_OF_MAX_CAP = 0.4
N_ALGORITHMS = 6
PRINTING = 0
MULTIPLIER = 1.7





#all type 

#glob lists to carry datapoints for plotting

#Stores all selected student data
all_data = []
#stores relative averages as a n_alg * 2 list of list 
rel_avg = []
rel_wc = []
#relatives for priority
r_avg = []
r_best = []
r_worst = []
p_tot = []
p_worst = []

def get_truncated_normal(mean=0, sd=1, low=0, upp=10):
    return truncnorm(
        (low - mean) / sd, (upp - mean) / sd, loc=mean, scale=sd)

#SAT score generators
x0 = get_truncated_normal(1135,211,0,1600)

#single type
x1 = get_truncated_normal(963,211,0,1600)
x2 = get_truncated_normal(964,211,0,1600)
x3 = get_truncated_normal(1016,211,0,1600)

#double type 
x12 = get_truncated_normal(878,211,0,1600)
x13 = get_truncated_normal(904,211,0,1600)
x23 = get_truncated_normal(905,211,0,1600)

#all types 
x123 = get_truncated_normal(838,211,0,1600)


def setup():
    for i in range(0,N_ALGORITHMS):
        all_data.append([[],[]])
        rel_avg.append([[],[]])
        rel_wc.append([1,1])
        r_avg.append([])
        r_best.append([])
        r_worst.append([])
        p_tot.append([])
        p_worst.append(1)
def enter_data(alg,d1,d2):
    global all_data
    all_data[alg][0].append(d1)
    all_data[alg][1].append(d1 + d2)

#calculates: priority of selected students, then sorts
#input is s: selected students, pl: priority list
def avgg(s,pl):
    s2 = []
    for i in range(len(pl)):
        for ss in s:
            if (ss == pl[i]):
                s2.append(i+1)
    s2.sort()
    return s2 

def enter_p_data(alg,s,pl,o):
    global r_avg 
    global r_best 
    global r_worst 
    global p_tot
    size = len(s)
    best = []
    for i in range(1,size + 1):
        best.append(i)
    s1 = avgg(s,pl)
    r_avg[alg].append((avg(s1)/avg(best)))
    r_best[alg].append(s1[0]/best[0])
    r_worst[alg].append(s1[len(s1)-1]/best[len(s1)-1])
    p_tot[alg].append(avg(s1))
    opt = 100 - o
    result = 100 - avg(s1)
    if (result/opt) < p_worst[alg]:
        p_worst[alg] = result/opt

def enter_rel_data(alg,s1,s2,s11,s12,s21,s22):
    global rel_avg 
    global rel_wc
    s12 = s11 + s12 
    s22 = s21 + s22 
    if (s11 != 0):
        r1 = s21/s11 
    else:
        r1 = 1
    if (s12 != 0):
        r2 = s22/s12 
    else:
        r2 = 1
    rel_avg[alg][0].append(r1) 
    rel_avg[alg][1].append(r2) 
    if (rel_wc[alg][0] > r1):
        rel_wc[alg][0] = r1 
    if (rel_wc[alg][1] > r2):
        rel_wc[alg][1] = r2 


def get_params():
    print("Would you like to enter custom parameters? (y/n)")
    print("Note: default is- n_students = 10, n_types = 4, max_seats/(type/rank) = 2, max rank = 2, type chance = 0.5")
    option = input()
    if (option == 'y'):
        global N_STUDENTS
        global N_TYPES 
        global MAX_SEATS 
        global MAX_RANK 
        global TYPE_CHANCE
        print("Enter number of students: ")
        N_STUDENTS = int(input())
        print("Enter n_types: ")
        N_TYPES = int(input())
        print("Enter max number of seats/(type/rank) [Reduce when many types]: ")
        MAX_SEATS = int(input())
        print("Enter max rank: ")
        MAX_RANK = int(input())
        print("Enter type chance [0-1]")
        TYPE_CHANCE = float(input())
        print(f"type chance is now {TYPE_CHANCE}")
    print("Enter number of tests to run: ")
    n = int(input())
    print("Print output of each test? (y/n)")
    yn = input()
    if (yn == 'y'):
        global PRINTING
        PRINTING = 1
    return n

def print_example(s1,s2,s3,s4,s5,s6,students,reserves,capacity,priority):
    # if ((s1_r1 != s2_r1 or s1_r1 + s1_r2 != s2_r1 + s2_r2)):
    #         print('SPECIAL EXAMPLE!!!')
    print("example found:")
    print ("Student profiles: ")
    for s in students:
        print(f"index {s.index} | types {s.types}")
    print("Reserves: ")
    for r in reserves:
        print(f"type: {r.t} | rank: {r.rank} | capacity: {r.cap}")
    print(f"capacity is {capacity}")
    print(f"priorty ordering is {priority}")
    print(f"A-S selected {s1}")
    print(f"EHYY selected {s2}")
    print(f"SY1 selected {s3}")
    print(f"SY2 selected {s4}")

def avg(l):
    if (len(l) != 0):
        return sum(l)/len(l)
    else:
        return 0

def blockPrint():
    sys.stdout = open(os.devnull, 'w')

def enablePrint():
    sys.stdout = sys.__stdout__

def test(test_no,students,capacity,reserves,priority):
    blockPrint()
    #run algos and get results 
    s1,s1_r1,s1_r2 = algo1(students,capacity,reserves,priority)
    s2,s2_r1,s2_r2 = algo2(students,capacity,reserves,priority)
    # s3,s3_r1,s3_r2 = algo5(students,capacity,priority,reserves)
    #s4,s4_r1,s4_r2 = algo6(students,capacity,priority,reserves)
    s5,s5_r1,s5_r2 = pog(students,capacity,priority,reserves)
    s6,s6_r1,s6_r2 = pos(students,capacity,priority,reserves)
    s3,s3_r1,s3_r2 = algo7(students,capacity,reserves,priority)
    s4,s4_r1,s4_r2 = algo8(students,capacity,reserves,priority)
    enter_data(0,s1_r1,s1_r2)
    enter_data(1,s2_r1,s2_r2)
    enter_data(2,s3_r1,s3_r2)
    enter_data(3,s4_r1,s4_r2)
    enter_data(4,s5_r1,s5_r2)
    enter_data(5,s6_r1,s6_r2)
    enablePrint()
    s1.sort()
    s2.sort()
    s3.sort()
    s4.sort()
    s5.sort()
    s6.sort()
    #Looks for examples
    #if (s1 != s2 and s1 != s3 and s1 != s4):
        #print_example(s1,s2,s3,s4,s5,s6,students,reserves,capacity,priority)
    enter_rel_data(1,s1,s2,s1_r1,s1_r2,s2_r1,s2_r2)
    enter_rel_data(2,s1,s3,s1_r1,s1_r2,s3_r1,s3_r2)
    enter_rel_data(3,s1,s4,s1_r1,s1_r2,s4_r1,s4_r2)
    enter_rel_data(4,s1,s5,s1_r1,s1_r2,s5_r1,s5_r2)
    enter_rel_data(5,s1,s6,s1_r1,s1_r2,s6_r1,s6_r2)  
    o = avg(avgg(s6,priority))
    enter_p_data(0,s1,priority,o)
    enter_p_data(1,s2,priority,o)
    enter_p_data(2,s3,priority,o)
    enter_p_data(3,s4,priority,o)
    enter_p_data(4,s5,priority,o)
    enter_p_data(5,s6,priority,o)
    
    if (PRINTING == 0):
        blockPrint()
    else:
        enablePrint()
    print(f"Input of test #{test_no}:")
    sl = []
    for s in students:
        sl.append((s.index,s.types))
    rl = []
    for r in reserves: 
        rl.append((r.t,r.rank,r.cap))
    print(f'Students (index,types)= {sl}')
    print(f'Capacity = {capacity}')
    print(f'Priority = {priority}')
    print(f'Reserves (type,rank,capacity)= {rl}')
    print(f"Results of test #{test_no}:")
    print(f"Algorithm1 selected students: {s1}")
    print(f"    Rank 1 seats filled: {s1_r1}")
    print(f"    Rank 2 seats filled: {s1_r2}")
    print(f"Algorithm2 selected students: {s2}")
    print(f"    Rank 1 seats filled: {s2_r1}")
    print(f"    Rank 2 seats filled: {s2_r2}")
    print(f"Horizontal choice on 1 rank selected students: {s3}")
    print(f"    Rank 1 seats filled: {s3_r1}")
    print(f"    Rank 2 seats filled: {s3_r2}")
    print(f"Horizontal choice on 2 ranks selected students: {s4}")
    print(f"    Rank 1 seats filled: {s4_r1}")
    print(f"    Rank 2 seats filled: {s4_r2}")
    print(f"POG selected students: {s5}")
    print(f"    Rank 1 seats filled: {s5_r1}")
    print(f"    Rank 2 seats filled: {s5_r2}")
    print(f"POS selected students: {s6}")
    print(f"    Rank 1 seats filled: {s6_r1}")
    print(f"    Rank 2 seats filled: {s6_r2}")
    if (PRINTING == 0):
        enablePrint()
    return s1_r1,s1_r2,s2_r1,s2_r2,s3_r1,s3_r2,s4_r1,s4_r2,s5_r1,s5_r2,s6_r1,s6_r2

def generate_students(n_students,n_types):
    students = [] 
    for i in range(n_students):
        types = [] 
        for j in range(n_types):
            if (random() < TYPE_CHANCE):
                types.append(j+1)
        s = Student(i+1,types)
        students.append(s)
    return students 

def generate_reserves(n_reserves,max_cap,max_rank):
    reserves = []
    for i in range(n_reserves):
        for j in range(max_rank):
            cap = int(round(random() * max_cap * RESERVE_PERCENTAGE_OF_MAX_CAP))
            r = Reserve(i+1,j+1,cap)
            reserves.append(r)
    return reserves

def generate_example(n,cap):
    all_students = generate_students(N_STUDENTS,N_TYPES)
    all_reserves = generate_reserves(N_TYPES,MAX_SEATS,MAX_RANK)
    #We keep capacity >= 1 because otherwise the answer is trivial and not interesting
    capacity = cap
    plist = [i for i in range(1,N_STUDENTS + 1)]
    #print(all_students,all_reserves,capacity,plist)
    s1_r1, s1_r2, s2_r1, s2_r2, s3_r1, s3_r2, s4_r1, s4_r2, s5_r1, s5_r2, s6_r1, s6_r2 = test(n,all_students,capacity,all_reserves,plist)
    return s1_r1, s1_r2, s2_r1, s2_r2, s3_r1, s3_r2, s4_r1, s4_r2, s5_r1, s5_r2, s6_r1, s6_r2 

def generate_sat_students(n_s):
    students = []
    for i in range(0,n_s):
        types = []
        #race
        if (ran.uniform(0,1) < 0.39):
            types.append(1)
            #education
            if (ran.uniform(0,1) < 0.6):
                types.append(2)
                if (ran.uniform(0,1) < 0.26):
                    types.append(3)
            else:
                if (ran.uniform(0,1) < 0.1):
                    types.append(3)
        else:
            #education, no race 
            if (ran.uniform(0,1) < 0.3):
                types.append(2) 
                if (ran.uniform(0,1) < 0.26):
                    types.append(3)
            else:
                if(ran.uniform(0,1) < 0.1):
                    types.append(3)
        types.sort()
        #assign SAT score
        score = 0
        if (types == []):
            score = x0.rvs()
        elif (types == [1]):
            score = x1.rvs()
        elif (types == [2]):
            score = x2.rvs()
        elif (types == [3]):
            score = x3.rvs()
        elif (types == [1,2]):
            score = x12.rvs()
        elif (types == [1,3]):
            score = x13.rvs()
        elif (types == [2,3]):
            score = x23.rvs()
        else: 
            score = x123.rvs()
        s = Student(i+1,types)
        s.sat = score 
        students.append(s)
    return students 


def generate_sat_reserves(cap):
    mu = MULTIPLIER / 0.65
    r1 = Reserve(1,1,int(cap * 0.15 * mu ))
    r2 = Reserve(1,2,int(cap * 0.20 * mu))
    r3 = Reserve(2,1,int (cap * 0.10 * mu))
    r4 = Reserve(2,2,int (cap * 0.10 * mu))
    r5 = Reserve(3,1, max(1,int (cap * 0.05 * mu)))
    r6 = Reserve(3,2, max(1,int (cap * 0.05 * mu)))
    reserves = [r1,r2,r3,r4,r5,r6]
    #hence, total rank 1 seats = 0.3, total rank 1 + 2 seats = 0.5
    return reserves 


def generate_sat_example(n,cap,students):
    all_students = generate_sat_students(students)
    all_reserves = generate_sat_reserves(cap)
    capacity = cap
    plist = []
    #sort by sat score
    sorted_students = sorted(all_students,key = operator.attrgetter('sat'),reverse = True)
    for s in sorted_students:
        plist.append(s.index)
    s1_r1, s1_r2, s2_r1, s2_r2, s3_r1, s3_r2, s4_r1, s4_r2, s5_r1, s5_r2, s6_r1, s6_r2 = test(n,sorted_students,capacity,all_reserves,plist)
    return s1_r1, s1_r2, s2_r1, s2_r2, s3_r1, s3_r2, s4_r1, s4_r2, s5_r1, s5_r2, s6_r1, s6_r2 

def run_sat_examples(n,s,c):
    
    n = int(n)
    s = int(s)
    c = int(c)
    s1_r1 = 0
    s1_r2 = 0
    s2_r1 = 0 
    s2_r2 = 0 
    s3_r1 = 0
    s3_r2 = 0
    s4_r1 = 0 
    s4_r2 = 0
    s5_r1 = 0
    s5_r2 = 0
    s6_r1 = 0
    s6_r2 = 0
    blockPrint()
    for i in range(n):
        #get temp values to add to totals
        t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12 = generate_sat_example(i,c,s)
        s1_r1 += t1 
        s1_r2 += t2 
        s2_r1 += t3 
        s2_r2 += t4
        s3_r1 += t5 
        s3_r2 += t6 
        s4_r1 += t7 
        s4_r2 += t8 
        s5_r1 += t9 
        s5_r2 += t10 
        s6_r1 += t11 
        s6_r2 += t12
    enablePrint()
    #Calc averages
    s1_r1_avg = s1_r1/n 
    s1_r2_avg = s1_r2/n 
    s2_r1_avg = s2_r1/n 
    s2_r2_avg = s2_r2/n 
    s3_r1_avg = s3_r1/n 
    s3_r2_avg = s3_r2/n 
    s4_r1_avg = s4_r1/n 
    s4_r2_avg = s4_r2/n 
    s5_r1_avg = s5_r1/n
    s5_r2_avg = s5_r2/n
    s6_r1_avg = s6_r1/n
    s6_r2_avg = s6_r2/n
    #get sums 
    s1_both = s1_r1_avg + s1_r2_avg 
    s5_both = s5_r1_avg + s5_r2_avg 
    s6_both = s6_r1_avg + s6_r2_avg 
    rel_s5 = s5_both/s1_both
    rel_s6 = s6_both/s1_both 
    #Report gathered results
    if (s1_r1_avg == 0 ):
        print('something went wrong!')
        exit(1)
    
    #NB: optimal in terms of priority --> top n seats wrt \succ_c
    maxim = 100
    print(f"Ptot is {p_tot}")
    print(f"Results after {n} tests: ")
    print(f"    AZ                       | average number of rank 1 seats filled: {s1_r1_avg}")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s1_r1_avg + s1_r2_avg}")
    print(f"                             | average percentile rank of selected students: {(maxim - avg(p_tot[0]))* (maxim/100)} | average percentile of worst rank of selected student: {p_worst[0]}")
    print(f"    EHYY                     | average number of rank 1 seats filled: {s2_r1_avg}            | WC relative to AZ: {rel_wc[1][0]} | rel avg {(s2_r1_avg)/(s1_r1_avg)}")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s2_r1_avg + s2_r2_avg} | WC relative to AZ: {rel_wc[1][1]} | rel avg {(s2_r1_avg + s2_r2_avg)/(s1_r1_avg + s1_r2_avg)}")
    print(f"                             | average percentile rank of selected students: {(maxim - avg(p_tot[1]))* (maxim/100)} | average percentile of worst rank of selected student: {p_worst[1]}")
    print(f"    SY1                      | average number of rank 1 seats filled: {s3_r1_avg}            | WC relative to AZ: {rel_wc[2][0]} | rel avg {(s3_r1_avg)/(s1_r1_avg)} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s3_r1_avg + s3_r2_avg} | WC relative to AZ: {rel_wc[2][1]}| rel avg {(s3_r1_avg + s3_r2_avg)/(s1_r1_avg + s1_r2_avg)}")
    print(f"                             | average percentile rank of selected students: {(maxim - avg(p_tot[2]))* (maxim/100)} | average percentile of worst rank of selected student: {p_worst[2]}")
    print(f"    SY2                      | average number of rank 1 seats filled: {s4_r1_avg}            | WC relative to AZ: {rel_wc[3][0]} | rel avg {(s4_r1_avg)/s1_r1_avg} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s4_r1_avg + s4_r2_avg} | WC relative to AZ {rel_wc[3][1]} | rel avg {(s4_r1_avg + s4_r2_avg)/(s1_r1_avg + s1_r2_avg)} ")
    print(f"                             | average percentile rank of selected students: {(maxim - avg(p_tot[3]))* (maxim/100)} | average percentile of worst rank of selected student: {p_worst[3]}")
    print(f"    POG                      | average number of rank 1 seats filled: {s5_r1_avg}            | WC relative to AZ: {rel_wc[4][0]} | rel avg {(s5_r1_avg)/s1_r1_avg} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s5_both} | WC relative to AZ {rel_wc[4][1]} | rel avg {rel_s5} ")
    print(f"                             | average percentile rank of selected students: {(maxim - avg(p_tot[4])) * (maxim/100)} | average percentile of worst rank of selected student: {p_worst[4]}")
    print(f"    POS                      | average number of rank 1 seats filled: {s6_r1_avg}            | WC relative to AZ: {rel_wc[5][0]} | rel avg {(s6_r1_avg)/s1_r1_avg} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s6_both} | WC relative to AZ {rel_wc[5][1]} | rel avg {rel_s6} ")
    print(f"                             | average percentile rank of selected students: {(maxim - avg(p_tot[5])) * (maxim/100)} | average percentile of worst rank of selected student: {p_worst[5]}")
    p11 = (maxim - avg(p_tot[0]))* (maxim/100)
    p21 = (maxim - avg(p_tot[1]))* (maxim/100)
    p31 = (maxim - avg(p_tot[2]))* (maxim/100)
    p41 = (maxim - avg(p_tot[3]))* (maxim/100)
    p51 = (maxim - avg(p_tot[4]))* (maxim/100)
    p61 = (maxim - avg(p_tot[5]))* (maxim/100)
    r1_avgs = [s1_r1_avg,s2_r1_avg,s3_r1_avg,s4_r1_avg,s5_r1_avg,s6_r1_avg]
    r2_avgs = [s1_r2_avg,s2_r2_avg,s3_r2_avg,s4_r2_avg,s5_r2_avg,s6_r2_avg]
    p_avgs = [p11,p21,p31,p41,p51,p61]
    opt = p61
    for i in range(6):
        p_avgs[i] = p_avgs[i]/opt
    wcs = rel_wc 
    return r1_avgs,r2_avgs,p_avgs,p_worst,wcs 
    

def run_n_examples(n):
    #Totals for reserves filled
    s1_r1 = 0
    s1_r2 = 0
    s2_r1 = 0 
    s2_r2 = 0 
    s3_r1 = 0
    s3_r2 = 0
    s4_r1 = 0 
    s4_r2 = 0
    s5_r1 = 0
    s5_r2 = 0
    s6_r1 = 0
    s6_r2 = 0
    blockPrint()
    for i in range(n):
        #get temp values to add to totals
        t1,t2,t3,t4,t5,t6,t7,t8,t9,t10,t11,t12 = generate_example(i)
        s1_r1 += t1 
        s1_r2 += t2 
        s2_r1 += t3 
        s2_r2 += t4
        s3_r1 += t5 
        s3_r2 += t6 
        s4_r1 += t7 
        s4_r2 += t8 
        s5_r1 += t9 
        s5_r2 += t10 
        s6_r1 += t11 
        s6_r2 += t12
    enablePrint()
    #Calc averages
    s1_r1_avg = s1_r1/n 
    s1_r2_avg = s1_r2/n 
    s2_r1_avg = s2_r1/n 
    s2_r2_avg = s2_r2/n 
    s3_r1_avg = s3_r1/n 
    s3_r2_avg = s3_r2/n 
    s4_r1_avg = s4_r1/n 
    s4_r2_avg = s4_r2/n 
    s5_r1_avg = s5_r1/n
    s5_r2_avg = s5_r2/n
    s6_r1_avg = s6_r1/n
    s6_r2_avg = s6_r2/n
    #get sums 
    s1_both = s1_r1_avg + s1_r2_avg 
    s5_both = s5_r1_avg + s5_r2_avg 
    s6_both = s6_r1_avg + s6_r2_avg 
    rel_s5 = s5_both/s1_both
    rel_s6 = s6_both/s1_both 
    
    
    #Report gathered results
    if (s1_r1_avg == 0 ):
        print('something went wrong!')
        exit(1)

    #NB: optimal in terms of priority --> top n seats wrt \succ_c
    print(f"Results after {n} tests: ")
    print(f"    AZ                       | average number of rank 1 seats filled: {s1_r1_avg}")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s1_r1_avg + s1_r2_avg}")
    print(f"                             | average rank of selected students: {avg(p_tot[0])} | average rank of selected students relative to optimal: {avg(r_avg[0])}| average relative best rank student {avg(r_best[0])}| average relative worst rank student {avg(r_worst[0])}")
    print(f"    EHYY                     | average number of rank 1 seats filled: {s2_r1_avg}            | WC relative to AZ: {rel_wc[1][0]} | rel avg {(s2_r1_avg)/(s1_r1_avg)}")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s2_r1_avg + s2_r2_avg} | WC relative to AZ: {rel_wc[1][1]} | rel avg {(s2_r1_avg + s2_r2_avg)/(s1_r1_avg + s1_r2_avg)}")
    print(f"                             | average rank of selected students: {avg(p_tot[1])} | average rank of selected students relative to optimal: {avg(r_avg[1])}| average relative best rank student {avg(r_best[1])}| average relative worst rank student {avg(r_worst[1])}")
    print(f"    SY1                      | average number of rank 1 seats filled: {s3_r1_avg}            | WC relative to AZ: {rel_wc[2][0]} | rel avg {(s3_r1_avg)/(s1_r1_avg)} ")
    print(f"                             | average rank of selected students: {avg(p_tot[2])} | average number of rank 1 and rank 2 seats filled: {s3_r1_avg + s3_r2_avg} | WC relative to AZ: {rel_wc[2][1]}| rel avg {(s3_r1_avg + s3_r2_avg)/(s1_r1_avg + s1_r2_avg)}")
    print(f"                             | average rank of selected students relative to optimal: {avg(r_avg[2])}| average relative best rank student {avg(r_best[2])}| average relative worst rank student {avg(r_worst[2])}")
    print(f"    SY2                      | average number of rank 1 seats filled: {s4_r1_avg}            | WC relative to AZ: {rel_wc[3][0]} | rel avg {(s4_r1_avg)/s1_r1_avg} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s4_r1_avg + s4_r2_avg} | WC relative to AZ {rel_wc[3][1]} | rel avg {(s4_r1_avg + s4_r2_avg)/(s1_r1_avg + s1_r2_avg)} ")
    print(f"                             | average rank of selected students: {avg(p_tot[3])} | average rank of selected students relative to optimal: {avg(r_avg[3])}| average relative best rank student {avg(r_best[3])}| average relative worst rank student {avg(r_worst[3])}")
    print(f"    POG                      | average number of rank 1 seats filled: {s5_r1_avg}            | WC relative to AZ: {rel_wc[4][0]} | rel avg {(s5_r1_avg)/s1_r1_avg} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s5_both} | WC relative to AZ {rel_wc[4][1]} | rel avg {rel_s5} ")
    print(f"                             | average rank of selected students: {avg(p_tot[4])} |average rank of selected students relative to optimal: {avg(r_avg[4])}| average relative best rank student {avg(r_best[4])}| average relative worst rank student {avg(r_worst[4])}")
    print(f"    POS                      | average number of rank 1 seats filled: {s6_r1_avg}            | WC relative to AZ: {rel_wc[5][0]} | rel avg {(s6_r1_avg)/s1_r1_avg} ")
    print(f"                             | average number of rank 1 and rank 2 seats filled: {s6_both} | WC relative to AZ {rel_wc[5][1]} | rel avg {rel_s6} ")
    print(f"                             | average rank of selected students: {avg(p_tot[5])} |average rank of selected students relative to optimal: {avg(r_avg[5])}| average relative best rank student {avg(r_best[5])}| average relative worst rank student {avg(r_worst[5])}")

def special():
    #Number of tests
    n = 100
    #Number of students
    s = 100
    #capacities tested
    c = [20,40,60,80]
    #where fig[0][2] would be for figure 1, algorithm 3 (sy1)
    #ordering is as,ehyy,sy1,sy2,pog,pos
    fig = []
    for i in range(0,6):
        fig.append([[],[],[],[],[],[]])
    for i in range(0,len(c)):
        r1,r2,pa,pw,wc = run_sat_examples(n,s,c[i])
        fig[0][0].append(1)
        for j in range(1,6):
            fig[0][j].append(r1[j]/r1[0])
        fig[1][0].append(1)
        for j in range(1,6):
            fig[1][j].append( (r1[j] + r2[j]) / (r1[0] + r2[0]) )
        for j in range(0,6):
            fig[2][j].append(pa[j])
        fig[3][0].append(1)
        for j in range(1,6):
            fig[3][j].append(wc[j][0])
        fig[4][0].append(1)
        for j in range(1,6):
            fig[4][j].append(wc[j][1])
        for j in range(0,6):
            fig[5][j].append(pw[j])
        global all_data 
        global rel_avg 
        global rel_wc 
        global r_avg 
        global r_best 
        global r_worst
        global p_tot 
        global p_worst 
        #Stores all selected student data
        all_data = []
        #stores relative averages as a n_alg * 2 list of list 
        rel_avg = []
        rel_wc = []
        #relatives for priority
        r_avg = []
        r_best = []
        r_worst = []
        p_tot = []
        p_worst = []
        setup()
    for i in range(0,6):
        print(f"==== Graph {i} =====\n")
        for j in range(0,6):
            print(f"Algorithm {j}: {fig[i][j]}\n")
    print("Done")


if __name__ == "__main__":

    print("Uniform random (any key) or based on SAT data (s), or multiple (m)?")
    o = input() 
    setup()
    if (o == "s" ):
        print('enter number of tests')
        n = input()
        print('enter number of students')
        s = input()
        print('enter capacity')
        c = input()
        print("Running tests ... ")
        run_sat_examples(n,s,c)
    elif (o == "m"):
        special()
    else:
        n = get_params()
        print("Running tests ... ")
        run_n_examples(n)
        print("Parameters for testing were: ")
        print(f"Number of students: {N_STUDENTS}")
        print(f"Number of seats/(type/rank): {MAX_SEATS}")
        print(f"Number of types: {N_TYPES}")
        print(f"Maximum rank: {MAX_RANK}")
        print(f"Type chance: {TYPE_CHANCE}")
    f1,ax1 = plt.subplots()
    ax1.set_title("Rank 1 seats filled")
    ax1.boxplot([all_data[0][0],all_data[1][0],all_data[2][0],all_data[3][0],all_data[4][0],all_data[5][0]])
    plt.xticks([1,2,3,4,5,6],["AZ","EHYY","SY1","SY2","POG","POS"])
    f2,ax2 = plt.subplots()
    ax2.set_title("Rank 1+2 seats filled")
    ax2.boxplot([all_data[0][1],all_data[1][1],all_data[2][1],all_data[3][1],all_data[4][1],all_data[5][1]])
    plt.xticks([1,2,3,4,5,6],["AZ","EHYY","SY1","SY2","POG","POS"])
    f3,ax3 = plt.subplots()
    ax3.set_title("Rank 1 seats filled relative to AZ")
    ax3.boxplot([rel_avg[1][0],rel_avg[2][0],rel_avg[3][0],rel_avg[4][0],rel_avg[5][0]])
    plt.xticks([1,2,3,4,5],["EHYY","SY1","SY2","POG","POS"])
    f4,ax4 = plt.subplots()
    ax4.set_title("Rank 1 + 2 seats filled relative to AZ")
    ax4.boxplot([rel_avg[1][1],rel_avg[2][1],rel_avg[3][1],rel_avg[4][1],rel_avg[5][1]])
    plt.xticks([1,2,3,4,5],["EHYY","SY1","SY2","POG","POS"])
    plt.show()

    