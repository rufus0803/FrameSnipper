import usb.core
import usb.util


dev = usb.core.find(idVendor=0x1bcd, idProduct=0x0215)

if dev is None:
    raise ValueError('Device not found')


dev.set_configuration()


cfg = dev.get_active_configuration()
intf = cfg[(0,0)]


ep = usb.util.find_descriptor(
    intf,
    custom_match=lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN
)

assert ep is not None


while True:
    try:
        data = dev.read(ep.bEndpointAddress, ep.wMaxPacketSize)
        print("Data read from USB device:", data)
    except usb.core.USBError as e:
        if e.args == ('Operation timed out',):
            continue
        print("USB error:", e)
        break
