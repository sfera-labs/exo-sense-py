import time
import _thread
from exosense import ExoSense
from exosense import thpa_const

exo = ExoSense()
exo.sound.init()
exo.light.init()
exo.thpa.init(gas_heater_temperature=300, temp_offset=-5, elevation=100)

def _sample_sound():
    while True:
        exo.sound.sample()
        time.sleep_ms(5)

_thread.start_new_thread(_sample_sound, ())

while True:
    exo.thpa.read()

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
    print(exo.thpa.iaq())
    print(exo.thpa.iaq_trend())

    print(exo.DI1())
    exo.DO1.toggle()
    print(exo.DO1())

    time.sleep(2)
