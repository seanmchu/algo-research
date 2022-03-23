import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [10,25,50,75,100]
az = [2075.8995983935743,938.5220883534137,531.843373493976,388.140562248996, 324.53413654618475]
ehyy = [2072.248995983936,916.277108433735,451.2409638554217,287.5140562248996,180.70682730923696]
sy1 = [2090.8152610441766, 916.9076305220883,478.17269076305223,393.9839357429719,217.1285140562249]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Buddy dataset MSD to closest 1 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
x = [10,25,50,75,100]
az = [10781.429718875503, 27245.393574297188,50364.9437751004,72345.58634538153, 95860.54618473895]
ehyy = [13998.915662650603,30144.293172690763,51739.97590361446,74702.37751004015,97752.9156626506]
sy1 = [11703.317269076306,28273.441767068274,50290.65060240964,72911.9718875502,95742.48192771085]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Buddy dataset MSD to closest k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
x = [10,25,50,75,100]
az = [28781.204819277107,83365.56626506025,158445.54618473895,246963.41767068274, 321935.2891566265]
ehyy = [34891.59437751004,90759.24899598393,166753.46987951806,265851.7269076305,350245.2008032129]
sy1 = [28450.791164658636,82944.59437751005,156509.718875502,241425.12449799196,331464.3453815261]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Buddy dataset MSD to closest k/2 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
x = [10,25,50,75,100]
az = [74024.281124498,176136.98795180724,358076.3253012048,543771.1485943776, 696853.9317269076]
ehyy = [85942.12851405622,194222.05220883535,382088.8473895582,599255.9959839358,792049.4417670682]
sy1 = [68326.76305220883,169270.15261044176,348558.5903614458,515240.1887550201,732189.0883534136]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Buddy dataset MSD to closest 3k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
x = [10,25,50,75,100]
az = [117478.0642570281,323131.3734939759,660750.1526104418,1000297.140562249, 1325071.7630522088]
ehyy = [143027.3172690763,382360.5823293173,737053.1646586346,1128473.3534136547,1530886.7028112449]
sy1 = [133575.28514056225,335360.2168674699,671936.3534136546,975415.4819277108, 1442436.5863453816]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Buddy dataset MSD to closest k centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

