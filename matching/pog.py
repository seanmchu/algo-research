from classes import *

def pog(students,cap,plist,reserves):
    sel = []
    slist = []
    r1 = 0
    r2 = 0
    #we sort students by priority
    for p in plist:
        for s in students:
            if (s.index == p):
                slist.append(s)
    #Put reserves into an aggregated dict
    res = {}
    for r in reserves:
        if (r.cap != 0):
            res[(r.t,r.rank)] = r.cap
    
    for s in slist:
        if (len(sel) >= cap):
            break
        sel.append(s.index)
        done = False 
        for t in s.types:
            if (res.get((t,1)) != 0 and res.get((t,1)) is not None):
                res[(t,1)] -= 1
                r1 += 1
                done = True 
                break
        if (not done):
            for t in s.types:
                if (res.get((t,2)) != 0 and res.get((t,2)) is not None):
                    res[(t,2)] -= 1
                    r2 += 1
                    break
    sel.sort()
    return sel,r1,r2
         


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
    sel,r1_seats,r2_seats = pog(all_students,cap,plist,all_reserves,)
    sel.sort()
    print(f"POG selected students: {sel}")
    print(f"Rank 1 seats filled: {r1_seats}")
    print(f"Rank 2 seats filled: {r2_seats}")
    print(f"Unreserved entries: {cap - r1_seats - r2_seats}")

if __name__ == "__main__":
    example_1()