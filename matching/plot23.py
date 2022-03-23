import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy =  [1, 1, 1, 1]
sy1 = [0.7, 0.75, 0.75, 0.8472222222222222]

sy2 = [1, 1, 1, 1]
pog = [0.1, 0.225, 0.38333333333333336, 0.64]
pos = [0.1, 0.225, 0.38333333333333336, 0.64]
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

