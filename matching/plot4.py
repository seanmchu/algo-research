import matplotlib.pyplot as plt
hfont = {'fontname':'serif'}


x = [10,20,30,40,50,60,70,80]
az = [1,1,1,1,1,1,1,1]
ehyy = [1,1,1,1,1,1,1,1]
sy1 = [1,1,1,1,1,1,1,1]
sy2 = [1,1,1,1,1,1,1,1]
pog = [0.0, 0.3333333333333333, 0.5, 0.6666666666666666, 0.7857142857142857, 0.8333333333333334, 0.9, 0.9583333333333334]
pos = [0.0, 0.3333333333333333, 0.5, 0.75, 0.9285714285714286, 0.8888888888888888, 0.95, 1]
plt.plot(x,az, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.xlabel("Capacity (q_c)",**hfont)
plt.legend()
plt.show()

