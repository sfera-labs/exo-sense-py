class MCP79410:
    def __init__(self, i2c_device=None, addr=0x6f):
        self._i2c = i2c_device
        self._addr = addr

    def init(self, i2c_device, addr=0x6f):
        self._i2c = i2c_device
        self._addr = addr

    def configure(self, control=0x80, osctrim=0x47):
        self._i2c.writeto_mem(self._addr, 0x07, control)
        self._i2c.writeto_mem(self._addr, 0x08, osctrim)

    def get_date(self):
        val = self._i2c.read_byte_data(self._addr, 0x00)
        secone = val & 0b1111
        secten = (val >> 4) & 0b111
        seconds = secten * 10 + secone

        val = self._i2c.read_byte_data(self._addr, 0x01)
        minone = val & 0b1111
        minten = (val >> 4) & 0b111
        minute = minten * 10 + minone

        val = self._i2c.read_byte_data(self._addr, 0x02)
        hrone = val & 0b1111
        hrten = (val >> 4) & 0b11
        hr12 = (val >> 6) & 0b1
        hradd = 0
        if hr12 == 1:
            hrpm = (hrten >> 1)
            hrten &= 0b1
            if hrpm == 1:
                hradd = 12
        hour = hrten * 10 + hrone + hradd

        val = self._i2c.read_byte_data(self._addr, 0x04)
        dateone = val & 0b1111
        dateten = (val >> 4) & 0b11
        day = dateten * 10 + dateone

        val = self._i2c.read_byte_data(self._addr, 0x05)
        mthone = val & 0b1111
        mthten = (val >> 4) & 0b1
        month = mthten * 10 + mthone

        val = self._i2c.read_byte_data(self._addr, 0x06)
        yrone = val & 0b1111
        yrten = (val >> 4) & 0b1111
        year = yrten * 10 + yrone

        return (year, month, day, hour, minute, seconds)

    def set_date(self, year, month, day, hour, minute, seconds):
        secten = (seconds // 10)
        secone = (seconds % 10)
        val = 0x80 | (secten << 4) | secone
        self._i2c.writeto_mem(self._addr, 0x00, val)

        minten = (minute // 10)
        minone = (minute % 10)
        val = (minten << 4) | minone
        self._i2c.writeto_mem(self._addr, 0x01, val)

        hrten = (hour // 10)
        hrone = (hour % 10)
        val = (hrten << 4) | hrone
        self._i2c.writeto_mem(self._addr, 0x02, val)

        dateten = (day // 10)
        dateone = (day % 10)
        val = (dateten << 4) | dateone
        self._i2c.writeto_mem(self._addr, 0x04, val)

        mthten = (month // 10)
        mthone = (month % 10)
        MM = (mthten << 4) | mthone
        self._i2c.writeto_mem(self._addr, 0x05, MM)

        year %= 100
        yrten = (year // 10)
        yrone = (year % 10)
        val = (yrten << 4) | yrone
        self._i2c.writeto_mem(self._addr, 0x06, val)
