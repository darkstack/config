#!/ssd/src/artik/bin/python
import struct
import usb.core
import usb.util

dev = usb.core.find(idVendor=0x1d57, idProduct=0xfa60)
ep = dev[0].interfaces()[2].endpoints()[0]
def get_mouse_battery():
    if dev is None: 
        raise ValueError("Not found") 
    if dev.is_kernel_driver_active(0x2):
        dev.detach_kernel_driver(0x2)
    for i in range(10):
        try:
            iret = dev.read(ep.bEndpointAddress,5,100)
            val = struct.Struct('<IB')
            value = val.unpack(bytes(iret))
            print(value[1]*10,"%")
            return 0
        except Exception as error:
            pass
    print("Plugged?")
get_mouse_battery()
