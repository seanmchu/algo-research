import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [10,20,30,40,50,60,70,80]
az = [1,1,1,1,1,1,1,1]
ehyy = [1,1,1,1,1,1,1,1]
sy1 = [1,1,1,1,1,1,1,1]
sy2 = [1,1,1,1,1,1,1,1]
pog = [0.5633333333333334, 0.785, 0.935, 0.9483333333333334, 0.9885714285714285, 0.9872222222222222, 0.9964999999999999, 0.9991666666666666]
pos = [0.59, 0.8033333333333333, 0.945, 0.9766666666666667, 0.9978571428571429, 0.9988888888888889, 0.9994999999999999, 1.0]
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


