from can import Message
from can.interfaces.ixxat import IXXATBus, exceptions


class Fetch:
    rate = 500000
    try:
        bus = IXXATBus(channel=0, can_filters=[{"can_id": 0x000, "can_mask": 0x000}], bitrate=rate)
    except exceptions.VCIDeviceNotFoundError:
        bus = None
    count = 0

    def __init__(self):
        self.bus = Fetch.bus
        self.message = Message(is_extended_id=False, arbitration_id=0xfff, dlc=8,
                               data=[0, 0, 0, 0, 0, 0, 0, 0])