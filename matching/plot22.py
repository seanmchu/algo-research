import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [1, 1, 1, 1]
ehyy = [1, 0.9666666666666667, 0.8888888888888888, 0.8688524590163934]
sy1 = [1.0, 1.0, 1.0, 1.0]
sy2 = [0.35714285714285715, 0.43333333333333335, 0.37777777777777777, 0.4918032786885246]
pog =[0.14285714285714285, 0.3, 0.4666666666666667, 0.64]
pos = [0.14285714285714285, 0.3, 0.4666666666666667, 0.64]
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


 