#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 13:02:32 2022

@author: genzel
"""


import os, sys, json
import numpy as np
import pandas as pd
import mdaio
from scipy import signal
from scipy.signal import butter, lfilter
from timeit import default_timer as timer
from scipy.signal import butter, sosfilt, sosfreqz

def butter_bandpass(lowcut, highcut, fs, order=5):
        nyq = 0.5 * fs
        low = lowcut / nyq
        high = highcut / nyq
        sos = butter(order, [low, high], analog=False, btype='band', output='sos')
        return sos

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
        sos = butter_bandpass(lowcut, highcut, fs, order=order)
        y = sosfilt(sos, data)
        return y

directory = '/media/genzel/data/spikesorting/Rat/rat2/Rat_Hm_Ephys_Rat2_389237_20200915_postsleep.mountainsort/'
name = 'Rat_Hm_Ephys_Rat2_389237_20200915_postsleep.nt'
li = [3]
start = timer()
for i in li:
    postsleep = mdaio.readmda(directory+name+str(i)+'.mda')
    postsleep = postsleep[:,:108000000*4]
    postsleep = np.transpose(postsleep).astype(int)
    recording = pd.DataFrame()
    for j in range(4):
        fe = 30000
        f_nyq = fe/2
        fc1 = 1
        fc2 = 300
        recording1 = butter_bandpass_filter(postsleep[:, j], fc1, fc2, fe, order=5)
        q=10
        down1 = signal.decimate(recording1,q)
        q=5
        down1 = signal.decimate(down1,q)
        ch1 = pd.DataFrame(down1)
        recording = pd.concat([recording,ch1], axis=1)
    recording.columns = ['wavech1','wavech2','wavech3','wavech4']
    recording = recording.to_numpy()    
    recording = recording.transpose()
    mdaio.writemda16i(recording,name+'Down'+str(i)+'.mda')
end = timer()  
print(f'elapsed time: {end - start}')
