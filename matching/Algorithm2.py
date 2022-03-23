from classes import Student, Seat, Reserve, Graph


def algo2(students,capacity,reserves,plist):

    print("Students | types: ")
    for s in students:
        print(f'{s.get_index()} | {s.get_types()}')
    print(f"Capacity : {capacity}")
    print("Reserves : Type | Rank | quota limit")
    for r in reserves:
        print(f'{r.get_type()}|{r.get_rank()}|{r.get_cap()}')
    print("Priority ordering of students (index)")
    print(plist)
    
    
    sel = []
    p_students = [] 
    typedict = {}

    #We wish to keep track of rank 1 and 2 seats filled
    r1_seats = 0
    r2_seats = 0

    #Put reserves into a dict of types
    for i in reserves:
        if (i.t not in typedict):
            typedict[i.t] = {}
            typedict[i.t][1] = 0
            typedict[i.t][2] = 0
        typedict[i.t][i.rank] = i.cap
    #Order in students by priority
    for p in plist:
        for s in students:
            if (s.get_index() == p):
                p_students.append(s)
    #get students 
    #rank 1 case 
    for s in p_students:
        if (len(sel) < capacity):
            if (s not in sel):          
                for t in s.types:
                    if (t in typedict and typedict[t][1] > 0):
                        typedict[t][1] -= 1
                        sel.append(s)
                        r1_seats += 1
                        break
        else:
            break
    #rank 2 case
    for s in p_students:
        if(len(sel) < capacity):
            if (s not in sel):
                for t in s.types:
                    if (t in typedict and typedict[t][1] + typedict[t][2] > 0):
                        if (typedict[t][1] > 0):
                            typedict[t][1] -= 1
                            r1_seats += 1 
                        else: 
                            typedict[t][2] -= 1
                            r2_seats += 1
                        sel.append(s)
                        break
        else:
            break 
    #add the rest
    for s in p_students:
        if(len(sel) < capacity):
            if (s not in sel):
                sel.append(s)
        else:
            break 
    #Convert sel to student numbers 
    #we want to return the requisite metrics as well
    sl = [] 
    for s in sel:
        sl.append(s.index)
    sl.sort()
    return sl,r1_seats,r2_seats
    
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
    sel,r1_seats,r2_seats = algo2(all_students,cap,all_reserves,plist)
    print(f"Algorithm 2 selected {sel}")
    print(f"Rank 1 seats filled {r1_seats}")
    print(f"Rank 2 seats filled {r2_seats}")
    print(f"Unranked students filled {cap - r1_seats - r2_seats}")
if __name__ == "__main__":
    example_1()