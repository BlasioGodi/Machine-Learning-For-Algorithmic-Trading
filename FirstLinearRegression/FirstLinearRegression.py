#import environments
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

#Define datapath and dataframe for analysis
datapath = r"C:\Users\user\Desktop\GOLD DATA\Results History.csv"
datafile = pd.read_csv(datapath)

print(datafile.shape)
datafile.head()

#Prepare data set and plotting information 
datasets = datafile.iloc[:,0:]
sb.pairplot(datasets,diag_kind="kde")

plt.show()