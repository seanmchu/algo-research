import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [0.6860335195530726, 0.479874213836478, 0.5158273381294963, 0.7716386554621849]
ehyy = [0.6860335195530726, 0.479874213836478, 0.5158273381294963, 0.7716386554621849]
sy1 = [0.9528491620111732, 0.9543616352201256, 0.9723908872901678, 0.9804642857142856]
sy2 = [0.701860335195530726, 0.48979874213836478, 0.52158273381294963, 0.7816386554621849]
pog = [1.0, 1.0, 1.0, 1.0]
pos = [1.0, 1.0, 1.0, 1.0]
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



