import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az =[0.6743016759776537, 0.549685534591195, 0.5143884892086331, 0.7581932773109243]
ehyy = [0.6715083798882682, 0.549685534591195, 0.5143884892086331, 0.7581932773109243]
sy1 = [0.8268156424581006, 0.7880503144654087, 0.7702637889688249, 0.8006302521008404]
sy2 = [0.6943016759776537, 0.549685534591195, 0.5243884892086331, 0.7581932773109243]
pog = [1, 1, 1, 1]
pos = [1, 1, 1, 1]
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

