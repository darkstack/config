#!/bin/env python3
import hid 
import struct
import time
class EvisionDeviceConfig:
    def __init__(self,path) -> None:
        self.path=path 
        self.device = [None]*len(path)
    
    def __repr__(self):
        return "<{0}: {1!r}>".format(self.__class__.__name__, self.path)

    def get(self, dev):
        if self.device[dev] is not None:
            return self.device[dev]
    
        d = hid.device()
        d.open_path(self.path[dev])
        self.device[dev] = d
        d.set_nonblocking(1)
        return d

    def checksum(self,cmd,data):
        checksum = 0
        return checksum
    
    def read(self,id,len_data):
        dev = self.get(id)
        data = dev.read(5,5000);
        if data is not None and len(data) == 5:
            val = struct.Struct('<IB')
            value = val.unpack(bytes(data))
            print(value[1]*10)

def enumerate_x3():
    interface = {}
    for d in hid.enumerate(0x1d57,0xfa60):
        interface[d['interface_number']]= d['path']
    return interface

interface_config = enumerate_x3()
mouse = EvisionDeviceConfig(interface_config)
mouse.read(2,5)
