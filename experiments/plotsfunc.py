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
    

def comparaMedias(database, field, categories):

    means=[]
    stds=[]
    labels=[]

    for category in categories:
        means.append(database[database.category == category][field].mean())
        stds.append(database[database.category == category][field].std())
        labels.append(category)
    
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


def plot_corr(df,size=10):
    '''Function plots a graphical correlation matrix for each pair of columns in the dataframe.

    Input:
        df: pandas DataFrame
        size: vertical and horizontal size of the plot'''

    corr = df.corr()
    fig, ax = plt.subplots(figsize=(size, size))
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90);
    plt.yticks(range(len(corr.columns)), corr.columns);