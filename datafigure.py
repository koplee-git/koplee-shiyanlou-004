#!/usr/bin/env python3
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analysis(file):
    dic={}
    times = 0
    minutes = 0
    df = pd.read_json(file,typ='frame')
    for user_id in df['user_id']:
        minutes = df[df['user_id']==user_id]['minutes'].sum()
        dic[str(user_id)] = minutes
    return dic
def show(dic):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.set_title('StudyData')
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    pd.Series(dic,index=dic.keys()).plot()
    plt.show()
if __name__ =="__main__":
    print(analysis('/home/shiyanlou/Code/user_study.json'))
    dic=analysis('/home/shiyanlou/Code/user_study.json')
    show(dic)
