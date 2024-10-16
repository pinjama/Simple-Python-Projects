import numpy as np
import matplotlib.pyplot as plt

n = [500,1000,2000,5000,10000,15000,20000,50000,100000]

#for-loop käy läpi eri n-luvut
for x in n:
    sumlist=[]

    #heittää noppia tietyn n-luvun verran, tallentaa listaan summat ja for-loopin jälkeen piirtää histogrammin
    for i in range(x):
        dice1 = np.random.randint(1,7)
        dice2 = np.random.randint(1,7)
        sum=dice1+dice2
        sumlist.append(sum)

    s = np.array(sumlist)

    h,h2 = np.histogram(s,range(2,14)) #histogrammi arrayn tiedoilla tallentuu kahteen muuttujaan
    plt.bar(h2[:-1],h/x) #esitetään histogrammi palkkeina, toinen on mahdolliset akseli summat ja toinen todennäköisyys
    plt.title("n="+str(x))
    plt.show()
