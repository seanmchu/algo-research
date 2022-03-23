import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}


x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1, 1, 0.9230769230769231, 0.8703703703703703]
sy1 = [1, 1, 1, 1]
sy2 = [0.5, 0.46153846153846156, 0.5128205128205128, 0.5370370370370371]
pog =[0.16666666666666666, 0.3076923076923077, 0.5641025641025641, 0.6530612244897959]
pos = [0.16666666666666666, 0.3076923076923077, 0.5641025641025641, 0.6530612244897959]

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

