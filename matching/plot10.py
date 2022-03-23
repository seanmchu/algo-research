import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1, 1, 0.9444444444444444, 0.875]
sy1 = [1.0, 1.0, 1.0, 1.0]
sy2 = [0.5, 0.5833333333333334, 0.6388888888888888, 0.6666666666666666]
pog = [0.08333333333333333, 0.3333333333333333, 0.5833333333333334, 0.7083333333333334]
pos = [0.08333333333333333, 0.3333333333333333, 0.5833333333333334, 0.7083333333333334]
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



