import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [20,40,60,80]
az = [0.7996536312849162, 0.6893364779874216, 0.6246882494004796, 0.8425903361344538]
ehyy = [0.7988100558659218, 0.689311320754717, 0.6246594724220623, 0.8425903361344538]
sy1 = [0.9528491620111732, 0.9543616352201256, 0.9723908872901678, 0.9804642857142856]
sy2 = [0.8197039106145251, 0.7093364779874216, 0.63246882494004796, 0.851425903361344538]
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


