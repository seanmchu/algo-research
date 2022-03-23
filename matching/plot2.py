import matplotlib.pyplot as plt
hfont = {'fontname':'serif'}

x = [10,20,30,40,50,60,70,80]
az = [1,1,1,1,1,1,1,1]
ehyy = [1.0, 1.0, 1.0, 1.0, 1.0, 0.9994871794871796, 0.9993180268242784, 0.9909615384615384]
sy1 = [0.47714285714285715, 0.546923076923077, 0.61, 0.6169230769230769, 0.71, 0.7256410256410256, 0.808365537622187, 0.8524999999999999]
sy2 = [1,1,1,1,1,1,1,1]
pog = [0.32142857142857145, 0.4653846153846154, 0.5844444444444444, 0.6084615384615385, 0.7051612903225807, 0.7223076923076923, 0.8045010229597637, 0.845576923076923]
pos = [0.3242857142857143, 0.4692307692307693, 0.5894444444444444, 0.6096153846153847, 0.7093548387096775, 0.7253846153846154, 0.8081382132302797, 0.8524999999999999]
plt.plot(x,az, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.xlabel("Capacity (q_c)",**hfont)
plt.legend()
plt.show()

