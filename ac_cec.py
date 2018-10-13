import cec

cec.init()

tv = cec.Device(cec.CECDEVICE_TV)

def turn_on_tv():
    tv.power_on()

