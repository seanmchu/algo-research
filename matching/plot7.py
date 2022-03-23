import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1.0, 1.0, 0.9988888888888889, 0.9860416666666666]
sy1 = [1.0, 1.0, 1.0, 1.0]
sy2 = [0.7225, 0.7545833333333333, 0.8072222222222222, 0.7977083333333334]
pog = [0.4908333333333333, 0.6533333333333333, 0.8061111111111111, 0.8693749999999999]
pos = [0.4925, 0.66125, 0.8202777777777778, 0.9020833333333332]
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


