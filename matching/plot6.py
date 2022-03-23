import matplotlib.pyplot as plt
from matplotlib import rc 
hfont = {'fontname':'serif'}

x = [10,20,30,40,50,60,70,80]
azsu = [0.8656084656084656, 0.8581005586592179, 0.8859960552268246, 0.8522012578616353, 0.8853691275167787, 0.8328537170263789, 0.8788482834994462, 0.9077310924369748]

ehyy = [0.8497354497354497, 0.8581005586592179, 0.8836291913214991, 0.8515723270440252, 0.8853691275167787, 0.8256594724220624, 0.8777408637873754, 0.8987394957983194]

sy1 = [0.9555555555555555, 0.9692737430167597, 0.9893491124260354, 0.989308176100629, 0.9994630872483222, 0.9966426858513189, 0.9995570321151714, 1]

sy2 = [0.8656084656084656, 0.8581005586592179, 0.8859960552268246, 0.8522012578616353, 0.8853691275167787, 0.8328537170263789, 0.8788482834994462, 0.9077310924369748]

pog = [1, 1, 1, 1, 1, 1, 1, 1]

pos = [1, 1, 1, 1, 1, 1, 1, 1]

plt.plot(x,azsu, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.xlabel("Capacity (q_c)",**hfont)

plt.legend()
plt.show()

