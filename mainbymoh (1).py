import logging
import sys, os
import time
import qdarkstyle
import numpy as np
from audio2numpy import open_audio
import numpy as np
from pandas import Int16Dtype
from scipy.io.wavfile import write
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QUrl
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pyqtgraph as pg

import pyqtgraph
from pyqtgraph import PlotWidget
from Trial3_21 import Ui_MainWindow
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
import pygame
import sounddevice as sd
import soundfile as sf
from scipy.io import wavfile
import matplotlib.pyplot as plt
import cmath
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.figure=plt.figure()
        #self.canvas = FigureCanvas(self.figure)
        #self.axis=self.figure.add_subplot(111)
        #self.canvas.draw()
        #self.axis.set_xlabel("time (in seconds)")
        #self.axis.set_ylabel("frequency (Hz)")
        pygame.mixer.init()
        self.status="play"
        self.data=''#####3ashan akhod el oghnya ely hatdoos 3aleeha we ashaghlhaloo
        self.soundarray=[]
        self.initalizeddata=[]
        self.fs=44100 #initially default
        self.start=0.0
        self.Increment=0
        self.index=0
        self.newindex=3
        self.xylophonevol=100
        self.loopsvalue=0
        self.Volume_val=1 # betebteedy men 100 3ashan lama fata7t slider el volume fel winows la2eeto bade2 men 100
        test=[]
        self.timearray=[]
        self.soundarraytoplot=[]
        self.soundarray=[]
        self.timetoplot=[]
        self.fstoplot=0
        self.player = QMediaPlayer()

        self.ui.Music_listView.clicked.connect(self.list)## nady 3ala el function ba2aa
        self.ui.actionOpen.triggered.connect(lambda: self.load(0))
        self.ui.Start_pushButton.clicked.connect(lambda:self.changestatus())
        #self.ui.Pause_pushButton.clicked.connect(lambda: self.changestatus())
        self.ui.Instrument0_verticalSlider.valueChanged[int].connect(lambda:self.E_Update(0))
        self.ui.Instrument1_verticalSlider.valueChanged[int].connect(lambda:self.E_Update(1))
        self.ui.Instrument2_verticalSlider.valueChanged[int].connect(lambda:self.E_Update(2))
        self.ui.Volume_horizontalSlider.valueChanged[int].connect(self.changevolume)
        self.ui.Volume_horizontalSlider_xylo.valueChanged[int].connect(self.changexylovalue)#
        self.ui.looplineedit.returnPressed.connect(lambda: self.changeloopsxylo())#
        self.ui.comboBox.activated.connect(self.comboindex)
        #self.ui.checkBox.stateChanged.connect(self.Spectogram_hide)
        #self.ui.checkBox.setChecked(True)
        #Drums buttons
        self.ui.pushButton_Ride.clicked.connect(self.getsong)
        self.ui.pushButton_Hi.clicked.connect(self.getsong)
        self.ui.pushButton_Crash.clicked.connect(self.getsong)
        self.ui.pushButton_Base.clicked.connect(self.getsong)
        self.ui.pushButton_Snare.clicked.connect(self.getsong)
        self.ui.pushButton_FloorTom.clicked.connect(self.getsong)
        self.ui.pushButton_HiTom.clicked.connect(self.getsong)
        #Xylophne buttons
        self.ui.pushButton_chord_0.clicked.connect(self.getsong)
        self.ui.pushButton_chord_1.clicked.connect(self.getsong)
        self.ui.pushButton_chord_2.clicked.connect(self.getsong)
        self.ui.pushButton_chord_3.clicked.connect(self.getsong)
        self.ui.pushButton_chord_4.clicked.connect(self.getsong)
        self.ui.pushButton_chord_5.clicked.connect(self.getsong)
        self.ui.pushButton_chord_6.clicked.connect(self.getsong)
        self.ui.pushButton_chord_7.clicked.connect(self.getsong)
        self.ui.pushButtonPianoleft1.clicked.connect(lambda:self.buttoncall('C',self.newindex))
        self.ui.pushButtonPianoleft2.clicked.connect(lambda:self.buttoncall('D',self.newindex))
        self.ui.pushButtonPianoleft3.clicked.connect(lambda:self.buttoncall('E',self.newindex))
        self.ui.pushButtonPianoleft4.clicked.connect(lambda:self.buttoncall('F',self.newindex))
        self.ui.pushButtonPianoleft5.clicked.connect(lambda:self.buttoncall('G',self.newindex))
        self.ui.pushButtonPianoleft6.clicked.connect(lambda:self.buttoncall('A',self.newindex))
        self.ui.pushButtonPianoleft7.clicked.connect(lambda:self.buttoncall('B',self.newindex))
        #black buttons
        self.ui.pushButtonPianoleftblack1.clicked.connect(lambda:self.buttoncall('C#',self.newindex))
        self.ui.pushButtonPianoleftblack2.clicked.connect(lambda:self.buttoncall('D#',self.newindex))
        self.ui.pushButtonPianoleftblack3.clicked.connect(lambda:self.buttoncall('F#',self.newindex))
        self.ui.pushButtonPianoleftblack4.clicked.connect(lambda:self.buttoncall('G#',self.newindex))
        self.ui.pushButtonPianoleftblack5.clicked.connect(lambda:self.buttoncall('A#',self.newindex))
        

    def comboindex(self):        
        self.index=self.ui.comboBox.currentIndex()
        print(self.index)
        self.newindex=self.index+3
        print(self.newindex)
        #white buttons on Piano
       

    def buttoncall(self,alpha,level):#for piano only
        print("Hello there !")
        print(alpha)
        print(level)
        self.filename=str(alpha)+str(level)+'.'+'wav'
        full_file_path = os.path.join(os.getcwd(),self.filename)
        #print(os.getcwd())
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)
        self.player.play()
         

    def changexylovalue(self):
        self.xylophonevol=self.ui.Volume_horizontalSlider_xylo.value()

    def changeloopsxylo(self):
        self.loopsvalue=int(self.ui.looplineedit.text())  
        print("loops value gowa el func:",self.loopsvalue)  
    

    def getsong(self): #for xylophone and drums
        textmsg = self.sender()
        print(textmsg.text())
        self.filevar=textmsg.text()
        self.filename= str(self.filevar)+'.'+'wav'
        full_file_path = os.path.join(os.getcwd(),self.filename)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        #self.player.setMedia(content)
        #self.player.setVolume(1000)
        #self.player.play()
        pygame.mixer.music.load(full_file_path)#load the sound signal then play
        pygame.mixer.music.play(loops=self.loopsvalue)
        pygame.mixer.music.set_volume(self.xylophonevol/100)





    def load(self,n):
        if(n==0):
            self.path = QFileDialog.getOpenFileName(self, 'Open a file', '')

        if (self.path != ('', '') or n==1):
            if (n==0):
                self.data = self.path[0]
            #self.sound= pygame.mixer.Sound(self.data)#to get the sound signal as an array
            #self.soundarray=pygame.sndarray.array(self.sound)#to get the sound signal as an array contnd.
            #test= pygame.sndarray.samples(self.sound)
            #print("testing pygame sampling: ",len(test),test)
            self.soundarraytoplot, self.fstoplot = sf.read(self.data) ## to read it as an array and so we can plot it
            print("data file path: ",self.data )
            self.fs ,self.soundarray= wavfile.read(self.data) # to read the file and can hear it 
            self.timearray=np.linspace(0,len(self.soundarray)/self.fs,num=len(self.soundarray))
            self.timetoplot=self.timearray
            #print('Ana hena ahoooooooooooo')
            #print('sound array loaded: ',len(self.soundarray),self.soundarray)
            #print('time array generated: ',len(self.timearray),self.timearray)
            pygame.mixer.music.load(self.data)#load the sound signal then play
            pygame.mixer.music.play(loops=0)
            if (n==0):
                self.ui.Music_listView.addItem(self.data)
            self.start=time.time()
            #print("File path: " + self.data)
            #self.sr, self.x = read(self.data)
            #fp = self.data  # change to the correct path to your file accordingly
            #self.signal, self.sampling_rate = open_audio(fp)

            #print(self.signal)
            #print(self.sampling_rate)
            #self.ui.Soundsignal_graphicsView.plot(self.timearray,self.soundarray)
            self.ui.Soundsignal_graphicsView.clear()
            self.Increment=0
            self.AddPlot()
            self.AddSpecgram(self.soundarray)


            # write('os .wav', 44100, self.signal)



    def changevolume(self):
        self.ui.Volume_horizontalSlider.value()
        self.ui.Volume_lcdNumber.display(self.ui.Volume_horizontalSlider.value())
        self.Volume_val=self.ui.Volume_horizontalSlider.value()/100
        pygame.mixer.music.set_volume(self.ui.Volume_horizontalSlider.value()/100)
        # song = AudioSegment.from_mp3(self.data)

        #     # boost volume by 6dB
        # self.louder_song = song + (self.ui.Volume_horizontalSlider.value()/10)

        #     # reduce volume by 3dB
        # self.quieter_song = song - (self.ui.Volume_horizontalSlider.value()/10)

        #     #Play song
        # play(self.louder_song)


    def changestatus(self):
        #if d==0:
        if ("Paused"==self.ui.Start_pushButton.text()):
            #playsound(data,True)
            self.status='play'
            self.ui.Start_pushButton.setText("Playing")
            pygame.mixer.music.unpause()
        else:
            #playsound(data,False)
            pygame.mixer.music.pause()
            self.status="pause"
            self.ui.Start_pushButton.setText("Paused")
        

    def E_Update(self,event):
        if event==0:
            self.ui.Instrument0_lcdNumber.display(self.ui.Instrument0_verticalSlider.value())
            self.Emphasize(self.soundarray,self.ui.Instrument0_verticalSlider.value(),0)
        elif event==1:
            self.ui.Instrument1_lcdNumber.display(self.ui.Instrument1_verticalSlider.value())
            self.Emphasize(self.soundarray,self.ui.Instrument1_verticalSlider.value(),1)
        elif event==2:
            self.ui.Instrument2_lcdNumber.display(self.ui.Instrument2_verticalSlider.value())
            self.Emphasize(self.soundarray,self.ui.Instrument2_verticalSlider.value(),2)

    def Emphasize(self, arrayofsound, slidervalue, Instrumentno):
        self.gaintimesfourier=[]
        maxfreq=[1050, 302, 10346]#el max values btoo3 kol instrument 
        minfreq=[200, 35, 1060]# el min values btoo3 kol instrument 
        self.soundarrayinequalization = arrayofsound / 2.0 ** 15 #32 bit
        self.soundfourier=np.fft.rfft(self.soundarrayinequalization)
        self.soundfrequency=np.fft.rfftfreq(len(self.soundarrayinequalization), 1/self.fs)
        print("sound array: ", len(self.soundarrayinequalization),self.soundarrayinequalization)

        gain=(10)**(slidervalue/20)# 20log(10)(gain)=db

        rangeFreq = (self.soundfrequency >= minfreq[Instrumentno]) & (self.soundfrequency <= maxfreq[Instrumentno])
        self.soundfourier[rangeFreq] *= gain

        self.fileloadedattime=pygame.mixer.music.get_pos()  # in milli seconds
        self.fileloadedattime=self.fileloadedattime*0.001   # in seconds
        index=np.searchsorted(self.timearray,self.fileloadedattime)
        print("Index: ", index)
        print("Time:", self.fileloadedattime)
        self.gainsound=np.fft.irfft(self.soundfourier)
        #self.soundarray=self.gainsound
        self.gainsound=self.gainsound[index:]
        print("sound sound after filtering: ",len(self.gainsound), self.gainsound)
        pygame.mixer.music.unload()
        pygame.mixer.music.stop()
        sf.write('myfile.wav', self.gainsound, self.fs)
        self.fs ,self.soundarray= wavfile.read('myfile.wav') # to read the file and can hear it
        #self.fs2 ,self.soundarray2= wavfile.read(self.data)#just for testing that the file is not empty
        #print(len(self.soundarray2),self.soundarray2)
        #self.soundarray=self.gainsound
        pygame.mixer.music.load(r'myfile.wav')#load the sound signal then play
        pygame.mixer.music.play(loops=0)
        self.AddSpecgram(self.soundarray,1)


    def Anotation(self,ENDTIME=None):
        if ENDTIME:
            self.end=ENDTIME
            start=int((self.end-self.start)/0.0000228)
            data=self.soundarray[start:]
            return  data
        else:
            self.end=time.time()
            start=int((self.end-self.start)/0.0000228)
            data=self.soundarray[start:]
            return  data

    def list(self):
        self.data=self.ui.Music_listView.currentItem().text()
        self.load(1)
        #print(self.clickedpath)        

    def AddPlot(self):
        print("AnA gowa om el plot")
        self.plotline=self.ui.Soundsignal_graphicsView.plot(self.timetoplot[:self.Increment],self.soundarraytoplot[:self.Increment]*(self.Volume_val),pen='g')
        self.timer1 = QtCore.QTimer()
        self.timer1.timeout.connect(self.update)
        self.timer1.start(40)

    def update(self):
        if self.status=='play':
            self.Increment += 40000#1770#40/(1000*(1/44100))
            self.ui.Soundsignal_graphicsView.setLimits(xMin=min(self.timetoplot), xMax=max(self.timetoplot),minXRange=0, maxXRange=10000000000,yMin=min(self.soundarraytoplot), yMax=max(self.soundarraytoplot))
            self.plotline.setData(self.timetoplot[:self.Increment],self.soundarraytoplot[:self.Increment])
            print("Gowa el update len el xaxis: ",len(self.timetoplot[:self.Increment]))
            self.ui.Soundsignal_graphicsView.setAutoPan(x=True)

    def AddSpecgram(self,array,Upadteme=None):
        if Upadteme:
            self.ui.axis.cla()              
            self.ui.axis.specgram(array,Fs=self.fs,Fc=None, detrend=None, window=None, noverlap=None, cmap='magma')
            self.ui.canvas.draw()
            self.Temp_Spectrogram=array
        else:
            self.ui.axis.specgram(array,Fs=self.fs)
            self.ui.canvas.draw()
            self.Temp_Spectrogram=array

    # def  Spectogram_hide(self):  
        
    #     if self.ui.checkBox.isChecked():
    #         self.ui.axis.clear()
    #         self.ui.axis.specgram(self.Temp_Spectrogram,Fs=self.fs)
    #         self.ui.canvas.draw()
    #     else:
    #         self.ui.axis.clear()
    #         self.ui.canvas.draw()

    # def generatesound(self):
    #     print("ana gowaaa")
    #     if (0):



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    win.show()
    sys.exit(app.exec_())