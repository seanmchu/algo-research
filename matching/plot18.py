import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}

def fix(a):
    print(a)
    a[0] = a[0]/89.5
    a[1] = a[1]/79.5
    a[2] = a[2]/69.5
    a[3] = a[3]/59.5
    print(a)


x = [20,40,60,80]
az = [65.93449999999999, 44.38224999999999, 33.46649999999999, 45.304750000000006]
ehyy = [65.8825, 44.366749999999996, 33.46616666666665, 45.304750000000006]
sy1 = [78.312, 70.39575, 59.65166666666667, 50.35325000000002]
sy2 = [66.2365, 44.38224999999999, 34.26649999999999, 45.904750000000006]
pog =[89.5, 79.5, 69.5, 59.5]
pos = [89.5, 79.5, 69.5, 59.5]
fix(az)
fix(ehyy)
fix(sy1)
fix(sy2)
fix(pog)
fix(pos)
plt.plot(x,az, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.title("")
plt.xlabel("Capacity (q_c)",**hfont)
plt.legend()
plt.show()

