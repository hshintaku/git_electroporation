# -*- coding: utf-8 -*-
# C:\Users\hirof\Anaconda3\Library\bin\pyuic5 -o gui_ui.pygui_main1.ui
import sys

import numpy as np
from NIDAQ_plt3 import AI as NI
import time
from PyQt5 import QtWidgets, QtCore
from gui_ui import Ui_MainWindow
from matplotlibwidget import MatplotlibWidget
class wavefunc():
    def wf1974(exposure, laser, dt):
        import visa
#        float exposure
#        float width1; float width2
        rm = visa.ResourceManager()
        # wv = rm.get_instrument("USB0::0x0D4A::0x000E::9137840::INSTR")
        wv = rm.get_instrument("USB0::0x0D4A::0x000D::9148960::INSTR")
        #print(wv.query('*IDN?'))
        wv.write(':SOURce1:VOLTage:LEVel:IMMediate:AMPLitude 5.0; OFFSet 2.5')
        # wv.write(':SOURce2:VOLTage:LEVel:IMMediate:AMPLitude 5.0; OFFSet 2.5')
        numofpulse=100
        numofpulse=str(numofpulse)
        wv.write(':SOURce1:BURSt:TRIGger:NCYCles '+ numofpulse)#number of cycles output onw
        # wv.write(':SOURce2:BURSt:TRIGger:NCYCles '+ numofpulse)#number of cycles output two
        wv.write(':SOURce1:FUNCtion:SHAPe PULSe')
        # wv.write(':SOURce2:FUNCtion:SHAPe PULSe')
        wv.write(':TRIGger1:BURSt:SOURce EXT')
        # wv.write(':TRIGger2:BURSt:SOURce EXT')
        width1=exposure-0.002
        width2=dt-laser
        delay=exposure-dt+laser/2
        wv.write(':SOURce1:PULSe:PERiod '+str(exposure)+'ms')#control the pulse period of output1
        # wv.write(':SOURce2:PULSe:PERiod '+str(dt)+'ms')#control the pulse period of output2
        wv.write(':SOURce1:PULSe:WIDTh '+str(width1)+'ms')#control the pulse width of output one
        # wv.write(':SOURce2:PULSe:WIDTh '+str(width2)+'ms')#control the pulse width of output two
        wv.write(':SOURce1:BURSt:TGATe:OSTop CYCLe')
        # wv.write(':SOURce2:BURSt:TGATe:OSTop CYCLe')
        # wv.write(':SOURce2:BURSt:SLEVel 100PCT')
        # wv.write(':SOURce2:PHAse:ADJust -180DEG')
        wv.write(':SOURce1:BURSt:TDELay 400ms')
        # wv.write(':SOURce2:BURSt:TDELay '+str(delay)+'ms')
        wv.write('OUTPut1:STATe ON')
        # wv.write('OUTPut2:STATe ON')
class MainWindow(QtWidgets.QMainWindow):    
    def __init__(self, parent=None):
        global ui
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.graphwidget = MatplotlibWidget(ui.centralwidget,title='', xlabel='Time', ylabel='Current',
                 xlim=None, ylim=None, xscale='linear', yscale='linear',
                 width=8, height=3, dpi=100)

        ui.graphwidget.axes = ui.graphwidget.figure.add_subplot(121)  
        ui.graphwidget.axes = ui.graphwidget.figure.add_subplot(122)   
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(50)
        ui.x=[]
        ui.y=[]
        ui.c=[]
        ui.save=False
        ui.valve=False
        ui.Filename="./"
        ui.value=0
        
        exposure=10
        laser=0.025
        dt=0.05
        ui.plainTextEdit_1.setPlainText(str(dt))
        ui.plainTextEdit_2.setPlainText(str(exposure))
        ui.plainTextEdit_3.setPlainText(str(laser))
        ui.plainTextEdit.setPlainText('1000')#interval
        ui.plainTextEdit_4.setPlainText('1')#number of pulsese
