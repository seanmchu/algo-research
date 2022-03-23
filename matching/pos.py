from classes import *
from Algorithm1 import algo1

def pos(students,cap,plist,reserves):
    sel = []
    for p in plist:
        if (len(sel) >= cap):
            break 
        for s in students:
            if (s.index == p):
                sel.append(s)
    for ss in sel:
        print(ss.index)
    s,r1,r2 = algo1(sel,cap,reserves,plist)
    return s,r1,r2




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
    sel,r1_seats,r2_seats = pos(all_students,cap,plist,all_reserves,)
    sel.sort()
    print(f"Algorithm 4 selected students: {sel}")
    print(f"Rank 1 seats filled: {r1_seats}")
    print(f"Rank 2 seats filled: {r2_seats}")
    print(f"Unreserved entries: {cap - r1_seats - r2_seats}")

if __name__ == "__main__":
    example_1()