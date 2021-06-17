# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:05:26 2021

@author: Lab
"""
import sys
import os

import numpy as np
from NIDAQ_plt3 import AI as NI
import time, datetime
import matplotlib.pyplot as plt
import pyvisa as visa
import schedule

class wavefunc():
    def wf1974(voltage, pulse,period,num_cycl):
#        import visa
#        float exposure
#        float width1; float width2
        rm = visa.ResourceManager()
        # wv = rm.get_instrument("USB0::0x0D4A::0x000E::9137840::INSTR")
        wv = rm.open_resource("USB0::0x0D4A::0x000D::9148960::INSTR")
        #print(wv.query('*IDN?'))
        wv.write(':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude '+ str(voltage) +'; OFFSet '+ str(voltage/2))
        # wv.write(':SOURce2:VOLTage:LEVel:IMMediate:AMPLitude 5.0; OFFSet 2.5')
        wv.write(':SOURce1:BURSt:TRIGger:NCYCles '+ str(num_cycl))#number of cycles output onw
        # wv.write(':SOURce2:BURSt:TRIGger:NCYCles '+ numofpulse)#number of cycles output two
        wv.write(':SOURce1:FUNCtion:SHAPe PULSe')
        # wv.write(':SOURce2:FUNCtion:SHAPe PULSe')
        wv.write(':TRIGger1:BURSt:SOURce EXT')
        # wv.write(':TRIGger2:BURSt:SOURce EXT')
        
        wv.write(':SOURce1:PULSe:PERiod '+str(period)+'ms')#control the pulse period of output1
        # wv.write(':SOURce2:PULSe:PERiod '+str(dt)+'ms')#control the pulse period of output2
        wv.write(':SOURce1:PULSe:WIDTh '+str(pulse)+'ms')#control the pulse width of output one
        # wv.write(':SOURce2:PULSe:WIDTh '+str(width2)+'ms')#control the pulse width of output two
        wv.write(':SOURce1:BURSt:TGATe:OSTop CYCLe')
        # wv.write(':SOURce2:BURSt:TGATe:OSTop CYCLe')
        wv.write(':SOURce1:BURSt:SLEVel:STATe ON')
        wv.write(':SOURce1:BURSt:SLEVel -100PCT')
        # wv.write(':SOURce2:PHAse:ADJust -180DEG')
        wv.write(':SOURce1:BURSt:TDELay 400ms')
        # wv.write(':SOURce2:BURSt:TDELay '+str(delay)+'ms')
        wv.write('OUTPut1:STATe ON')
        # wv.write('OUTPut2:STATe ON')

def update_figure(ch_num,smpl,rate):
    import time
    smpltime=time.time()
    data=NI.NIDAQ_Stream(ch_num,smpl,rate)
    return data

def NF_triger():
    rm = visa.ResourceManager()
    wv = rm.open_resource("USB0::0x0D4A::0x000D::9148960::INSTR")
    wv.write("*TRG")
    print("Trigerred")
    
def DefFile(): # Making Folder for saving this result
    FolderName1 = 'C:/Users/Lab/Documents/Github/git_electroporation/Data'        
    FolderName1=FolderName1+"/"+str(datetime.datetime.today().strftime("%Y%m%d"))
    os.makedirs(FolderName1,exist_ok=True)
    FileName=str(datetime.datetime.
                     today().strftime("%Y%m%d_%H%M%S"))+'_exp'
    FileName1=FolderName1+"/"+FileName+str(1+len([x for x in os.listdir(FolderName1) if x.endswith(".csv")])).zfill(4)
    return(FileName1)

def job():
    count = 0
    # Start recording
    import time
    smpltime=time.time()
    stime=smpltime
    ch_num=3
    rate=1000
    smpl=1000
    Filename = DefFile()
    print("Job")
    
    while (count < duration_rec + 10):
        data=NI.NIDAQ_Stream(ch_num,smpl,rate)
        
        # Plot
        x = np.arange(0,smpl,1)
        for counter2 in range(0,ch_num-1):
            y  = data[counter2]
            plt.plot(x,y)
        plt.draw()
            
        plt.pause(1)
        plt.cla()
        
        # Save
        smpltime=time.time()
        smpltime=smpltime-stime
        duration=float(smpl)/float(rate) #second
        stamp=np.linspace(smpltime,smpltime+duration,smpl)
        data=np.vstack([stamp,data])
        with open(Filename,'a') as f_handle:
            np.savetxt(f_handle,data.T,delimiter=',')
        if count == 5:
            NF_triger()
        count = count + 1
    print("End")


# Main

# Set parameters
voltage=5   # [V]
pulse=5     # [ms]
frequency=20    # [Hz]
period=1000/frequency
num_cycl=100
duration_rec = int(num_cycl/frequency)

ch_num=3
rate=1000
smpl=1000

save = False
count = 0

# Send to function generator
wavefunc.wf1974(voltage, pulse, period,num_cycl)

# Set sheduled job
schedule.every(2).hour.do(job)

plt.figure()

time.sleep(60)
print('Start firts ELP')
job()

while True:
    schedule.run_pending()
    
    # Plot
    x = np.arange(0,smpl,1)
    data = update_figure(ch_num,smpl,rate)
    for counter2 in range(0,ch_num-1):
        y  = data[counter2]
        plt.plot(x,y)
    plt.draw()
    
    # Remaining time
    time_remain = schedule.idle_seconds()
    print('Next: '+str(time_remain)+'sec')
            
    plt.pause(1)
    plt.cla()




        
