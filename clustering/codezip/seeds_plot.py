import matplotlib.pyplot as plt
import matplotlib.markers
hfont = {'fontname':'serif'}
x = [10,25,50,75,100]
az = [1.7489904613809526,0.7431595660476188,0.40653086619047624,0.22011032842857137,  0.17824235185714288]
ehyy = [1.5112113359047614, 0.6460062330952381,0.28521358495238086, 0.15060888709523815,0.08939819009523813]
sy1 = [ 1.2996052611904758,0.733682743809524, 0.3761177881428569,0.3436780520952382,0.144855633]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Seeds dataset MSD to closest 1 centroid")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,25,50,75,100]
az = [11.767578330047625,25.896822137619075,45.48695120219046,63.83029812338106,   81.97128928628568]
ehyy = [13.783298998190473, 34.79262753771426,53.08849794352384,75.95480317942852,94.45970506309496]
sy1 = [12.577680601952375,26.33539456276195,44.41395761533331,67.47918444447622,84.65922003052344]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Seeds dataset MSD to closest k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,25,50,75,100]
az = [40.78658989038091,121.21807809542865,210.6889069513811, 335.43966781061914,430.26943327976306]
ehyy = [45.3459333992858,133.36413761009518,227.7975508420481, 360.9734606798583,450.2248983770976]
sy1 = [39.51688218661908,110.3525300160954,213.2340373510476,334.39912939533184,430.93077872776274]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Seeds dataset MSD to closest k/2 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
x = [10,25,50,75,100]
az = [127.32730888261881, 311.77796679995186,615.4189723481429,933.0888208008099,1193.810132984901]
ehyy = [155.98336605471428,340.6465320907607,648.6187945468093,948.8048172414229,1231.0926797485624]
sy1 = [119.55697814447608,283.30484144957086,605.8896567191424,920.7390116838068,1197.9901392017591]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Seeds dataset MSD to closest 3k/4 centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()

x = [10,25,50,75,100]
az = [241.17209390047643,658.6136354711892, 1336.2235130785737,2028.5662808068994,2707.896716626101]
ehyy = [293.5051396648573,739.2021217491911,1395.6337684570508,2044.9532977547242,2776.4555297977226]
sy1 = [303.68412761814295, 680.9434756284778,1388.3053225458518,2083.8175469878115,2796.997007526621]

plt.plot(x,az, label = "Algorithm 1", linestyle = '--', marker = '^')
plt.plot(x,ehyy, label = "K means ++",linestyle = '-.', marker = 'o')
plt.plot(x,sy1, label = "Alg_g (Li et al (2021))",alpha = 1,lw = 1,linestyle = ':', marker = 's')
plt.title("Seeds dataset MSd to closest k centroids")
plt.xlabel("k",**hfont)
plt.ylabel("Mean Squared Error",**hfont)
plt.legend()
plt.show()
