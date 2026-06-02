# ──────────────────────────────────────────────────────────
#  NEC IR Remote Decoder for BBC micro:bit  (MicroPython)
#
#  Wiring  (typical TSOP1738 / VS1838B / HX1838 module):
#     IR receiver OUT  →  micro:bit pin0
#     IR receiver VCC  →  micro:bit 3V
#     IR receiver GND  →  micro:bit GND
#
#  The receiver idles HIGH and pulls LOW during IR bursts.
#
#  NEC frame format (all times approximate):
#  ┌─────────┐         ┌───┐ ┌───┐   ┌───┐ ┌─────┐
#  │  9 ms   │ 4.5 ms  │562│ │562│   │562│ │1688 │ ...
#  │  LOW    │  HIGH   │LOW│ │LOW│   │LOW│ │ HIGH│
#  └─────────┘         └───┘ └───┘   └───┘ └─────┘
#   AGC burst  AGC space  bit "0"       bit "1"
#
#  32 bits sent LSB-first:
#    [ address 8-bit ] [ address inverted 8-bit ]
#    [ command 8-bit ] [ command inverted 8-bit ]
#
#  Extended NEC uses a full 16-bit address (no inversion).
#  Repeat code: 9 ms burst + 2.25 ms space + 562 µs burst.
# ──────────────────────────────────────────────────────────

from microbit import *
import utime

class NECDecode():
    def __init__(self, pin):
        self.pin = pin
        self.last_addr = 0
        self.last_cmd = 0
        self.addr = 0
        self.cmd = 0

    def decode_nec(self):
        """
        Block until a complete NEC IR frame (or repeat code) is
        captured on *pin*, then return the decoded result.

        Returns
        -------
        (int, int)  – (address, command) on a valid data frame.
        "REPEAT"    – when a repeat burst is detected.
        None        – when decoding fails (noise / bad timing).
        """

        pin = self.pin

        # ── 1. Synchronise: make sure the line is idle (HIGH) ──
        t = utime.ticks_us()
        while pin.read_digital() == 0:
            if utime.ticks_diff(utime.ticks_us(), t) > 15000:
                return None                        # line stuck LOW

        # ── 2. Wait for the AGC burst to begin (first falling edge) ──
        while pin.read_digital() == 1:
            pass                                   # blocks until signal

        # ── 3. Measure AGC burst (LOW, expect ≈ 9 000 µs) ──
        t = utime.ticks_us()
        while pin.read_digital() == 0:
            if utime.ticks_diff(utime.ticks_us(), t) > 12000:
                return None
        agc_burst = utime.ticks_diff(utime.ticks_us(), t)

        if not (7000 < agc_burst < 11000):
            return None

        # ── 4. Measure AGC space (HIGH) ──
        #       ≈ 4 500 µs → data frame
        #       ≈ 2 250 µs → repeat code
        t = utime.ticks_us()
        while pin.read_digital() == 1:
            if utime.ticks_diff(utime.ticks_us(), t) > 6000:
                return None
        agc_space = utime.ticks_diff(utime.ticks_us(), t)

        if agc_space < 3000:                       # short space → repeat
            return "REPEAT"
        if not (3500 < agc_space < 5500):
            return None

        # ── 5. Read 32 data bits (LSB first) ──
        raw = 0
        for i in range(32):

            # — bit mark: LOW burst ≈ 562 µs —
            t = utime.ticks_us()
            while pin.read_digital() == 0:
                if utime.ticks_diff(utime.ticks_us(), t) > 1500:
                    return None

            # — bit space: HIGH ≈ 562 µs → '0', ≈ 1 688 µs → '1' —
            t = utime.ticks_us()
            while pin.read_digital() == 1:
                if utime.ticks_diff(utime.ticks_us(), t) > 3000:
                    return None
            space = utime.ticks_diff(utime.ticks_us(), t)

            if space > 1100:                       # threshold between 0 and 1
                raw |= 1 << i

        # ── 6. Parse the 32-bit word ──
        addr     =  raw        & 0xFF
        addr_inv = (raw >>  8) & 0xFF
        cmd      = (raw >> 16) & 0xFF
        cmd_inv  = (raw >> 24) & 0xFF

        # Validate command (inverted byte must be the complement)
        if cmd ^ cmd_inv != 0xFF:
            return None

        # Standard NEC: 8-bit address (addr + addr_inv are complements)
        # Extended NEC: 16-bit address (addr + addr_inv are independent)
        if addr ^ addr_inv == 0xFF:
            self.addr = addr
            self.cmd = cmd
            return (addr, cmd)
        else:
            self.addr = addr | (addr_inv << 8)
            self.cmd = cmd
            return (addr | (addr_inv << 8), cmd)
    
    def print_info(self):
        print("Address: 0x{:02X}, Command: 0x{:02X}".format(self.addr, self.cmd))


