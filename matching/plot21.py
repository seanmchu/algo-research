import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [0.7996648044692737, 0.6813930817610062, 0.6142805755395686, 0.8450021008403358]
ehyy = [0.7993687150837987, 0.6806226415094339, 0.6141055155875301, 0.8450021008403358]
sy1 = [0.9243519553072626, 0.876993710691824, 0.8718489208633095, 0.881710084033613]
sy2 = [0.8196927374301674, 0.714088050314464, 0.6242805755395686, 0.85150021008403358]
pog =  [1.0, 1.0, 1.0, 1.0]

pos =  [1.0, 1.0, 1.0, 1.0]

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

 