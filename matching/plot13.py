import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1.0, 1.0, 0.997948717948718, 0.9740356083086054]
sy1 = [1.0, 1.0, 1.0, 1.0]
sy2 = [0.6875, 0.6807692307692308, 0.6710256410256411, 0.7054896142433233]
pog = [0.4908333333333333, 0.6130769230769231, 0.737948717948718, 0.8137982195845698]
pos = [0.49500000000000005, 0.6165384615384616, 0.7425641025641025, 0.8260385756676557]
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

