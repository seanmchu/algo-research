import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [10,50,100,200,300]
az = [6424.927458699188,5256.961421300812,4824.796510406505,4397.427268292684,   4197.789814796751]
ehyy = [2687.6435760975614,703.1398154471545,395.1273873170729,176.83760829268292,96.1307951219512]
sy1 = [5950.18102292683,5429.365800162603,5357.318395284554,3713.241357886179, 1030.814495934959]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("HCV dataset MSD to closest 1 centroid")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,50,100,200,300]
az = [22599.34653902439,97812.89526000009,187036.21684812993,378262.2334604881,  566806.8513998397]
ehyy = [36212.48968162593,82880.21971105676, 158791.86747674804,332972.78833723604,517099.0014863425]
sy1 = [21334.92608000001,94810.5209027642,187488.04654211353,370964.4004476427, 546504.439231384]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("HCV dataset MSD to closest k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,50,100,200,300]
az = [40646.39921203251,210525.6406530079,420680.6237029261, 845481.3138406522,1269583.7324663412]
ehyy = [124083.99631951218,250374.9208278043,456286.41397723474, 836773.9932816271,1244285.030423903]
sy1 = [39792.15618878047,204902.3652287808,417640.0921939826,  834974.7590915464,1253336.3079403285]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("HCV dataset MSD to closest k/2 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,50,100,200,300]
az = [72695.57247934972,352127.7569616262,687734.710200163, 1376151.7893491015,2068289.1842294286]
ehyy = [546103.3082318715,760492.1637795137,1049141.8591156001, 1599424.9191099254,2194639.542871545]
sy1 = [78556.98748878039,342924.19081626035, 679900.7061354463, 1369637.1033647123,2075300.3888624338]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("HCV dataset MSD to closest 3k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,50,100,200,300]
az = [186052.680976585,542861.3294081311,1087538.5383058526,2167896.5648702616, 3293183.467976578]
ehyy = [1767480.8965390252,3788476.3237751373,5046475.590147337,6293318.208938536,7396493.75954102]
sy1 = [117938.62972097572, 535679.1609764224,1071021.4954299207,2434362.110899358,  5088374.6236155545]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("HCV dataset MSD to closest k centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
