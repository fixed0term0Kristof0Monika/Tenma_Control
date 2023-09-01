from tenma_control import Tenm

import time

pwsupp = Tenm()
print("Power supply version: ",pwsupp.version())
pwsupp.setV(21.33)
pwsupp.setC(2.311)
print("Current: ",pwsupp.getC())
print("Voltage: ", pwsupp.getV())
pwsupp.tenma_on()
time.sleep(3)
pwsupp.tenma_off()