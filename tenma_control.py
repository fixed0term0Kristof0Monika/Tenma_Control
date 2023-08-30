
# source Tenma API: https://tenma-serial.readthedocs.io/en/latest/library/api.html

from tenma import Tenma72_2540
import time

class Tenm:
    def __init__(self):
        try:
            #for innitializing one should use the power supply name and the serial communication port name
            self.tenma = Tenma72_2540("COM3") 
        except:
            print("Couldn't find com port")
       
            
    def version(self):
        return self.tenma.getVersion() 
        
    def setV(self, voltage):
        try:
            voltage = voltage*1000
            self.tenma.setVoltage(1, voltage)
        except:
            print("Couldn't set voltage")
        
    def setC(self, current):
        try:
            # this function takes mA and mV, so it has to be converted in ampers and volts
            current= current*1000
            self.tenma.setCurrent(1,current)
        except:
            print("Couldn't set current")
        
    def tenma_off(self):
        try:
            self.tenma.OFF()
        except:
            print("Couldn't set current")
    
    def tenma_on(self):
        try:
            self.tenma.ON()  
        except:
            print("Couldn't set current")
        
    def  getV(self):
        try:
            return float(self.tenma.readVoltage(1))
        except:
            print("Can't read voltage")
     
    def getC(self):
        try:
            return self.tenma.readCurrent(1)  
        except:
            print("Can't read current")
           
pwsupp = Tenm()
print("Power supply version: ",pwsupp.version())
pwsupp.setV(21.33)
pwsupp.setC(2.311)
print("Current: ",pwsupp.getC())
print("Voltage: ", pwsupp.getV())
pwsupp.tenma_on()
time.sleep(3)
pwsupp.tenma_off()