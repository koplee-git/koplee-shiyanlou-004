from pandas import offsets
import pandas as pd


def quarter_volume():
    alldata = pd.read_csv('apple.csv', header=0)
    timeindex =pd.to_datetime(alldata.Date)
    timeindexdata = alldata.Volume.rename(timeindex)
    sampledata = timeindexdata.resample("3MS",convention='start').sum()
    #sampledata = timeindexdata.resample("Q",convention='start').sum()
    result = sampledata.sort_values()
    return result[-2]

if __name__ == '__main__':
    print(quarter_volume())
