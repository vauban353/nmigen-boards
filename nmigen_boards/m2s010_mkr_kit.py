import subprocess

from nmigen.build import *
from nmigen.vendor.microchip_smartfusion2 import *
from nmigen_boards.resources import *


__all__ = ["DigiKeySmartFusion2MakerKitPlatform"]


class DigiKeySmartFusion2MakerKitPlatform(MicrochipSmartFusion2Platform):
    device      = "M2S010"
    package     = "144 TQ"
    speed       = "STD"
    temperature = "COM"
    voltage     = "1.2"

    default_clk = "clk_50mhz"

    resources   = [
        Resource("clk_50mhz", 0, Pins("23", dir="i"),
                 Clock(50e6), Attrs(GLOBAL=True, IO_STANDARD="LVCMOS33")),

        Resource("DEVRST_N", 0, Pins("72", dir="i"), Attrs(DEDICATED_IO="DEVRST_N")),

        *LEDResources(pins="129 128 125 124 123 122 118 117", invert=True, attrs=Attrs(IO_STANDARD="LVCMOS33")),

        *ButtonResources(
            pins="143 144",
            attrs=Attrs(IO_STANDARD="LVCMOS33")
        ),

        UARTResource(0,
            rx="2", tx="1",
            attrs=Attrs(IO_STANDARD="LVTTL33", PULLUP=1)
        ),

        *SPIFlashResources(0,
            cs_n="103", clk="100", copi="102", cipo="101", wp_n="85", hold_n="87",
            attrs=Attrs(IO_STANDARD="LVCMOS33")
        ),
    ]

    connectors = [
        Connector("mod1", 0, "83 81 90 93 88 82"),
        Connector("j", 7, "92 16 94 21 22"),
    ]

if __name__ == "__main__":
    from nmigen_boards.test.blinky import *
    DigiKeySmartFusion2MakerKitPlatform().build(Blinky(), do_program=False)
