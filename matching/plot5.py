import matplotlib.pyplot as plt

hfont = {'fontname':'serif'}
x = [10,20,30,40,50,60,70,80]
az = [1,1,1,1,1,1,1,1]
ehyy = [1, 1, 1, 1, 1, 0.9487179487179487, 0.9545454545454546, 0.9230769230769231]
sy1 = [0.42857142857142855, 0.46153846153846156, 0.4444444444444444, 0.46153846153846156, 0.45161290322580644, 0.48717948717948717, 0.5909090909090909, 0.6923076923076923]

sy2 = [1,1,1,1,1,1,1,1]
pog = [0.0, 0.15384615384615385, 0.2222222222222222, 0.34615384615384615, 0.45161290322580644, 0.46153846153846156, 0.5909090909090909, 0.6923076923076923]

pos = [0.0, 0.15384615384615385, 0.2222222222222222, 0.34615384615384615, 0.45161290322580644, 0.46153846153846156, 0.5909090909090909, 0.6923076923076923]

plt.plot(x,az, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.xlabel("Capacity (q_c)",**hfont)
plt.legend()
plt.show()

