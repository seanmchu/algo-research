import matplotlib.pyplot as plt

hfont = {'fontname':'serif'}
x = [10,20,30,40,50,60,70,80]
azsu = [0.9377566137566139, 0.9373743016759778, 0.9529151873767258, 0.9321792452830189, 0.9515114093959732, 0.939187050359712, 0.9581085271317829, 0.9612773109243697]

ehyy = [0.9345925925925926, 0.9349664804469274, 0.9509072978303746, 0.9289559748427672, 0.9486684563758391, 0.9361894484412471, 0.9555902547065335, 0.9609075630252101]

sy1 = [0.9904021164021164, 0.9947877094972066, 0.9990927021696252, 0.999556603773585, 0.999986577181208, 0.9999664268585131, 0.9999955703211516, 1.0]

sy2 = [0.9377566137566139, 0.9373743016759778, 0.9529151873767258, 0.9321792452830189, 0.9515114093959732, 0.939187050359712, 0.9581085271317829, 0.9612773109243697]

pog = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

pos = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
plt.plot(x,azsu, label = "A-S", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "EHYY",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "SY1",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.plot(x,sy2, label = "SY2",linestyle = 'dotted', marker = 'p')
plt.plot(x,pog, label = "POG",linestyle = '--', marker = 'D')
plt.plot(x,pos, label = "POS",linestyle = '--', marker = 'P')
plt.xlabel("Capacity (q_c)",**hfont)
plt.legend()
plt.show()