#        wavefunc.wf1974(exposure, laser, dt)
    def update_figure(self):
        #ui.graphwidget.clf
            
        x,y,c=NI.ArduinoAI(ui.x,ui.y,ui.c)
        c[1]=c[1]*0.1266-114.74
        c[2]=c[2]*0.1266-114.74
        c[3]=-(c[3]-204.6)/818.4*99-1
 
        if ui.save == True:
            
            # add Hiroyuki
            if ui.count != 0:
                # ui.count = 0で新規file open 
                ui.Ti = np.append(ui.Ti,c[0]-x[1])
                #print(ui.Ti)
                ui.CA1 = np.append(ui.CA1,c[1])
                ui.CA2 = np.append(ui.CA2,c[2])
                ui.CA3 = np.append(ui.CA3,c[3])
                ui.CA4 = np.append(ui.CA4,c[4])

                ui.graphwidget.axes = ui.graphwidget.figure.add_subplot(121)          
                ui.graphwidget.axes.clear()
                ui.graphwidget.x  = ui.Ti
                ui.graphwidget.y  = ui.CA1
                ui.graphwidget.axes.plot(ui.graphwidget.x,ui.graphwidget.y)
                ui.graphwidget.x  = ui.Ti
                ui.graphwidget.y  = ui.CA2
                ui.graphwidget.axes.plot(ui.graphwidget.x,ui.graphwidget.y)
                ui.graphwidget.x  = ui.Ti
                ui.graphwidget.y  = ui.CA3
                ui.graphwidget.axes.plot(ui.graphwidget.x,ui.graphwidget.y)
                ui.graphwidget.draw()
 
                ui.graphwidget.axes = ui.graphwidget.figure.add_subplot(122)       
                ui.graphwidget.axes.clear()
                ui.graphwidget.x  = ui.Ti
                ui.graphwidget.y  = ui.CA4
                ui.graphwidget.axes.plot(ui.graphwidget.x,ui.graphwidget.y)
                ui.graphwidget.draw()

                file = open(ui.Filename, 'a')

            else:
                ui.Ti = c[0]-x[1]
                ui.CA1  = c[1]
                ui.CA2  = c[2]
                ui.CA3  = c[3]
                ui.CA4  = c[4]
                
                file = open(ui.Filename, 'w')

                
            ui.count = ui.count + 1
            c[0] = c[0]-x[1]  #時間変換
            #
            #  record Display Time by Hiroyuki

            c[0]=round(c[0],6)
            for i in c:
                jp = (str(i))
                file.write(jp)
                file.write(',') # コンマ
            file.write('\n')  # 改行コード
            file.close()

            ui.c=[]
            
        else:
#            ui.x=[]
#            ui.y=[]
#            ui.c=[]
            ui.count = 0 # add Hiroyuki
#            x,y,c=NI.ArduinoAI(ui.x,ui.y,ui.c) # add Hiroyuki
            

        # counter Display
        #NI.ArduinoAO(ui.valve)
        ui.lcdNumber.display(c[1])
        ui.lcdNumber_2.display(c[2])
        ui.lcdNumber_3.display(c[3])
        ui.lcdNumber_4.display(c[4])

        
    def slot1(self):

        ui.save = not ui.save
        if ui.save == True:

            ui.Filename = NI.DefFile()
    
    def slot2(self):# valve on off
#        NI.NIDAQ_Stream()
        ui.valve = not ui.valve
        NI.ArduinoDO(ui.valve)
        #I.ArduinoAO(ui.valve, ui.value)
#    def slot3(self):
#        NI.NIDAQ_DO()       
    def slot4(self):
        exposure=float(ui.plainTextEdit_2.toPlainText())
        laser=float(ui.plainTextEdit_3.toPlainText())
        dt=float(ui.plainTextEdit_1.toPlainText())
        wavefunc.wf1974(exposure,laser,dt)
    def slot5(self):
        import visa
        interval=float(ui.plainTextEdit.toPlainText())
        number=int(ui.plainTextEdit_4.toPlainText())
        # NI.ArduinoDP(4,interval,1,number)
        rm = visa.ResourceManager()
        wv = rm.get_instrument("USB0::0x0D4A::0x000D::9148960::INSTR")
        wv.write("*TRG")
        for counter in range(number):
            # NI.NIDAQ_DO()
            data=NI.NIDAQ_Stream()
            time.sleep(interval/1000)
            ui.graphwidget.axes = ui.graphwidget.figure.add_subplot(122)       
            ui.graphwidget.axes.clear()
            ui.graphwidget.x  = np.arange(0,100,1)
        for counter in range(0,2):
            ui.graphwidget.y  = data[counter]
            ui.graphwidget.axes.plot(ui.graphwidget.x,ui.graphwidget.y)
        ui.graphwidget.draw()            
    def svalue_changed(self):
        ui.lcdNumber.display(ui.horizontalSlider_1.value())
        ui.lcdNumber_2.display(ui.horizontalSlider_2.value())
        ui.lcdNumber_3.display(ui.horizontalSlider_3.value())
        ui.lcdNumber_4.display(ui.horizontalSlider_4.value())
        ui.value = int(ui.horizontalSlider_1.value()*5000/99)
        #time.sleep(1)
        #ui.statusBar.showMessage(ui.horizontalSlider_1.value())
       

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())