import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1.0, 1.0, 1.0, 1.0]
sy1 = [0.6035, 0.65, 0.6592292089249493, 0.866131621187801]
sy2 = [1.0, 1.0, 1.0000000000000002, 0.9999999999999999]
pog =[0.3045, 0.403, 0.48985801217038544, 0.7157303370786517]
pos = [0.30450000000000005, 0.403, 0.48985801217038544, 0.7157303370786515]
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

