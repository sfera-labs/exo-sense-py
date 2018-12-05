import time
import _thread
from exosense import ExoSense
from exosense import thpa_const

exo = ExoSense()
exo.sound.init()
exo.light.init()
exo.thpa.init(gas_heater_temperature=300)

def _sample_sound():
    while True:
        exo.sound.sample()

def _read_thpa():
    while True:
        exo.thpa.read()
        time.sleep(1)

_thread.start_new_thread(_sample_sound, ())
_thread.start_new_thread(_read_thpa, ())

while True:
    print("================")
    print(exo.sound.read())
    print(exo.sound.peak())
    print(exo.sound.avg())

    print(exo.light.device_id())
    print(exo.light.lux())

    print(exo.thpa.temperature())
    print(exo.thpa.humidity())
    print(exo.thpa.pressure())
    print(exo.thpa.gas_resistance())

    print(exo.DI1())
    exo.DO1.toggle()
    print(exo.DO1())

    time.sleep(1)
