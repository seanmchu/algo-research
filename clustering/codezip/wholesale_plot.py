import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [10,30,50,100,150]
az = [121814006.93863636,104079280.20681818,104754508.21363637,86775698.94318181,68751782.47954546]
ehyy = [107528599.79772727,33745194.45,19820876.802272726,8969732.295454545,4822555.94090909]
sy1 = [129780381.76818182,125350805.32954545,107494390.26136364,67935437.48863636,37729373.29545455]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Wholesale dataset, MSD to closest 1 centroid")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,30,50,100,150]
az = [644628478.9909091, 1775954094.790909,2880760614.640909,5569138670.247727,8553704247.572727]
ehyy = [774220351.7181818,1828651609.5772727,2810869697.197727,5146320705.4,7748297164.790909]
sy1 = [651708592.425,1749233750.2113636,2812027525.2477274,5299474140.356818,7929253734.190909]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Wholesale dataset, MSD to closest k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,30,50,100,150]
az = [1499895725.0113637,4597719848.35,7676680198.168181,15517758938.704546,23458101856.74091]
ehyy = [2432478665.740909,6539080880.522727,9990745745.679546,18245880509.668182,25238952407.095455]
sy1 = [1472637948.0454545,4521137421.263637,7463251732.577272,14927874181.90909,22754747267.08409]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Wholesale dataset, MSD to closest k/2 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,30,50,100,150]
az = [3357305106.990909,9116402506.620455,15064204210.152273,29601242241.127274,82990385884.60454]
ehyy = [12171759285.845455, 21874063175.677273,26431045526.211365,42613633708.41136,168001508104.43182]
sy1 = [3358743093.840909,9168507471.377274,14713239420.038637,29199705861.55682,103659128149.27272]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Wholesale dataset, MSD to closest 3k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()



x = [10,30,50,100,150]
az = [6740417876.609091,16202260064.018183,26914841481.02727,53991375165.48182,82990385884.60454]
ehyy = [29631326642.618183,72901544418.23636,94457311299.26364,136547006252.77272,168001508104.43182]
sy1 = [5841941639.054545,16105179666.65909,27541627575.552273,60819824757.31591,114399786376.84319]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Wholesale dataset, MSD to closest k centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

