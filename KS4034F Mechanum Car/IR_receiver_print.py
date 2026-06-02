from microbit import *
from IR_receiver_class import NECDecode

nec = NECDecode(pin0)

while True:
    result = nec.decode_nec()
    
    addr, cmd = result if isinstance(result, tuple) else (None, None)
    if cmd is not None:
        nec.print_info()