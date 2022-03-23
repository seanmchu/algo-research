import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1.0, 0.9996666666666666, 0.9939999999999999, 0.9474037976810621]
sy1 = [1.0, 1.0, 1.0, 1.0]
sy2 = [0.5992857142857143, 0.5730000000000001, 0.5613333333333334, 0.5862880188203664]
pog = [0.43142857142857144, 0.517, 0.6402222222222222, 0.744916820702403]
pos = [0.43142857142857144, 0.517, 0.6406666666666666, 0.74777348344816]

plt.plot(x,az, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.title("")
plt.xlabel("Capacity (q_c)",**hfont)
plt.legend(loc="lower right")
plt.show()


