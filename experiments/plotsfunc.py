import numpy as np
import matplotlib.pyplot as plt

def comparasionWithBoxPlot(field):
    a={}
    a['chcall']= chcall[field]
    a['folhaall']= folhaall[field]
    a['fapespall']=fapespall[field]

    a = pd.DataFrame(a)    
    a.plot(kind='box')
    #.plot(kind='box')
    

def comparaMedias(database, field):
    means=[database[field].mean()]
    stds=[database[field].std()]


    labels = ["Reviews"]
    ind = np.arange(len(means))
    width = 0.25
    colours = ['red','blue','green','yellow']

    plt.figure()
    
    for i in range(len(means)):
        plt.bar(ind[i],means[i],width,color=colours[i],align='center',yerr=stds[i],ecolor='k')
    
    plt.xticks(ind,labels)

    def autolabel(bars,peakval):
        for ii,bar in enumerate(bars):
            height = bars[ii]
            plt.text(ind[ii], height*1.01, '%f'% (means[ii]), ha='center', va='bottom')
    autolabel(means,means)  
    
    plt.title(field)
    plt.ylabel('Mean')
    plt.show()