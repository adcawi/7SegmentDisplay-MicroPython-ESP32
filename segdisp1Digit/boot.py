# This file is executed on every boot (including wake-boot from deepsleep)
import webrepl
import machine

machine.freq(240000000)
import os
webrepl.start(password = 'x')

# For allowing a connection with ampy, esp osdebug needs to be turned off.
import esp
esp.osdebug(None)


