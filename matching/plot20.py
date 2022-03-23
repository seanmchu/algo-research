import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1.0, 1.0, 1.0, 1.000000000000000]
sy1 = [0.7, 0.75, 0.7643961270596229, 0.9595291841341503]
sy2 = [1, 1, 1, 1]
pog = [0.3045, 0.38775, 0.4897231187361984, 0.7175104804901645]
pos = [0.3045, 0.38775, 0.4897231187361984, 0.7175104804901645]
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


 