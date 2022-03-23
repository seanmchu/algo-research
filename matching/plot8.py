import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1.0, 1.0, 1.0, 0.9999999999999999]
sy1 = [0.6014999999999999, 0.60075, 0.6119402985074627, 0.7850891410048622]
sy2 = [1.0, 1.0, 0.9999999999999999, 1.0]
pog = [0.3025, 0.39925, 0.503731343283582, 0.7094003241491085]
pos = [0.3025, 0.39925, 0.5037313432835822, 0.7094003241491085]
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


