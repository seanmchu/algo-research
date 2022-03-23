from a1 import kprf 
from a3 import approx_prf
import numpy as np
from sklearn.cluster import kmeans_plusplus
from sklearn.preprocessing import LabelEncoder
import math
import csv 


def within(a,b):
    for i in a:
        #print(i,b)
        if (np.all(np.equal(i,b))):
            return True 
    return False

def norm(a,b):
    n = 0
    for i in range(a.shape[0]):
        n = n + (a[i] - b[i])**2 
    #print(n)
    n = math.sqrt(n)
    return n

def mse(data,centres):
    mse = 0
    centres = np.array(centres)
    for i in range(data.shape[0]):
        #Find closest centroid to data point 
        closest_dist = 10000000000000
        for j in range(centres.shape[0]):
            dist = np.linalg.norm(data[i]-centres[j])
            if (dist < closest_dist):
                closest_dist = dist 
        #mse is distance from closest data point 
        mse += pow(closest_dist,2)
    mse = mse / data.shape[0]
    return mse

#distance of each point to EVERY centroid summed and mean'd
def mss1(data,centres):
    mss = 0 
    centres = np.array(centres)
    for i in range(data.shape[0]):
        for j in range(centres.shape[0]):
            dist = np.linalg.norm(data[i] - centres[j]) 
            mss += pow(dist,2)
    mss = mss / data.shape[0]
    return mss 
def mss2(data,centres,j):
    mss = 0 
    centres = np.array(centres)
    #print(len(centres),j)
    if (j > len(centres)):
        j = len(centres)
    for i in range(data.shape[0]):
        #distance from i to each centroid 
        selections = [] 
        for k in range(centres.shape[0]):
            dist = np.linalg.norm(data[i] - centres[k]) 
            selections.append(dist)
        selections.sort()
        #print(selections)
        #print(j)
        for s in range(j):
            #print(s)
        #    print(selections[s])
            mss += pow(selections[s],2)
        
    mss = mss / data.shape[0]
    return mss 

def wholesale():
    print("=====TESTING DATA FOR WHOLESALE DATASET=====")
    file = open("datasets/wholesale.csv")
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    rows.pop(0)
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            rows[i][j] = int(rows[i][j])
    
    data = np.array(rows)
    ks = [10,30,50,100,150]
    print("data shape is:")
    print(data.shape[0],data.shape[1])
    for k in ks:
        print(f"=====TESTING data for k = {k} =====",flush=True)
        kp = kprf(data,k)
        centres,_ = kmeans_plusplus(data,n_clusters = k)
        a_kpp = approx_prf(data,k)
        mse1 = mse(data,kp)
        mse2 = mse(data,centres)
        mse3 = mse(data,a_kpp)
        mss11 = mss1(data,kp)
        mss12 = mss1(data,centres)
        mss13 = mss1(data,a_kpp)
        print("======Testing of K means criterion=========")
        print("======Mean Squared Distance (closest centroid)=========")
        print(f"Algorithm 1: {mse1}")
        print(f"Scikit k++: {mse2}")
        print(f"Algorithm 3: {mse3}")
        js = [1,math.ceil(k/4),math.ceil(k/2),math.ceil(3*k/4),k]
        for j in js:
            print(f"======Mean Squared Distance  (closest {j} centroids)=========")
            mss21 = mss2(data,kp,j)
            mss22 = mss2(data,centres,j)
            mss23 = mss2(data,a_kpp,j)
            print(f"Algorithm 1: {mss21}")
            print(f"Scikit k++: {mss22}")
            print(f"Algorithm 3: {mss23}")
        print("======Mean Squared Distance  (All centroids)=========")
        print(f"Algorithm 1: {mss11}")
        print(f"Scikit k++: {mss12}")
        print(f"Algorithm 3: {mss13}")
    file.close()
    for i in range(5):
        print(f"\n")

def buddy():
    file = open("datasets/buddymove_holidayiq.csv")
    print("=====TESTING DATA FOR BUDDY DATASET=====",flush=True)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    rows.pop(0)
    rowws = [] 
    for row in rows:
        rr = [] 
        i = 1
        while (i < len(row)):
            rr.append(int(row[i]))
            i = i + 1 
        rowws.append(rr)
    data = np.array(rowws)
    print("data shape is:")
    print(data.shape[0],data.shape[1])
    ks = [10,25,50,75,100]
    for k in ks:
        print(f"=====TESTING data for k = {k} =====",flush=True)
        kp = kprf(data,k)
        centres,_ = kmeans_plusplus(data,n_clusters = k)
        a_kpp = approx_prf(data,k)
        #rand = []
        #for i in range(0,k):
        #    rand.append(data[i])
        #mse0 = mse(data,rand)
        mse1 = mse(data,kp)
        mse2 = mse(data,centres)
        mse3 = mse(data,a_kpp)
        mss11 = mss1(data,kp)
        mss12 = mss1(data,centres)
        mss13 = mss1(data,a_kpp)

        print("======Testing of K means criterion=========")
        print("======Mean Squared Distance (closest centroid)=========")
        print(f"Algorithm 1: {mse1}")
        print(f"Scikit k++: {mse2}")
        print(f"Algorithm 3: {mse3}")
        js = [1,math.ceil(k/4),math.ceil(k/2),math.ceil(3*k/4),k]
        for j in js:
            print(f"======Mean Squared Distance  (closest {j} centroids)=========")
            mss21 = mss2(data,kp,j)
            mss22 = mss2(data,centres,j)
            mss23 = mss2(data,a_kpp,j)
            print(f"Algorithm 1: {mss21}")
            print(f"Scikit k++: {mss22}")
            print(f"Algorithm 3: {mss23}")
        print("======Mean Squared Distance  (All centroids)=========")
        print(f"Algorithm 1: {mss11}")
        print(f"Scikit k++: {mss12}")
        print(f"Algorithm 3: {mss13}")
    for i in range(5):
        print(f"\n")

def hcv():
    file = open("datasets/hcvdat0.csv")
    print("=====TESTING DATA FOR HCV DATASET=====",flush=True)
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)
    rows.pop(0)
    rowws = [] 
    for row in rows:
        rr = [] 
        i = 1
        while (i < len(row)):
            if (i == 1):
                rr.append(int(row[1][0]))
            elif (i == 3):
                if (row[3][0] == "m"):
                    rr.append(0)
                else:
                    rr.append(1)
            else:
                if (row[i] == "NA"):
                    rr.append(0)
                else:
                    rr.append(float(row[i]))
            i = i + 1
        rowws.append(rr)
    print(rowws)
    data = np.array(rowws)
    print("data shape is:")
    print(data.shape[0],data.shape[1])
    ks = [10,50,100,200,300]
    for k in ks:
        print(f"=====TESTING data for k = {k} =====",flush=True)
        kp = kprf(data,k)
        centres,_ = kmeans_plusplus(data,n_clusters = k)
        a_kpp = approx_prf(data,k)
        mse1 = mse(data,kp)
        mse2 = mse(data,centres)
        mse3 = mse(data,a_kpp)
        mss11 = mss1(data,kp)
        mss12 = mss1(data,centres)
        mss13 = mss1(data,a_kpp)

        print("======Testing of K means criterion=========")
        print("======Mean Squared Distance (closest centroid)=========")
        print(f"Algorithm 1: {mse1}")
        print(f"Scikit k++: {mse2}")
        print(f"Algorithm 3: {mse3}")
        js = [1,math.ceil(k/4),math.ceil(k/2),math.ceil(3*k/4),k]
        for j in js:
            print(f"======Mean Squared Distance  (closest {j} centroids)=========")
            mss21 = mss2(data,kp,j)
            mss22 = mss2(data,centres,j)
            mss23 = mss2(data,a_kpp,j)
            print(f"Algorithm 1: {mss21}")
            print(f"Scikit k++: {mss22}")
            print(f"Algorithm 3: {mss23}")
        print("======Mean Squared Distance  (All centroids)=========")
        print(f"Algorithm 1: {mss11}")
        print(f"Scikit k++: {mss12}")
        print(f"Algorithm 3: {mss13}")
    for i in range(5):
        print(f"\n")

    
def seeds():
    file = open("datasets/seeds_dataset.txt")
    print("=====TESTING DATA FOR SEEDS DATASET=====",flush=True)
    lines = file.readlines()
    i = 0
    data_list = [] 
    while (i < len(lines)):
        #print(lines[i])
        row = [] 
        dat = lines[i].split()
        for num in dat:
            row.append(float(num))
        i = i + 1
        data_list.append(row)
    #print(data_list)
    data = np.array(data_list)
    ks = [10,25,50,75,100]
    print("data shape is:")
    print(data.shape[0],data.shape[1])
    for k in ks:
        print(f"=====TESTING data for k = {k} =====",flush=True)
        kp = kprf(data,k)
        centres,_ = kmeans_plusplus(data,n_clusters = k)
        a_kpp = approx_prf(data,k)
        mse1 = mse(data,kp)
        mse2 = mse(data,centres)
        mse3 = mse(data,a_kpp)
        mss11 = mss1(data,kp)
        mss12 = mss1(data,centres)
        mss13 = mss1(data,a_kpp)
        print("======Testing of K means criterion=========")
        print("======Mean Squared Distance (closest centroid)=========")
        print(f"Algorithm 1: {mse1}")
        print(f"Scikit k++: {mse2}")
        print(f"Algorithm 3: {mse3}")
        js = [1,math.ceil(k/4),math.ceil(k/2),math.ceil(3*k/4),k]
        for j in js:
            print(f"======Mean Squared Distance  (closest {j} centroids)=========")
            mss21 = mss2(data,kp,j)
            mss22 = mss2(data,centres,j)
            mss23 = mss2(data,a_kpp,j)
            print(f"Algorithm 1: {mss21}")
            print(f"Scikit k++: {mss22}")
            print(f"Algorithm 3: {mss23}")
        print("======Mean Squared Distance  (All centroids)=========")
        print(f"Algorithm 1: {mss11}")
        print(f"Scikit k++: {mss12}")
        print(f"Algorithm 3: {mss13}")
    for i in range(5):
        print(f"\n")
    file.close()

if (__name__ == "__main__"):
    wholesale()
    buddy()
    hcv()
    seeds()
